from flask import Flask
from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort
import marshmallow as ma

from dataclasses import dataclass

@dataclass
class Profit:
    id: int
    name: str
    amount: float
    
class ProfitSchema(ma.Schema):
    id = ma.fields.Integer()
    name = ma.fields.String()
    amount = ma.fields.Float()

class ProfitQueryArgsSchema(ma.Schema):
    name = ma.fields.String()
    amount = ma.fields.Float()

blp = Blueprint(
    "profits", "profits", url_prefix="/profits", description="Operations on profits"
)

@blp.route("/")
class Profits(MethodView):

    @blp.arguments(ProfitQueryArgsSchema, location="query")
    @blp.response(200, ProfitSchema)
    def get(self, args):
        """ Profit amount for a specific person """
        return Profit(1, "AJ", 123.456)

class Config:
    API_TITLE = "Test API"
    API_VERSION = "1.0.0"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = '/doc'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_VERSION = '3.24.2'
# app.config['API_DESCRIPTION'] = "A super cool test API, complete with dope auto-documentation!"
    
app = Flask(__name__)
app.config.from_object(Config)

api = Api(app = app)

api.register_blueprint(blp)

# @app.route("/andris")
# def hello_andris():
#     return "Hello Andris, we've been waiting for you..."

if __name__ == "__main__":
    app.run(debug=True)
