from flask import Blueprint, render_template, request
from app.services.request_service import get_service_request, requests

request_bp = Blueprint("request_bp", __name__) 

@request_bp.route("/request", methods=["GET", "POST"])
def get_request():
    selected_request_type, request_template = None, None

    request_types = requests
    
    
    if request.method == 'POST':
        selected_request_type = request.form['request_type']
        request_template = get_service_request(selected_request_type)
        


    return render_template('request.html', 
                           request_types=request_types,
                           selected_request_type=selected_request_type, 
                           request_template=request_template)
