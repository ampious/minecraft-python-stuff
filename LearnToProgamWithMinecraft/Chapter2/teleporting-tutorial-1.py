from mcpi.minecraft import Minecraft
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--location", help="Enter a pre-defined location", choices = ['guest', 'oped'])
parser.add_argument("--coords", default='10,110,12', help="Coordinates in form 'x,y,z'")
parser.add_argument("--player", help="Set name of player to execute commands onto NOT IMPLEMENTED")
parser.add_argument("--getpos", help="Get coordinates of selected player")
args = parser.parse_args()        

locations = {}
locations['spawn_points'] = {}
locations['spawn_points']['guest'] = [998,2,952]
locations['spawn_points']['oped'] = [20,5,6]

mc = Minecraft.create()

curr_coords = mc.player.getPos()

if args.coords != '10,110,12':
    coordinates = [float(n) for n in args.coords.split(',')]
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]
elif args.location:
    if args.location == 'guest':
        x = locations['spawn_points']['guest'][0]
        y = locations['spawn_points']['guest'][1]
        z = locations['spawn_points']['guest'][2]
    elif args.location == 'oped':
        x = locations['spawn_points']['oped'][0]
        y = locations['spawn_points']['oped'][1]
        z = locations['spawn_points']['oped'][2]
else:
    x = 10
    y = 110
    z = 12

mc.player.setTilePos(x, y, z)

