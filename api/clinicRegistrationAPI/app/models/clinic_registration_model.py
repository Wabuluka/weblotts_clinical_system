import json

class ClinicRegistration:

    def __init__(self, **kwargs):
        self.registrationId =  kwargs.get("registrationId")
        self.clinicName = kwargs.get("clinicName")

    def clinic_registration_to_dictionary(self):
        return {
            "registrationId" : self.registrationId,
            "clinicName" : self.clinicName
        }