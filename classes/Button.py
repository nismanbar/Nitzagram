class Button:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def is_hovered(self, pos):
        return self.x_pos <= pos[0] <= self.x_pos + self.width and self.y_pos <= pos[1] <= self.y_pos + self.height
