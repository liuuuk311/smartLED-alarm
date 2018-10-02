from flask_restful import Resource, reqparse
from utils.Controller import set_color_to_all

stripColorParser = reqparse.RequestParser()
stripColorParser.add_argument('red', required=True)
stripColorParser.add_argument('green', required=True)
stripColorParser.add_argument('blue', required=True)

class StripColor(Resource):
    
    # Set a new color for all leds
    def post(self):
        args = stripColorParser.parse_args()
        set_color_to_all(args['red'], args['green'], args['blue'])

        return {'message': 'New color set'}

stripClearParser = reqparse.RequestParser()
stripClearParser.add_argument('wipe')

class StripClear(Resource):
    def get(self):
        args = stripClearParser.parse_args()
        print(args)
        return {'message': 'Strip clear'}