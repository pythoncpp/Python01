class Student:

    def __init__(self, name, college):
        self._name = name
        self._college = college

    def __str__(self):
        return "Student [name: {}, college: {}]".format(self._name, self._college)


def main():
    student = Student('student 1', 'college 1')
    print(student)


if __name__ == '__main__':
    main()