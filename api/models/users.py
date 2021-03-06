from ..utils import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(45),nullable=False)
    email = db.Column(db.String(45),nullable=False,unique=True)
    password = db.Column(db.String(45),nullable=True)
    is_staff = db.Column(db.Boolean(),default=False)
    is_active = db.Column(db.Boolean(),default=False)
    orders = db.relationship('Order',backref='users.id')
    def __repr__(self):
        return f"{self.username}"