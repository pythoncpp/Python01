# Hybrid inheritance

class Person:

    def __init__(self, name):
        self._name = name

    def print_person_details(self):
        print('name: ', self._name)


class Teacher(Person):

    def __init__(self, name, subject):
        Person.__init__(self, name)
        self._subject = subject

    def print_teacher_details(self):
        Person.print_person_details(self)
        print('subject: ', self._subject)


class LabAssistant(Person):

    def __init__(self, name, lab):
        Person.__init__(self, name)
        self._lab = lab

    def print_lab_assistant_details(self):
        Person.print_person_details(self)
        print('lab: ', self._lab)


class TeacherLabAssistant(Teacher, LabAssistant):

    def __init__(self, name, subject, lab, timing):
        Teacher.__init__(self, name, subject)
        LabAssistant.__init__(self, name, lab)
        self._timing = timing

    def print_tla_details(self):
        Teacher.print_teacher_details(self)
        LabAssistant.print_lab_assistant_details(self)
        print("timing: ", self._timing)


tla = TeacherLabAssistant('tla1', 'computer', 'computer', '11-1')
tla.print_tla_details()