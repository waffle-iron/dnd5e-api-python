from dnd5eApi import db
#from dnd5eApi.models.racial_languages import racial_languages

class Feats( db.Model ):
  __tablename__ = "feats"

  id = db.Column( db.Integer, primary_key = True )
  name = db.Column( db.String, nullable = False )
  description = db.Column( db.String, nullable = False )
  requirements = db.Column( db.String, nullable = False )
  bonuses = db.Column( db.String, nullable = False )
  #races = db.relationship( 'Race', secondary = racial_languages, backref = db.backref( 'language', lazy = 'dynamic' ) )

  def __init__( self, name, description, requirements, bonuses ):
    self.name = name
    self.description = description
    self.requirements = requirements
    self.bonuses = bonuses

  def __repr__( self ):
    return "<Feats: {}>".format( self.name )
