from flask import Flask, render_template, url_for 
from flask_migrate import Migrate 



'''
#Application Factory.
The Factory Function: set up the  applications instance.
The __init__.py configures everything.
the application factory pattern.
take advantage of separating logic into different files.
'''

def create_app(): 
    #Create a Flask app instance
    app = Flask(__name__)

#Any config required here: custom logic.
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tundrass@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
 
    #Route on the app instance
    @app.route('/')
    def index():      #def hello():
        return 'Hello, PetFax!'

  # register pet blueprint 
      #Import the pet file:
    from . import pet
   
      #Call the register_blueprint method on the app instance,
      #and pass the pet blueprint into the method.
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app
    