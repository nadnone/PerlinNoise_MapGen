from os import replace
import noise
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot
from numpy.core.numeric import indices


PIXELS = (512, 512)

echelle = 100.0
octaves = 1
details = 0.0
persistance = 1.4

MER = (36,128,214)
HERBE = (10,125,18)
PIERRE = (118,120,117)
SABLE = (209, 206, 115)
NEIGE = (194,194,192)

image_path = "./colored_heighmap.png"
gray_scale_path = "./grayscale_heightmap.png"

image = Image.new(mode="RGBA", size=PIXELS)
gray_scale = Image.new(mode="RGBA", size=PIXELS)


world = np.zeros(PIXELS)

count = 0

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

        world[x][y] = val

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
        

        gray_scale.putpixel((x,y), (int(val*255), int(val*255), int(val*255)))     
"""
ligne_x = np.linspace(-1, 1, PIXELS[0], endpoint=False)
ligne_y = np.linspace(-1, 1, PIXELS[1], endpoint=False)
matx,maty = np.meshgrid(ligne_x, ligne_y)
"""

image.save(image_path)
gray_scale.save(gray_scale_path)

# affichage de la map
"""
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(matx,maty, world, cmap='terrain')
matplotlib.pyplot.show()
"""