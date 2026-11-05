from .frame_drawing.arr_manip import get_char_lookup

CHAR_ARR = get_char_lookup(" #@") # " .'`-^~:;=!+$*#@"

# output video
# 0 | None means use original, but that might
# be bugged if no value is associated with file
OUTPUT_FPS: None | int = 30 # 0 | None means use original

MAX_PX: int = 100 # for width and height compression

FOURCC_CODEC: str = "mp4v"
FILE_EXTENSION: str = ".mp4"
FN_ADDITION: str = "_textual"

# square text
FONT_NAME: str = "monospace"
FONT_SIZE: int = 16

# colours
FONT_COL: tuple[int, int, int] = (255, 255, 255) # white
BG_COL: tuple[int, int, int] = (0, 0, 0) # black
