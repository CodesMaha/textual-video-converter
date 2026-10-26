import yt_dlp
import cv2

from os import replace

def download_clip(url:str) -> str:
    """ download .mp4 clip to fn then return that fn. verbose=True """
    fn = "from_youtube.mp4"

    yt_opts = {
        "verbose": True, "overwrites": True,
        "outtmpl": "from_youtube.mp4"
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download(url)

    return fn

def trim_clip(fn: str, initial:float=0.0, duration:float=0.0) -> None:
    """ 
    modify .mp4 clip to only use a portion of it, 
    then replace clip with modified clip.
    also print frame counts (verbose)
    """
    if (initial == 0) and (duration == 0):
        return # no need to trim
    
    inp = cv2.VideoCapture(fn)

    fps = inp.get(cv2.CAP_PROP_FPS)

    i_frame = int(fps * initial) or 1
    inp.set(cv2.CAP_PROP_POS_FRAMES, i_frame)

    if not duration:
        f_frame = inp.get(cv2.CAP_PROP_FRAME_COUNT) - i_frame
    else:
        f_frame = int(duration * fps)

    print(f"\ntrimming from frame {i_frame} to {i_frame + f_frame}")

    new_fn = f"{fn.rsplit('.', 1)[0]}_trimmed.mp4"
    out = cv2.VideoWriter(
        new_fn, cv2.VideoWriter_fourcc(*"mp4v"), fps, 
        (
            int(inp.get(cv2.CAP_PROP_FRAME_WIDTH)), 
            int(inp.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
    )

    for _ in range(int(f_frame)):
        is_success, frame = inp.read()
        if not is_success:
            raise OSError("could not read frame while trimming")
        out.write(frame)

    inp.release()
    out.release()

    replace(new_fn, fn)

if __name__ == "__main__":
    download_clip("https://youtu.be/6AiTpL_PywQ")
