from PIL import Image, ImageDraw
import random as r

def split(tl, br):
    p1 = (r.randint(tl[0], br[0]), r.randint(br[1], tl[1]))
    w = r.randint(p1[0], br[0])
    h = r.randint(br[1], p1[1])
    p2 = (w, h)
    draw.line((tl[0], p1[1], p2[0], p1[1]), 0, 2)
    draw.line((p1[0], p1[1], p1[0], br[1]), 0, 2)
    draw.line((p1[0], p2[1], br[0], p2[1]), 0, 2)
    draw.line((p2[0], tl[1], p2[0], p2[1]), 0, 2)
    a = ((tl[0], tl[1]), (p2[0], p1[1]))
    b = ((tl[0] , p1[1]), (p1[0], br[1]))
    c = ((p2[0], tl[1]), (br[0], p2[1]))
    d = ((p1[0], p2[1]), (br[0], br[1]))
    e = ((p1[0], p1[1]), (p2[0], p2[1]))
    if a[0][1] <= 50 or a[1][0] <= 50:
        return None
    else:
        print('running')
        return split(a[0], a[1])
    

im = Image.new('RGB', (720, 720), (255, 255, 255))
draw = ImageDraw.Draw(im)
split((0, 720), (720, 0))
im.show()