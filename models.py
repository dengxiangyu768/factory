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
    name = db.Column(db.Enum('冲压', '焊接', '涂装', '总装', '完成'))
   
    create_timestamp = db.Column(db.String(20), nullable=False)
    modify_timestamp = db.Column(db.String(20))
    product_id = db.Column(db.Integer,db.ForeignKey("product.id"))

    def to_dict(self):
        return {"id":self.id,"name": self.name,"create_timestamp": self.create_timestamp,"modify_timestamp": self.modify_timestamp}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    name = db.Column(db.String(100),nullable=False)

    create_timestamp = db.Column(db.String(20), nullable=False)
    completion_timestamp = db.Column(db.String(20))
    progress_id = db.relationship("Progress",backref="product",lazy="dynamic")


    def to_dict(self):
        return {"id":self.id,"name": self.name,"create_timestamp": self.create_timestamp,"modify_timestamp": self.modify_timestamp}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

# class User(db.Model):
    