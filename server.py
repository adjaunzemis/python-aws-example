from flask import Flask, request
from flask_restx import Resource, Api, Namespace
from marshmallow import Schema, fields
from marshmallow.validate import Length

from dataclasses import dataclass

@dataclass
class Profit():
    name: str
    amount: float = 0.0
    
class ProfitSchema(Schema):
    name = fields.String(required=True, validate=Length(max=10))
    amount = fields.Float(required=False, default=0.0, missing=0.0)

profitAPI = Namespace("Profit Machine", description="A profit making machine")

profitsSchema = ProfitSchema(many=True)
profitSchema = ProfitSchema()
@profitAPI.route("/")
class ProfitResource(Resource):
    def get(self):
        """
        Some documentation for ProfitResource get function goes here.
        """
        errors = profitSchema.validate(request.args)
        if errors:
            return { 'errors': str(errors) }, 400
        values = profitSchema.load(request.args)
        return { 'data': profitSchema.dump(Profit(name=values['name'], amount=values['amount'])) }, 200
     
app = Flask(__name__)

mainAPI = Api(
    app = app,
    title = "Test API",
    version = "1.0.0",
    description = "A super cool test API, complete with dope auto-documentation!"
)
mainAPI.add_namespace(profitAPI, path="/api/profit")

@app.route("/andris")
def hello_andris():
    return "Hello Andris, we've been waiting for you..."

if __name__ == "__main__":
    app.run(debug=True)
