# iterator

def function1():
    phones = ['iphone', 'galaxy s10', 'oneplus 7']

    # for phone in phones:
    #     print(phone)

    iterator = iter(phones)
    print(iterator)
    try:
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
        print('next: ', next(iterator))
    except StopIteration:
        print("end of the list")


# function1()


class School:

    def __init__(self, name, students):
        self._name = name
        self._students = students
        self._index = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        else:
            raise StopIteration()

    def print_students(self):
        for student in self._students:
            print(student)


school_1 = School('school 1', ['student 1', 'student 2', 'student 3', 'student 4'])
# school_1.print_students()

# iter => school_1.__iter__()
school_iterator = iter(school_1)
print(school_iterator)

# next => school_iterator.__next__()
# try:
#     print('student: ', next(school_iterator))
#     print('student: ', next(school_iterator))
#     print('student: ', next(school_iterator))
#     print('student: ', next(school_iterator))
#     print('student: ', next(school_iterator))
#     print('student: ', next(school_iterator))
#     print('student: ', next(school_iterator))
# except StopIteration:
#     print("end of list")


for student in school_1:
    print(student)


















