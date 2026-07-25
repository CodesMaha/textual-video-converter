# text video converter
convert coloured videos to those made up of symbols. 

# usage
there is a five-second example file named `example.gif` that can be used for testing.

![one hundred and twenty-five high-contrast frames.](example.gif)

* select file in some directory;
* view new file saved to that directory.

## failure viewing
due to the nature of how `python-opencv` encodes videos, the output might not be able to be successfully displayed everywhere.

# config
there are certain limitations and other values set, but they are mostly arbitrary. for example, there is an option to process less symbols or pixels per frame, but it can be increased for clarity or further decreased for processing speed.