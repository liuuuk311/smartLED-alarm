from flask import Flask
from flask_restful import Api

import sys
sys.path.append('../') 

from resource.Strip import StripColor, StripColorIncrease
from resource.WipeColor import WipeColor

app = Flask(__name__)
api = Api(app)

api.add_resource(StripColor, '/strip/color')
api.add_resource(StripColorIncrease, '/strip/increase/color')

api.add_resource(WipeColor, '/strip/wipe/color')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
