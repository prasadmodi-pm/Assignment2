__author__ = 'prasadmodi'
class Employee:
    def department(self):
        print("IT department")

class Developer(Employee):
    print("There are 10 developers")

class Tester(Employee):
    print("There are 5 Tester")

class QualityAnalyst(Employee):
    print("There are 2 QA")

if __name__ == '__main__':
    E1 = Employee()
    E1.department()
