""" 
run via command line, so first cd to dir.
then e.g. python -m convert local example.gif
"""

import argparse 
from .convert import convert
from .frame_processing.get_download import download_clip

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
parser.add_argument(
    "-i", "--initial", type=float, default=0,
    help=(
        "initial timestamp in seconds to process "
        "frames from. default is start or second zero"
    )
); parser.add_argument(
    "-d", "--duration", type=float, default=0,
    help=(
        "duration of output video unless config " 
        "concedes it. default is end or value zero"
    )
)


# python -m convert -i 26.5 -d 4 youtube https://youtu.be/DzrwK8uDiiE
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


args = parser.parse_args()

if args.subcommand == "local":
    inp_fn = args.input
elif args.subcommand == "youtube":
    inp_fn = download_clip(args.url)
out_fn = args.output
stop_time = args.initial + args.duration if args.duration else 0

convert(inp_fn, out_fn, args.initial, stop_time)
