from flask import Flask
from flask_restful import Api
from models import db
from config import Config

from views import TodoObject,ProgressObject,ProductObject

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()


api = Api(app)
api.add_resource(TodoObject,'/api/v2/todos','/api/v2/todo/<int:id>')
api.add_resource(ProgressObject,'/api/v2/progress','/api/v2/progress/<int:id>')
api.add_resource(ProductObject,'/api/v2/products','/api/v2/product','/api/v2/product/<int:id>')




if __name__ == '__main__':

    app.run(debug=True)