from flask import (Blueprint, render_template)

#Blueprint instance.
bp = Blueprint('fact', __name__, url_prefix="/facts")

#Define a route on the blueprint instance .
@bp.route('/new')     
def new():        

       return render_template('facts/new.html')
