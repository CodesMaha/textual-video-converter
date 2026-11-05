import yt_dlp

def download_clip(url: str) -> str:
    """ download .mkv clip to fn then return that fn. verbose=True """

    yt_opts = {
        "verbose": True, "overwrites": True,
        "outtmpl": "from_youtube.%(ext)s"
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        fn = ydl.prepare_filename(info)

    return fn

if __name__ == "__main__":
    download_clip("https://youtu.be/DzrwK8uDiiE")
