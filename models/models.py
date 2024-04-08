from app import db

class TodoSimpleModel(db.Model):
    __tablename__= 'todosimple' 

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, unique=True, nullable=False)
    
    
    def _repr_(self):
        return '<TodoSimple %r>' % self.message