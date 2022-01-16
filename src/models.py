from src.app import db

class Enterprise(db.Model):
    __tablename__ = 'Enterprise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    nps = db.Column(db.Integer())
    question_1 = db.Column(db.Boolean())
    question_2 = db.Column(db.Boolean())
    question_3 = db.Column(db.Boolean())
    question_4 = db.Column(db.Boolean())
    question_5 = db.Column(db.Boolean())
    question_6 = db.Column(db.Boolean())
    question_7 = db.Column(db.Boolean())
    question_8 = db.Column(db.Boolean())
    question_9 = db.Column(db.Boolean())
    question_10 = db.Column(db.Boolean())
    question_11 = db.Column(db.Boolean())
    question_12 = db.Column(db.Boolean())
    question_13 = db.Column(db.Boolean())
    question_14 = db.Column(db.Boolean())
    question_15 = db.Column(db.Boolean())
    constant_factor = db.Column(db.Boolean())

    def __init__(self, name, author, published):
        self.name = name
        self.nps = nps
        self.constant_factor = constant_factor
        self.question_1 = question_1
        self.question_2 = question_1
        self.question_3 = question_1
        self.question_4 = question_1
        self.question_5 = question_1
        self.question_6 = question_1
        self.question_7 = question_1
        self.question_8 = question_1
        self.question_9 = question_1
        self.question_10 = question_1
        self.question_11 = question_1
        self.question_12 = question_1
        self.question_13 = question_1
        self.question_14 = question_1
        self.question_15 = question_1

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'nps': self.nps,
            'constant_factor':self.constant_factor,
            'question_1': self.question_1,
            'question_2': self.question_1,
            'question_3': self.question_1,
            'question_4': self.question_1,
            'question_5': self.question_1,
            'question_6': self.question_1,
            'question_7': self.question_1,
            'question_8': self.question_1,
            'question_9': self.question_1,
            'question_10': self.question_1,
            'question_11': self.question_1,
            'question_12': self.question_1,
            'question_13': self.question_1,
            'question_14': self.question_1,
            'question_15': self.question_1,
        }