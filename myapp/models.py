from flask_login import UserMixin
from .extensions import db, bcrypt

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    has_voted = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('vote', uselist=False))

class Candidate(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    gender      = db.Column(db.String(10),  nullable=False)
    bio         = db.Column(db.Text)
    image_url   = db.Column(db.String(250))

    def __repr__(self):
        return f'<Candidate {self.name}>' 
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'bio': self.bio,
            'image_url': self.image_url
        }

class VoteSelection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote_id = db.Column(db.Integer, db.ForeignKey('vote.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    position = db.Column(db.Integer, nullable=False)  # 1, 2, 3
    gender = db.Column(db.String(10), nullable=False)  # 'boy' or 'girl'

    vote = db.relationship('Vote', backref=db.backref('selections', lazy=True))
