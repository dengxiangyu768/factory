from flask_restful import Resource
from flask import request
from models import Todo,Progress
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
    

class ProgressObject(Resource):
    def praseObject(self,data,Class):
        result = Class()
        result.__dict__ = data
        return result
        

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
        

        
        
    


        