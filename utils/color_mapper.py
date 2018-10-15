import json

data = {}

import os
cwd = os.getcwd()

print('Color Mapper' + cwd)


    

def getRGB(color, intensity=1):
    color = color.split()[0].strip().capitalize()
    with open('utils/colors.json') as f:
        data = json.load(f)
        if color in data.keys():
            copy = data[color]
            copy.update((x, int(y)*int(intensity)) for x, y in copy.items())
            return copy
        else:
            return data["Black"]