from flask_restful import Resource


class RouteTest(Resource):
    @staticmethod
    def get():
        return "test get request"
