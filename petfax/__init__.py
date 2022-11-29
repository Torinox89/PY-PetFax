from flask import Flask, render_template, url_for 

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
    
    #Route on the app instance
    @app.route('/')
    def hello(): 
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