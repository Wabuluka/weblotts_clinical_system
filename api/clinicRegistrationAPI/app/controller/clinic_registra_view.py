from flask import Flask, jsonify, request, json
from flask.views import MethodView

from app.models.clinic_registra import ClinicRegistra


registras = []

class ClinicRegistraView(MethodView):
    
    def post(self):
        data = request.get_json()
       
    
        registra = ClinicRegistra(
            registraId = data['registraId'],
            firstName = data['firstName'],
            lastName = data['lastName'],
            gender = data['gender'],
            email = data['email'],
            telephone =data['telephone'])

        registras.append(registra)
        return jsonify({"data" : registra.registra_details_to_dictionary()})

   