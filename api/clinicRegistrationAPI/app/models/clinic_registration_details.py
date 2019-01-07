import json

class ClinicRegistrationDetails:

    def __init__(self, **kwargs):
        self.clinicDetailsId = kwargs.get("clinicDetailsId")
        self.govNumber = kwargs.get("govNumber")
        self.regionOfOperation = kwargs.get("regionOfOperation")

    def clinic_registration_details_to_dictionary(self):
        return {
            "clinicDateId" : self.clinicDetailsId,
            "govNumber" : self.govNumber,
            "regionOfOperation": self.regionOfOperation
        }