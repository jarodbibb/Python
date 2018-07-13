import random

class Patient(object):
    def __init__(self,id, name, allergies):
        self.name = name
        self.id = id 
        self.allergies = allergies
        self.bed = "none"

class Hospital(object):
    def __init__(self, patients, hosp_name, capacity ):
        self.patients = [patients]
        self.hosp_name = hosp_name
        self.capacity = capacity
    def admit(self, pat):
        if len(self.patients) < self.capacity:
            pat.bed = random.randint(1, 101)
            self.patients.append(pat)

            print "confirmed patient added"
        else:
            print "full"
    def discharge(self, pat):
        pat.bed = "none"
        self.patients.remove(pat)
        return self
    def __repr__(self):
        return "<Hospital object {}, capacity {}>".format(self.hosp_name, self.capacity)

new_pat = Patient(8, "jarod", "hella")
new_pat1 = Patient(1, "arod", "hell")
new_pat2 = Patient(2, "rod", "hel")
new_pat3 = Patient(3, "od", "he")
kaiser = Hospital( new_pat, "Kaiser", 37)
kaiser.admit(new_pat1)
kaiser.admit(new_pat2)
kaiser.admit(new_pat3)
kaiser.discharge(new_pat3)


print "hosp_patients", new_pat3.bed

print "repr object testing ", kaiser







