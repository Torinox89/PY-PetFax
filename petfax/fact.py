from flask import (Blueprint, render_template, request, redirect)
from . import models
#Blueprint instance.
bp = Blueprint('fact', __name__, url_prefix="/facts")

#POSTing to /facts
#the conventional endpoint to use for posting to a particular blueprint should be its base
@bp.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':          #IF statements to properly handle each separate method
        submitter = request.form['submitter']
        fact = request.form['fact']
        print(request.form)
        new_fact = models.Fact(submitter=submitter,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')        

    results = models.Fact.query.all()
                                             
    return render_template('facts/index.html', facts=results)  


#Factts New route
#Define a route on the blueprint instance .
@bp.route('/new')     
def new():        

       return render_template('facts/new.html')



