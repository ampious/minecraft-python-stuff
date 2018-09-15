from mcpi.minecraft import Minecraft
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--location", help="Enter a pre-defined location")
parser.add_argument("--coords", default='10,110,12', help="Coordinates in form 'x,y,z'")
#parser.add_argument("--y", help="Y-Coordinate")
#parser.add_argument("--x", help="Z-Coordinate")
args = parser.parse_args()        

mc = Minecraft.create()

curr_coords = mc.player.getPos()

if args.coords != '10,110,12':
    #coordinates = [int(n) for n in args.coords.split(',')]
    coordinates = [float(n) for n in args.coords.split(',')]
    #(int(x), int(y), int(z)) = args.coords.split(',')
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]
else:
    x = 10
    y = 110
    z = 12

mc.player.setTilePos(x, y, z)

