from os import replace
import noise
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot


PIXELS = (1000, 1000)

echelle = 300.0
octaves = 1
details = 0.2
persistance = 0.6

MER = (36,128,214)
HERBE = (10,125,18)
PIERRE = (118,120,117)
SABLE = (209, 206, 115)
NEIGE = (194,194,192)

image_path = "./colored_heighmap.png"
gray_scale_path = "./grayscale_heightmap.png"

image = Image.new(mode="RGB", size=PIXELS)
#gray_scale = Image.new(mode="RGB", size=PIXELS)

#data_map = open("heightmap.heightmap", "w")

world = np.zeros(PIXELS)


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
        
        #gray_scale.putpixel((x,y), (int(val*255), int(val*255), int(val*255)))


lin_x = np.linspace(-1, 1, PIXELS[0], endpoint=False)
lin_y = np.linspace(-1, 1, PIXELS[1], endpoint=False)
c_x, c_y = np.meshgrid(lin_x, lin_y)





"""

for i in range(0, len(c_x)):
    for j in range(0, len(c_x)):

        # formation d'un plan triangulé

        # triangle 1
        data_map.write(f"{c_y[i][j]} {c_y[i][j]} {world[i][j]}\n")
        data_map.write(f"{x} {val} {y}\n")
        data_map.write(f"{x} {val} {y}\n")

        # triangle 2
        data_map.write(f"{x} {val} {y}\n")
        data_map.write(f"{x} {val} {y}\n")
        data_map.write(f"{x} {val} {y}\n")
"""



image.save(image_path)
#gray_scale.save(gray_scale_path)

#data_map.close()

# affichage de la map

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(c_x,c_y, world, cmap='terrain')
matplotlib.pyplot.show()