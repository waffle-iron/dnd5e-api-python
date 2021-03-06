from dnd5eApi import db
from dnd5eApi.models.racial_languages import racial_languages


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    script = db.Column(db.String)
    races = db.relationship('Race', secondary=racial_languages)

    def __init__(self, name, script):
        self.name = name
        self.script = script

    def __repr__(self):
        return "<Language: {}>".format(self.name)
