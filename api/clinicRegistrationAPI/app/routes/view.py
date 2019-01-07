from app.controller.clinic_registra_view import ClinicRegistraView
from app import app

route_url = ClinicRegistraView.as_view('route_url')
app.add_url_rule('/api/v1/registra', view_func=route_url, methods=['POST',])