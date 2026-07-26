""" 
run via terminal like so: first cd to dir then
python convert.py abc.cba -o xyz.zyx 
"""

import argparse 
from main import main

parser = argparse.ArgumentParser(
    description="turn video colour into symbols"
)

parser.add_argument(
    "input",
    help="filepath of the file to convert"
)
parser.add_argument(
    "-o", "--output", 
    help=(
        "filepath for output file, but if not specified "
        "then a new file is created in the same directory "
        "as the input file"
    )
)

args = parser.parse_args()

main(args.input, args.output, verbose=True)