""" reading and processing input file with python-opencv """

import cv2

class InputVideo:
    """ operate on input video based off filename fn """
    def __init__(self, fn: str, max_px: int):
        self.video = cv2.VideoCapture(fn)

        self._fps: float = self.video.get(cv2.CAP_PROP_FPS)
        self._total_sec: float = self.video.get(
            cv2.CAP_PROP_FRAME_COUNT
        ) // self.fps
        self._frame_dim: tuple[int, int] = InputVideo.get_dimensions(
            self.video.get(cv2.CAP_PROP_FRAME_WIDTH),
            self.video.get(cv2.CAP_PROP_FRAME_HEIGHT),
            max_px
        ) # width, height

    @property
    def fps(self):
        return self._fps
    @property
    def time(self):
        return self._total_sec
    
    @property
    def width(self):
        return self._frame_dim[0]
    @property
    def height(self):
        return self._frame_dim[1]

    @staticmethod
    def get_dimensions(w: float, h: float, max_px: int) -> tuple[int, int]:
        """ calculate dimensions to resize to based of max_px """
        if max(w, h) <= max_px:
            return int(w), int(h)

        if w > h:
            return max_px, int((max_px / w) * h)
        else:
            return int((max_px / h) * w), max_px

    def read_frame_arr(self):
        """ return resized luminosity arr """
        is_success, frame = self.video.read()

        if not is_success:
            raise ValueError("could not successfully read frame")

        frame = cv2.cvtColor(
            cv2.resize(frame, self._frame_dim),
            cv2.COLOR_BGR2GRAY
        ) #  two-dimensional compressed np arr

        return frame

    def is_opened(self):
        return self.video.isOpened()

    def release(self):
        self.video.release()
