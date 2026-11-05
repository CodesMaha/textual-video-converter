""" reading and processing input file with python-opencv """

import cv2

class InputVideo:
    """ operate on input video based off filename fn """
    def __init__(self, fn: str, max_px: int):
        self.video = cv2.VideoCapture(fn)
        # not all codecs offer such metadata
        self._frame_no = self.get_frame_no(fn)

        self._frame_dim: tuple[int, int] = InputVideo.get_dimensions(
            self.video.get(cv2.CAP_PROP_FRAME_WIDTH),
            self.video.get(cv2.CAP_PROP_FRAME_HEIGHT),
            max_px
        ) # width, height

    @property
    def frame_no(self): return self._frame_no
    
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
    def get_frame_no(fn: str):
        """ read until failure. one-indexed """
        frame_no: int = 0
        copy = cv2.VideoCapture(fn)
        if not copy.isOpened():
            return frame_no
        
        while True:
            is_success, _ = copy.read()
            if not is_success: break
            frame_no += 1

        return frame_no

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
