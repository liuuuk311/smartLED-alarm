from flask_restful import Resource, reqparse
from utils.Controller import increase, ping_pong, set_all

stripColorParser = reqparse.RequestParser()
stripColorParser.add_argument('red', type=int, required=True)
stripColorParser.add_argument('green', type=int, required=True)
stripColorParser.add_argument('blue', type=int, required=True)
stripColorParser.add_argument('density', type=float)
stripColorParser.add_argument('wait', type=float)

class StripColor(Resource):
    # Set a new color for all leds
    def post(self):
        args = stripColorParser.parse_args()
        set_all(args['red'], args['green'], args['blue'])

        return {'message': 'New color set'}


class StripColorIncrease(Resource):
    def post(self):
        args = stripColorParser.parse_args()

        increase(args['red'], args['green'], args['blue'])
        return {'message': 'Increased'}


class StripColorPingPong(Resource):
    def post(self):
        args = stripColorParser.parse_args()

        ping_pong(args['red'], args['green'], args['blue'])
        return {'message': 'Ping pong'}