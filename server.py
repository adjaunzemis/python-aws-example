from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app=app)

@api.route('/api/profit')
class Profit(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('person', type=str, default=None, required=True, help='Person to profit')
        parser.add_argument('amount', type=float, default=0, required=False, help='Profit amount')
        args = parser.parse_args()

        return f"{args['person']} profits ${args['amount']:.2f}, hooray!"

@app.route('/andris')
def hello_andris():
    return 'Hello Andris, we\'ve been waiting for you...'

@app.route('/alex')
def hello_alex():
    return 'Hello Alex, we\'ve been waiting for you...'

@app.route('/wes')
def hello_wes():
    return 'Hello Wes, we\'ve been waiting for you...'

if __name__ == "__main__":
    app.run(debug=True)
