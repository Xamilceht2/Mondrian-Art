from PIL import Image, ImageDraw
import random as r


class mondo:
    def __init__(self, tl, br, minval):
        # create blank canvas / image
        self.im = Image.new('RGBA', (tl, br), (0, 0, 0))
        self.minval = minval
        self.draw = ImageDraw.Draw(self.im)
        # Blue pallet
        self.colours = {
            1: (0, 0, 255, 255),
            2: (0, 0, 128, 255),
            3: (65, 105, 225, 255),
            4: (100, 149, 237, 255),
            5: (173, 216, 230, 255),
            6: (135, 206, 235, 255),
            7: (0, 191, 255, 255),
            8: (30, 144, 255, 255),
            9: (70, 130, 180, 255),
            10: (119, 136, 153, 255),
            11: (0, 0, 255, 50),
            12: (0, 0, 200, 255),
            13: (50, 80, 200, 255)
        }

    def show(self):
        # shows image in pycharm
        self.im.show()

    def border(self, x1, y1, x2, y2):
        """
        :param x1: 
        :param y1: 
        :param x2: 
        :param y2: 
        :return:tuple within 20% of the x and y borders 
        """
        x_less = int((x2 - x1) * 0.3)
        x = r.randint(x1 + x_less, x2 - x_less)
        y_less = int((y2 - y1) * 0.3)
        y = r.randint(y1 + y_less, y2 - y_less)
        return x, y

    def split(self, tl, br):
        '''
        :param tl: top left point
        :param br: bottom right point
        :return: Recursive Function
        '''
        # Random touch
        if r.randint(0, 10) > 9:
            self.minval = 100
        if r.randint(0, 10) > 9:
            self.minval = 300
        if r.randint(0, 20) > 9:
            self.minval = 200

        if br[0] - tl[0] < self.minval or br[1] - tl[1] < self.minval:
            # Draw Rectangle if not recursively calling anymore
            c = self.colours[r.randint(1, len(self.colours))]
            self.draw.rectangle([tl, br], fill=c, outline="black", width=2)

        else:
            # Create rectangle points inside tl and br within 20%
            p1 = self.border(tl[0], tl[1], br[0], br[1])
            p2 = self.border(p1[0], p1[1], br[0], br[1])
            
            # split 5 ways and define each sector
            a = ((tl[0], tl[1]), (p2[0], p1[1]))
            b = ((tl[0], p1[1]), (p1[0], br[1]))
            c = ((p2[0], tl[1]), (br[0], p2[1]))
            d = ((p1[0], p2[1]), (br[0], br[1]))
            e = ((p1[0], p1[1]), (p2[0], p2[1]))
            
            # recall function for each of the defined sectors
            self.split(a[0], a[1])

            self.split(b[0], b[1])

            self.split(c[0], c[1])

            self.split(d[0], d[1])

            self.split(e[0], e[1])

z = mondo(1000, 1000, 100)
z.split((0, 0), (1000, 1000))
z.show()
