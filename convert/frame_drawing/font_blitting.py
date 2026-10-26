""" 
pygame.font required to be initialized 
for symbols to be rendered into font surfaces 
"""

import pygame

class FontRenderer:
    def __init__(
            self, font_name: str, font_size: int,
            font_colour: tuple[int, int, int]
        ):
        self.font = pygame.font.SysFont(font_name, font_size)
        self._w = self.font.size("W")[0]
        self.col = font_colour

    @property
    def width(self):
        return self._w

    def get_font_render(self, text: str) -> pygame.Surface:
        """ get font.render ready to blit """
        return self.font.render(text, True, self.col)

    def draw_lines(self, surf: pygame.Surface, lines):
        """ 
        get frame array of individual symbols then join them 
        to draw onto surface line by line 
        """
        for line, y in zip(lines, range(0, self._w*len(lines), self._w)):
            text_img = self.get_font_render("".join(line))
            surf.blit(text_img, (0, y))
