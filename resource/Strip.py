from flask_restful import Resource, reqparse
from utils.Controller import increase

stripColorParser = reqparse.RequestParser()
stripColorParser.add_argument('red', type=int, required=True)
stripColorParser.add_argument('green', type=int, required=True)
stripColorParser.add_argument('blue', type=int, required=True)
stripColorParser.add_argument('density', type=float)

class StripColor(Resource):
    # Set a new color for all leds
    def post(self):
        args = stripColorParser.parse_args()
        # set_color_to_all(args['red'], args['green'], args['blue'])

        return {'message': 'New color set'}


class StripColorIncrease(Resource):
    def post(self):
        args = stripColorParser.parse_args()

        increase(args['red'], args['green'], args['blue'])
        return {'message': 'Increased'}
