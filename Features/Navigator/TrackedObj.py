class TrackedObj:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.lr = 0.001
        self.velocity = 0
