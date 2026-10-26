""" connect pygame-ce to python-opencv """

import cv2
import pygame

def surf_to_arr(frame_surf: pygame.Surface):
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
