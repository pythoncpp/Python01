# Multiple inheritance

class Teacher:

    def __init__(self, name, subject):
        self._name = name
        self._subject = subject

    def print_teacher_details(self):
        print('name: ', self._name)
        print('subject: ', self._subject)


class LabAssistant:

    def __init__(self, name, lab):
        self._name = name
        self._lab = lab

    def print_lab_assistant_details(self):
        print('name: ', self._name)
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