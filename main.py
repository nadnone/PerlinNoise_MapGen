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
data_map = open("heightmap.heightmap", "w")

for x in range(PIXELS[0]):
    for y in range(PIXELS[1]):
        
        val = noise.pnoise2(
            x/echelle,
            y/echelle,
            octaves=octaves,
            persistence=persistance,
            repeatx=PIXELS[0],
            repeaty=PIXELS[1],
            base=0
            )

        if val < -0.07:
            image.putpixel((x,y), MER)
        elif val < 0.0:
            image.putpixel((x,y), SABLE)
        elif val < 0.25:
            image.putpixel((x,y), HERBE)
        elif val < 0.5:
            image.putpixel((x,y), PIERRE)
        elif val < 1.0:
            image.putpixel((x,y), NEIGE)
        
        #image.putpixel((w,h), (int(val*255), int(val*255), int(val*255)))

        # formation d'un plan triangulé
        
        x_c = x/512.0
        y_c = y/512.0

        # triangle 1
        data_map.write(f"{x_c-1} {val} {y_c+1}\n")
        data_map.write(f"{x_c+1} {val} {y_c+1}\n")
        data_map.write(f"{x_c+1} {val} {y_c-1}\n")

        # triangle 2
        data_map.write(f"{x_c-1} {val} {y_c+1}\n")
        data_map.write(f"{x_c-1} {val} {y_c-1}\n")
        data_map.write(f"{x_c+1} {val} {y_c-1}\n")

        # TODO A REVOIR !

image.save(image_path)
data_map.close()