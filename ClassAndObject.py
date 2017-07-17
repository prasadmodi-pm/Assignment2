__author__ = 'prasadmodi'
class car:
    def wheels(self):
        print("There are four wheels")

    def petrol(self):
        print("Car uses petrol")

    def disesl(self):
        print("Car uses diesel")

if __name__ == '__main__':
    c1 = car()
    c1.wheels()
    c1.petrol()
    c2 = car()
    c2.wheels()
    c2.disesl()