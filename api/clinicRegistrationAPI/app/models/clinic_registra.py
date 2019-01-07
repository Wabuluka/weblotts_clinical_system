import json
"""
    In this model:
        the person registering a clinic details are collected
        
"""
class ClinicRegistra:

    def __init__(self, **kwargs):
        self.registraId = kwargs.get("registraId")
        self.firstName = kwargs.get("firstName")
        self.lastName = kwargs.get("lastName")
        self.gender = kwargs.get("gender")
        self.email = kwargs.get("email")
        self.telephone = kwargs.get("telephone")
        
    def registra_details_to_dictionary(self):
        return {
            "registraId" : self.registraId,
            "firstname" : self.firstName,
            "lastname" : self.lastName,
            "gender" : self.gender,
            "email" : self.email,
            "telephone" : self.telephone
        }

   