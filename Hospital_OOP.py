class person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
class patient(person):
    def __init__(self, id, first_name, last_name,birth_date):
        super().__init__(id, first_name, last_name)
        self.birth_date = birth_date

    def get_info(self):
        return self.id,self.first_name,self.last_name,self.birth_date

class doctor(person):
    def __init__(self, id, first_name, last_name,specialty):
        super().__init__(id, first_name, last_name)
        self.specialty = specialty
class nurse(person): 
    def __init__(self, id, first_name, last_name,shift):
        super().__init__(id, first_name, last_name) 
        self.shift = shift
class appointment:
    def __init__(self,patient,doctor,date,time):
        self.patient=patient
        self.doctor=doctor
        self.date=date
        self.time=time
    def get_info(self):
        return (
            self.patient.first_name,
            self.patient.last_name,
            self.doctor.firs_name,
            self.doctor.last_name,
            self.date,
            self.time
        )


patient1=patient(1,"Aya","skaro","2006-01-12")   
doctor1=doctor(2,"j","smith","cardiology")
appointment1=appointment(
   patient1,
   doctor1,
   "2006-07-12",
   "10:30"

)

print(patient1.get_info())
  
 
