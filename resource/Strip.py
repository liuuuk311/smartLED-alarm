from flask_restful import Resource, reqparse
from utils.Controller import color_wipe, set_all

from utils.color_mapper import getRGB

myParser = reqparse.RequestParser()
myParser.add_argument('color', type=str)
myParser.add_argument('intensity', type=int)

class StripColor(Resource):
    # Set a new color for all leds

    def post(self):
        args = myParser.parse_args()
        
        rgb_val = getRGB(args['color'])
        set_all(rgb_val['R'], rgb_val['G'], rgb_val['B'])

        return {'message': rgb_val}


class StripColorIncrease(Resource):
    def post(self):
        args = myParser.parse_args()

        rgb_val = getRGB(args['color'], intensity=int(args['intensity']))
        density_val = float(args['intensity'])/10

        set_all(0,0,0) # Clean
        set_all(rgb_val['R'], rgb_val['G'], rgb_val['B'], density=density_val, animation=True, animation_speed=25)

        return {'message': rgb_val}