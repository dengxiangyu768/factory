from flask_restful import Resource
from flask import request
from models import Todo



class TodoObject(Resource):
    def get(self,id=None):
        if id:
            todo = Todo.query.get(id)
            if not todo:
                return {'error':'id not found'}, 404
            return Todo.to_dict(todo), 200
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
    


        