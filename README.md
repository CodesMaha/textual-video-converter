# text video converter
convert coloured videos to those made up of symbols. 

# usage
![one hundred and twenty-five high-contrast frames.](example.gif)

(`example.gif` can be used for testing.)

### running `convert.py` through shell…
---
using the `local` subcommand:
* provide filepath to input video;
* optionally enter filepath to output video.
```
python convert.py local [-o OUTPUT_FILEPATH] INPUT_FILEPATH
```
using the `youtube` subcommand:
+ provide link to desired video to be downloaded;
+ optionally pass in time arguments in seconds for trimming after download.
```
python convert.py youtube [-i INITIAL_TIMESTAMP] [-d DURATION] INPUT_URL
```

## dependencies
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