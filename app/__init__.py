from flask import Flask
from flask_restful import Api
from views.views import TodoSimple


app = Flask(__name__)
api = Api(app)
api.add_resource(TodoSimple, '/<string:todo_id>')

# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///project.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app) 

# with app.app_context():
#     db.create_all()