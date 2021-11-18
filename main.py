from os import replace
import noise
from PIL import Image

PIXELS = (512, 512)

echelle = 150.0
octaves = 2
details = 3.0
persistance = 6.0

MER = (36,128,214)
HERBE = (10,125,18)
PIERRE = (118,120,117)
SABLE = (209, 206, 115)
NEIGE = (194,194,192)

image_path = "./heighmap.png"

image = Image.new(mode="RGB", size=PIXELS)


for w in range(PIXELS[0]):
    for h in range(PIXELS[1]):
        
        val = noise.pnoise2(
            w/echelle,
            h/echelle,
            octaves=octaves,
            persistence=persistance,
            repeatx=PIXELS[0],
            repeaty=PIXELS[1],
            base=0
            )

        if val < -0.07:
            image.putpixel((w,h), MER)
        elif val < 0:
            image.putpixel((w,h), SABLE)
        elif val < 0.25:
            image.putpixel((w,h), HERBE)
        elif val < 0.5:
            image.putpixel((w,h), PIERRE)
        elif val < 1.0:
            image.putpixel((w,h), NEIGE)


image.save(image_path)