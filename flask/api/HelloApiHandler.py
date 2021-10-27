import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
# flask .scafoold is added to deal with an wrror in flask_restful
from flask_restful import Api, Resource, reqparse

class HelloApihandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message':'Hello Api Handler'
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message',type=str)

        args= parser.parse_args()

        print(args)

        request_type = args['type']
        request_json = args['message']

        ret_status=request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your message requested: {}".format(ret_msg)
        else:
            message = "No msg"
        
        final_ret = {"status": "Success", "message": message}

        return final_ret