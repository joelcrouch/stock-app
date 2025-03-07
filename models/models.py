from app import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(150), unique=True, nullable=False)
    email=db.Column(db.String(150), unique=True, nullable=False)
    profile_picture=db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<USER {self.username}>'