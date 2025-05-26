from PIL import Image, ImageDraw
import random as r

class mondo:
    def __init__(self, tl, br, minval):
        self.im = Image.new('RGBA', (tl, br), (0, 0, 0))
        self.minval = minval
        self.draw = ImageDraw.Draw(self.im)

        self.colours = ["#ffff33", "#ffffff", "#00f3ff", "#af00b3"]

    def show(self):
        self.im.show()

    def split(self, tl, br):
        if r.randint(0, 10) > 9:
            self.minval = 300

        if br[0] - tl[0] < self.minval or br[1] - tl[1] < self.minval:
            # draw
            c = self.colours[r.randint(0, len(self.colours)) - 1]

            self.draw.rectangle([tl, br], fill=c, outline="black", width=2)

        else:
            p1 = (r.randint(tl[0], br[0]), r.randint(tl[1], br[1]))
            w = r.randint(p1[0], br[0])
            h = r.randint(p1[1], br[1])
            p2 = (w, h)
            a = ((tl[0], tl[1]), (p2[0], p1[1]))
            b = ((tl[0], p1[1]), (p1[0], br[1]))
            c = ((p2[0], tl[1]), (br[0], p2[1]))
            d = ((p1[0], p2[1]), (br[0], br[1]))
            e = ((p1[0], p1[1]), (p2[0], p2[1]))

            self.split(a[0], a[1])

            self.split(b[0], b[1])

            self.split(c[0], c[1])

            self.split(d[0], d[1])

            self.split(e[0], e[1])



z = mondo(1000, 1000, 100)
z.split((0, 0),(1000, 1000))
z.show()