# textual video converter
convert coloured videos to those made up of symbols. 

# usage
First, `cd` to [local root directory](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository). 

Then, use `python -m convert -h` to check usage.

![one hundred and twenty-five high-contrast frames.](example.gif)

(`example.gif` can be used for testing.)

## running subcommands through shell
`local` subcommand:
* provide filepath to input video;
* optionally enter filepath to output video.
```
python -m convert local [-o OUTPUT_FILEPATH] INPUT_FILEPATH
```
`youtube` subcommand:
+ provide link to desired video for downloaded;
+ optionally pass in time arguments in seconds for trimming after download.
```
python -m convert youtube [-i INITIAL_TIMESTAMP] [-d DURATION] INPUT_URL
```

## dependencies
* `opencv-python` is required for putting together videos.
* `pygame-ce` is required for drawing on videos.
* `yt-dlp` is required for downloading videos.
```
├── opencv-python v5.0.0.93
│   └── numpy v2.5.1
├── pygame-ce v2.5.7
└── yt-dlp v2026.7.4
```

# notice

**overwriting**:

files are overwritten. for example, if there is already an `example_textual.mp4` file present, then it will be overwritten when processing `example.gif` again. this can be avoided by renaming the file manually or providing a unique output filepath

---

**failure viewing**:

due to the nature of how videos are encoded through `opencv-python`, the output might not be able to be successfully displayed everywhere.

# config
there are certain limitations and other values set, but they are mostly arbitrary. for example, there is an option to process less symbols or pixels per frame, but it can be increased for clarity or further decreased for processing speed.
