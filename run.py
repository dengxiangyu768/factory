from flask import Flask
from flask_restful import Api
from models import db
from config import Config

from views import TodoObject

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()


api = Api(app)
api.add_resource(TodoObject,'/api/v2/todos','/api/v2/todo/<int:id>')


if __name__ == '__main__':

    app.run(debug=True)