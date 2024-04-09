from flask_restful import Resource
from flask import request
from models import Todo,Progress,Product
import time



class TodoObject(Resource):
    def get(self,id=None):
        if id:
            todo = Todo.query.get(id)
            if not todo:
                return {'error':'id not found'}, 404
            return Todo.to_dict(todo)
        else:
            todos = Todo.query.all()
            todos_list = [todo.to_dict() for todo in todos]
            return {'todos': todos_list}, 200
        

    def put(self,id):
        todo = Todo.query.filter_by(id=id).first()
        if todo is None:
            data = request.form['data']
            todo = Todo(todo=data)
            todo.save()
        return {"message": "add sucess"}
    
class ProductObject(Resource):

    def get(self,id=None):
        if id:
            product = Product.query.get(id)
            if not product:
                return {'error':'id not found'}, 404
            return product.to_dict()
        else:
            products = Product.query.all()
            product_list = [product.to_dict() for product in products]
            return {"products":product_list}
        
    def post(self):
        data = request.get_json()
        if data is None:
            return {"error": "no input data provided"},404
        product = product(name=data["name"],model_of_car=data["model_of_car"],
                          vin=data["vin"],eni=data["eni"],create_timestamp=int(time.time())
                          )
        product.save()
        return product.to_dict()
    
    def put(self,id):
        product = Product.query.get(id)
        if product is None:
            return {'error':'product id not found'},404
        data = request.get_json()
        new_product = product(name=data["name"],model_of_car=data["model_of_car"],
                          vin=data["vin"],eni=data["eni"])
        new_product.save()
        return new_product.to_dict()
        
        
    
class ProgressObject(Resource):
    def get(self,id=None):
        if id:
            progress = Progress.query.get(id)
            if not progress:
                return {'error':'id not found'}, 404
            return progress.to_dict()
    def post(self):
        data = request.get_json()
        print(data)
        if not data:
            return {"error": "no input data provided"},404
        progress = Progress(name=data["name"],create_timestamp=str(int(time.time())))
        progress.save()
        return progress.to_dict()
        

        
        
    


        