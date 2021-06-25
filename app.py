from flask import Flask
from flask_restx import Api, Resource
from common.init import init

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {"Hello": "world!"}


if __name__ == "__main__":
    init()
    app.run(debug=True, host="0.0.0.0", port=8080, use_reloader=False)
