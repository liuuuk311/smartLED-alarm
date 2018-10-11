import json

data = {}

import os
cwd = os.getcwd()

print('Color Mapper' + cwd)

with open('utils/colors.json') as f:
    data = json.load(f)
    

def getRGB(color):
    color = color.split()[0].strip().capitalize()

    if color in data.keys():
        return data[color]
    else:
        return data["Black"]