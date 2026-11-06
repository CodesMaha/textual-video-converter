from . import config as con

import cv2
import pygame

from numpy import uint8, str_
from numpy.typing import NDArray

from .frame_processing.get_frame_arr import InputVideo

from .frame_drawing.font_blitting import FontRenderer
from .frame_drawing.arr_manip import surf_to_arr

pygame.font.init()

def reformat_filename(fn: str, to_insert: str, f_ext: str) -> str:
    """ take filename and add to_insert before the f_ext """
    return "".join((fn.rsplit(".", 1)[0], to_insert, f_ext))

def match_char(frame_luminance_arr: NDArray[uint8]) -> NDArray[str_]:
    """ replace frame luminance values with symbols """
    return con.CHAR_ARR[frame_luminance_arr]

def print_progress(frame_no: int, max_frame_count: int) -> None:
    if (frame_no % max(1, (max_frame_count // 4))) == 0:
        print(f"| {(frame_no / max_frame_count)*100}%", end=" |", flush=True)

def convert(
        inp_fn:str|None=None, out_fn:str|None=None,
    ):
    print("\nattempting to open file and count number of available frames")
    inp = InputVideo(inp_fn, con.MAX_PX)

    if not inp.is_opened():
        raise OSError(
            "could not open input file. "
            f"possible invalid directory: {inp_fn}"
        )
    print("\ninput file opened successfully")

    render = FontRenderer(con.FONT_NAME, con.FONT_SIZE, con.FONT_COL)
    frame_surf = pygame.surface.Surface(
        (inp.width * render.width, inp.height * render.width)
    )

    fn = out_fn or reformat_filename(inp_fn, con.FN_ADDITION, con.FILE_EXTENSION)
    out = cv2.VideoWriter(
        fn, cv2.VideoWriter_fourcc(*con.FOURCC_CODEC), 
        con.OUTPUT_FPS or inp.fps, frame_surf.size
    )

    if not out.isOpened():
        inp.release()
        raise OSError(
            "could not initialize output file. "
            f"possible invalid directory: {fn}"
        )
    print("output file initialized successfully")

    frame_count: int = inp.frame_count
    if con.MAX_SECS:
        frame_count = min(frame_count, int(con.MAX_SECS * inp.fps))
    if con.MAX_FRAMES:
        frame_count = min(frame_count, con.MAX_FRAMES)

    print(
        f"\nprocessing {frame_count} frames where "
        f"fps is {inp.fps:.2f} and duration "
        f"is {frame_count / inp.fps:.2f} sec"
    )
    for frame_no in range(frame_count):
        frame = inp.read_frame_arr()
        frame = match_char(frame)
        frame_surf.fill(con.BG_COL)
        render.draw_lines(frame_surf, frame)
        frame = surf_to_arr(frame_surf)
        print_progress(frame_no, frame_count)
        out.write(frame)

    print("\n\nsaving output and terminating")
    inp.release()
    out.release()
