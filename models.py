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
    create_timestamp = db.Column(db.Integer, nullable=False)
    completion_timestamp = db.Column(db.Integer)
    duration = db.Column(db.Integer)
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
    model_of_car = db.Column(db.Enum('轻卡', '特种车', '救护车')) 
    vin = db.Column(db.String(30),nullable=False)
    eni= db.Column(db.String(30),nullable=False)
    create_timestamp = db.Column(db.Integer, nullable=False)
    completion_timestamp = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    status =  db.Column(db.Enum('生产中', '完成'))
    progress = db.relationship("Progress",backref="product",lazy="dynamic")


    def to_dict(self):
        return {"id":self.id,"name": self.name,"create_timestamp": self.create_timestamp,"modify_timestamp": self.modify_timestamp}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def create_all_progress(self):
        for element in ['冲压', '焊接', '涂装', '总装', '完成']:
            progress = Progress(name=element,product_id=self.id)
            db.sesion.add(progress)
            db.session.commit()
            

# class User(db.Model):
    