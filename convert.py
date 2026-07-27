""" 
run via command line, so first cd to dir.
then e.g. python convert.py local example.gif
"""

import argparse 
from main import convert
from frame_processing.get_download import *

parser = argparse.ArgumentParser(
    description="turn video colour into symbols"
)

parser.add_argument(
    "-o", "--output", default=None,
    help=(
        "filepath for output file, but if not specified "
        "then a new file is created in the same directory "
        "as the input file"
    )
)

# python convert.py youtube https://www.youtube.com/watch?v=DzrwK8uDiiE -i 26.5 -d 4
subparsers = parser.add_subparsers(dest="subcommand")

local_convert = subparsers.add_parser("local")
local_convert.add_argument(
    "input",
    help="filepath of the file to convert"
)


youtube_convert = subparsers.add_parser("youtube")
youtube_convert.add_argument(
    "url",
    help="url to youtube video to download from"
)

youtube_convert.add_argument(
    "-i", "--initial", type=float, default=0,
    help=(
        "initial time in seconds to clip from; default "
        "is at beginning of youtube video or zero seconds"
    )
)
youtube_convert.add_argument(
    "-d", "--duration", type=float, default=0,
    help=(
        "duration of clip in seconds after initial time "
        "where the default is at end or zero"
    )
)


args = parser.parse_args()

if args.subcommand == "local":
    inp_fn, out_fn = args.input, args.output
elif args.subcommand == "youtube":
    inp_fn, out_fn = download_clip(args.url), args.output
    trim_clip(inp_fn, args.initial, args.duration)

convert(inp_fn, out_fn)