__author__ = 'prasadmodi'
class Testing:
    def getString(self):
        jk = input("Please enter something")
        print(jk)

    def printStr(self):
        print("This is entered by user:")

class Bull(Testing):
    print("This is Bull")

if __name__ == '__main__':
    B = Bull()
    B.getString()
    B.printStr()
