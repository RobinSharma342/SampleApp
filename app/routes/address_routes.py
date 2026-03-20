from flask import Blueprint, render_template, request
from app.services.address_service import ADDRESSES, get_random_street_name

address_bp = Blueprint("address_bp", __name__) 

@address_bp.route("/address", methods=["GET", "POST"])
def address():
    address,selected_state = None, None
    states = ADDRESSES.keys()
    
    if request.method == 'POST':
        selected_state = request.form['state']
        address = get_random_street_name(selected_state)
        


    return render_template('address.html', address=address,
                           states=states,
                            selected_state=selected_state)
