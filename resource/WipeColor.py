from flask_restful import Resource,reqparse
from utils.Controller import color_wipe

parser = reqparse.RequestParser()
parser.add_argument('red', required=True)
parser.add_argument('green', required=True)
parser.add_argument('blue', required=True)

class WipeColor(Resource):
    
    def post(self):
        args = parser.parse_args()
        color_wipe(args['red'], args['green'], args['blue'])

        return {'message': 'Wipe Color done'}