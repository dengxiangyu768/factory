from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    todo = db.Column(db.String(1000),nullable=False)
    def to_dict(self):
        return {"id": self.id,
                "todo": self.todo}
    def save(self):
        db.session.add(self)
        db.session.commit()
        

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Progress(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    name = db.Column(db.String(100),nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    modify_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_dict(self):
        return {"id":self.id,"name": self.name,"create_time": self.create_time,"modify_time": self.modify_time}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()



# class User(db.Model):
    