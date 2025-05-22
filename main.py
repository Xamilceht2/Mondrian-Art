from PIL import Image, ImageDraw
import random as r

def split(tl, br):
    minval = 100

    if r.randint(0, 10) >9:
       minval = 500

    if br[0] -tl[0] < minval or br[1] -tl[1] < minval:
        #draw
        c = colours[ r.randint(0, len(colours))-1]
        
        

        draw.rectangle( [tl,br], fill = c, outline="black", width=2)


    else:
        p1 = (r.randint(tl[0], br[0]), r.randint(tl[1], br[1]))
        w = r.randint(p1[0], br[0])
        h = r.randint(p1[1], br[1])
        p2 = (w, h)
        '''
        draw.line((tl[0], p1[1], p2[0], p1[1]), 0, 2)
        draw.line((p1[0], p1[1], p1[0], br[1]), 0, 2)
        draw.line((p1[0], p2[1], br[0], p2[1]), 0, 2)
        draw.line((p2[0], tl[1], p2[0], p2[1]), 0, 2)
        '''
        a = ((tl[0], tl[1]), (p2[0], p1[1]))
        b = ((tl[0], p1[1]), (p1[0], br[1]))
        c = ((p2[0], tl[1]), (br[0], p2[1]))
        d = ((p1[0], p2[1]), (br[0], br[1]))
        e = ((p1[0], p1[1]), (p2[0], p2[1]))


        print('running')
        split(a[0], a[1])

        split(b[0], b[1])

        split(c[0], c[1])

        split(d[0], d[1])

        split(e[0], e[1])

colours = ["#ffff33", "#ffffff", "#00f3ff", "#af00b3"]

im = Image.new('RGBA', (1000, 1000), (0, 0, 0))
draw = ImageDraw.Draw(im)
split((0, 0), (1000, 1000))
im.show()