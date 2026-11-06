""" reading and processing input file with python-opencv """

import cv2

class InputVideo:
    """ operate on input video based off filename fn """
    def __init__(self, fn: str, max_px: int):
        self.video = cv2.VideoCapture(fn)
        # not all codecs offer such metadata
        self._frame_count, self._dur = self.get_metadata(fn)

        self._frame_dim: tuple[int, int] = InputVideo.get_dimensions(
            self.video.get(cv2.CAP_PROP_FRAME_WIDTH),
            self.video.get(cv2.CAP_PROP_FRAME_HEIGHT),
            max_px
        ) # width, height

    @property
    def frame_count(self): return self._frame_count
    @property
    def dur(self): return self._dur
    @property
    def fps(self): return self.frame_count / self.dur
    
    @property
    def width(self): return self._frame_dim[0]
    @property
    def height(self): return self._frame_dim[1]

    @staticmethod
    def get_dimensions(w: float, h: float, max_px: int) -> tuple[int, int]:
        """ calculate dimensions to resize to based of max_px """
        if max(w, h) <= max_px:
            return int(w), int(h)

        if w > h:
            return max_px, int((max_px / w) * h)
        else:
            return int((max_px / h) * w), max_px

    @staticmethod
    def get_metadata(fn: str) -> tuple[int, float]:
        """ read until failure, and increment data.
        returns frame count, duration (in secs)
        """
        frame_count: int = 0; duration: float = 0.0
        copy = cv2.VideoCapture(fn)
        if not copy.isOpened():
            return frame_count, duration
        
        while True:
            duration = copy.get(cv2.CAP_PROP_POS_MSEC)
            is_success, _ = copy.read()
            if not is_success: break
            frame_count += 1
        copy.release()

        return frame_count, duration / 1000

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
