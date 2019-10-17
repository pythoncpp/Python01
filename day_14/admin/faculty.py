class Faculty:

    def __init__(self, name, subject):
        self._name = name
        self._subject = subject

    def __str__(self):
        return "Faculty [name: {}, subject: {}]".format(self._name, self._subject)

