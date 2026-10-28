""" manipulate frame arrs for use """

import cv2
import pygame
from numpy import array, uint8, str_
from numpy.typing import NDArray

def surf_to_arr(frame_surf: pygame.Surface) -> NDArray[uint8]:
    """ convert surface into usable arr for cv2 """

    # get height, width arr
    frame_surf_arr = pygame.surfarray.array3d(
        frame_surf
    ).transpose(1, 0, 2)

    # get bgr arr
    frame_surf_arr = cv2.cvtColor(
        frame_surf_arr, cv2.COLOR_RGB2BGR
    )

    return frame_surf_arr

def get_char_lookup(chars: str) -> NDArray[str_]:
    """ spread gvn chars across 256 indices """
    size_o: int = 2**8; n_chars: int = len(chars)

    # handle the case of < size_o
    char_lookup: list[str] = [chars[0]] * (size_o % n_chars)
    for i in range(n_chars): # dist wrt len
        char_lookup.extend([chars[i]] * (size_o // n_chars))

    return array(char_lookup)
