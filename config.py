from numpy import array

CHAR_ARR = array(list(" .'`-^~:;=!+$*#@"))
LUMINANCE_STEP: int = 255 // (CHAR_ARR.size - 1)

# output video
OUTPUT_FPS: None | int = None # None means use original
MAX_SECS: None | int = None # input video length

MAX_PX: int = 100 # for width and height compression

FOURCC_CODEC: str = "mp4v"
FILE_EXTENSION: str = ".mp4"
FN_ADDITION: str = "_textual"

FILE_TYPES: tuple[tuple[str]] = (
    ("all", "*.*"), ("gif", "*.gif"), ("mp4", "*.mp4")
)

# square text
FONT_NAME: str = "monospace"
FONT_SIZE: int = 16

# colours
FONT_COL: tuple[int, int, int] = (255, 255, 255) # white
BG_COL: tuple[int, int, int] = (0, 0, 0) # black