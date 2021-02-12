from flask import Flask
from flask_restful import Api
# from flask_cors import CORS

from resources.ocr import OCR
from resources.routeTest import RouteTest

app = Flask(__name__)
# CORS(app)
api = Api(app)

api.add_resource(OCR, '/ocr', '/ocr/<string:id>')
api.add_resource(RouteTest, '/routeTest', '/routeTest/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
