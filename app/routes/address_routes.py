from flask import Blueprint, render_template, request
from app.services.address_service import get_random_street_name

address_bp = Blueprint("address_bp", __name__) 

@address_bp.route("/address", methods=["GET", "POST"])
def address():
    address = None
    
    if request.method == 'POST':
        address = get_random_street_name(request.form['state'])
        


    return render_template('address.html', address=address)
