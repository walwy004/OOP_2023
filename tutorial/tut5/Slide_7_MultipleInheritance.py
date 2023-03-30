class Student:
    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        print("Student.__init__() was executed.")

    def printStudentInformation():
        print("<Student Information>")


class Staff:
    def __init__(self, staffID, position, salary):
        self.staffID = staffID
        self.position = position
        self.salary = salary
        print("Staff.__init__() was executed.")

    def printStaffInformation():
        print("<Staff Information>")


class PhDCandidate(Student, Staff):
    def __init__(self, studentID, name, staffID, position, salary, duration):
        Student.__init__(self, studentID, name)
        Staff.__init__(self, staffID, position, salary)
        self.duration = duration
        print("<PhDCandidate Information>")

    def printPhDCandidateInformation(self):
        super().printStudentInformation()
        super().printStaffInformation()


phdCandidate = PhDCandidate(
    110195632, "Ashe", 101172, "Lecturer", 1002500.0, 301.50)
