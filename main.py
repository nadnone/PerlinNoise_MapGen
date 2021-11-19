from os import replace
import noise
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot
from numpy.core.numeric import indices


PIXELS = (512, 512)

echelle = 50.0
octaves = 1
details = 1.0
persistance = 0.2

MER = (36,128,214)
HERBE = (10,125,18)
PIERRE = (118,120,117)
SABLE = (209, 206, 115)
NEIGE = (194,194,192)

image_path = "./colored_heighmap.png"
gray_scale_path = "./grayscale_heightmap.png"

#image = Image.new(mode="RGB", size=PIXELS)
#gray_scale = Image.new(mode="RGB", size=PIXELS)

data_map_data = open("world/heightmap_verticecs.data_map", "w")
#data_map_indices = open("world/heightmap_verticecs.indices", "w")

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
        """
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
        """
        #gray_scale.putpixel((x,y), (int(val*255), int(val*255), int(val*255)))     

        # formation d'un carré triangulé
        
        o = {
            "x": x/2,
            "z": y/2
        }
        
        position_carre = [
            [
                o["x"]/2,
                0,
                o["z"]*2
            ],
            [
                o["x"],
                0,
                o["z"]*2
            ],
            [
                o["x"]*2,
                0,
                o["z"]*2
            ],
            [
                o["x"]*2,
                0,
                o["z"]
            ],
            [
                o["x"]*2,
                0,
                o["z"]/2
            ],
            [
                o["x"],
                0,
                o["z"]/2
            ],
            [
                o["x"]/2,
                0,
                o["z"]/2
            ],
            [
                o["x"]/2,
                0,
                o["z"]
            ],
            [
                o["x"],
                val* 10,
                o["z"]
            ]

        ]

        """
        sommet = 9
        for i in range(0, 9):
            data_map_data.write(f"P {position_carre[i][0]} {position_carre[i][1]} {position_carre[i][2]} C {val} I {count+i+1}\n")
            data_map_indices.write(f"F_t {i+1}/{sommet}/{i+2}\n")
        sommet +=1

        count += 1

        """
        
        # on divise en 4
        for i in range(1, 8, 1):
            

            data_map_data.write(f"P {position_carre[i][0]} {position_carre[i][1]} {position_carre[i][2]} C {val} I {0}\n")
            data_map_data.write(f"P {position_carre[8][0]} {position_carre[8][1]} {position_carre[8][2]} C {val} I {0}\n")
            data_map_data.write(f"P {position_carre[i+1][0]} {position_carre[i+1][1]} {position_carre[i+1][2]} C {val} I {0}\n")

            # triangle 1
            #data_map.write(f"{x + halfx} {world[x][y]} {y + halfy}\n") # pt 1
            #data_map.write(f"{x + halfx} {world[x][y]} {y - halfy}\n") # pt 2
            #data_map.write(f"{x - halfx} {world[x][y]} {y - halfy}\n") # pt 3

            # triangle 2
            #data_map.write(f"{x + halfx} {world[x][y]} {y + halfy}\n") # pt 1
            #data_map.write(f"{x - halfx} {world[x][y]} {y - halfy}\n") # pt 3
            #data_map.write(f"{x - halfx} {world[x][y]} {y + halfy}\n") # pt 4

        


"""
ligne_x = np.linspace(-1, 1, PIXELS[0], endpoint=False)
ligne_y = np.linspace(-1, 1, PIXELS[1], endpoint=False)
matx,maty = np.meshgrid(ligne_x, ligne_y)

image.save(image_path)
#gray_scale.save(gray_scale_path)
"""
data_map_data.close()
#data_map_indices.close()

# affichage de la map
"""
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(matx,maty, world, cmap='terrain')
matplotlib.pyplot.show()
"""