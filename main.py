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

fn = get_filename(con.FILE_TYPES)
inp = InputVideo(fn, con.MAX_PX)

render = FontRenderer(con.FONT_NAME, con.FONT_SIZE, con.FONT_COL)
frame_surf = pygame.surface.Surface(
    (inp.width * render.width, inp.height * render.width)
)

fn = reformat_filename(fn, con.FN_ADDITION, con.FILE_EXTENSION)
out = cv2.VideoWriter(
    fn, cv2.VideoWriter_fourcc(*con.FOURCC_CODEC), 
    con.OUTPUT_FPS or inp.fps, frame_surf.size
)

seconds = inp.time
if (con.MAX_SECS) and (con.MAX_SECS < inp.time):
    seconds = con.MAX_SECS

for _ in range(int(seconds * inp.fps)):
    frame = inp.read_frame_arr()
    frame = match_char(frame)
    frame_surf.fill(con.BG_COL)
    render.draw_lines(frame_surf, frame)
    frame = surf_to_arr(frame_surf)
    out.write(frame)

inp.release()
out.release()