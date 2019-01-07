import json

class ClinicRegistrationDate:

    def __init__(self, **kwargs):
        self.dateId = kwargs.get("dateId")
        self.timeOfRegistration = kwargs.get("timeOfRegistration")
        self.dateOfRegistration = kwargs.get("dateOfRegistration")

    def clinic_registration_date_details(self):
        return {
            "dateId" : self.dateId,
            "timeOfRegistration": self.timeOfRegistration,
            "dateOfRegistration": self.dateOfRegistration
        }