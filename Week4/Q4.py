class teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def work(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}"
class doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def work(self):
        return f"Doctor Name: {self.name}, Specialization: {self.specialization}" 
teacher1 = teacher("Alice", "Mathematics")
doctor1 = doctor("Dr. Bob", "Cardiology")
professions = [teacher1, doctor1]
for person in professions:
        print(person.work())  