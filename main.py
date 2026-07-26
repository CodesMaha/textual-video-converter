import config as con

import cv2
import pygame

from frame_processing.get_file_info import *
from frame_processing.get_frame_arr import InputVideo

from frame_drawing.font_blitting import FontRenderer
from frame_drawing.arr_conversion import surf_to_arr

pygame.font.init()

def match_char(frame_luminance_arr):
    """ replace frame luminance values with symbols """
    frame_luminance_arr //= con.LUMINANCE_STEP
    return con.CHAR_ARR[frame_luminance_arr]

def print_progress(frame_no: int, max_frame_count: int) -> None:
    if (frame_no % max(1, (max_frame_count // 4))) == 0:
        print(f"| {(frame_no / max_frame_count)*100}%", end=" |", flush=True)

def main(
        inp_fn:str|None=None, out_fn:str|None=None,
        verbose:bool=False
    ):
    fn = inp_fn or get_filename(con.FILE_TYPES)
    inp = InputVideo(fn, con.MAX_PX)

    if not inp.is_opened():
        raise OSError(
            "could not open input file. "
            f"possible invalid directory: {fn}"
        )
    elif verbose:
        print("\ninput file opened successfully\n")

    render = FontRenderer(con.FONT_NAME, con.FONT_SIZE, con.FONT_COL)
    frame_surf = pygame.surface.Surface(
        (inp.width * render.width, inp.height * render.width)
    )

    fn = out_fn or reformat_filename(fn, con.FN_ADDITION, con.FILE_EXTENSION)
    out = cv2.VideoWriter(
        fn, cv2.VideoWriter_fourcc(*con.FOURCC_CODEC), 
        con.OUTPUT_FPS or inp.fps, frame_surf.size
    )

    if not out.isOpened():
        raise OSError(
            "could not initialize output file. "
            f"possible invalid directory: {fn}"
        )
    elif verbose:
        print("output file initialized successfully\n")

    seconds = inp.time
    if (con.MAX_SECS) and (con.MAX_SECS < inp.time):
        seconds = con.MAX_SECS

    frame_count: int = int(seconds * inp.fps)
    for frame_no in range(frame_count):
        frame = inp.read_frame_arr()
        frame = match_char(frame)
        frame_surf.fill(con.BG_COL)
        render.draw_lines(frame_surf, frame)
        frame = surf_to_arr(frame_surf)
        if verbose:
            print_progress(frame_no, frame_count)
        out.write(frame)

    if verbose: print("\n\nsaving output and terminating")
    inp.release()
    out.release()

if __name__ == "__main__":
    main()