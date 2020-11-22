class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.tower_imgs = []

    def draw(self, win):
        img = self.tower_imgs[self.level]
        win.blit(img, (self.x/img.get_width()/2, self.y/img.get_height()/2))

    def click(self):
        pass

    def sell(self):
        pass