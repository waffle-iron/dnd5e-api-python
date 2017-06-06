from dnd5eApi import db
from dnd5eApi.models.racial_languages import class_primary_ability

class Ability( db.Model ):
  __tablename__ = "ability"

  id = db.Column( db.Integer, primary_key = True )
  name = db.Column( db.String, nullable = False )
  description = db.Column( db.String, nullable = False )
  measures = db.Column( db.String, nullable = False )
  important_for = db.Column( db.String, nullable = False )
  classes = db.relationship( 'Class', secondary = class_primary_ability, backref = db.backref( 'ability', lazy = 'dynamic' ) )

  def __init__( self, name, description, measures, important_for ):
    self.name = name
    self.description = description
    self.measures = measures
    self.important_for = important_for

  def __repr__( self ):
    return "<Ability: {}>".format( self.name )