import math

def main():

    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x / y
    def squareroot(x):
        return math.sqrt(x)
    def PI(x):
        return math.pi * x
    def logs(x):
        return math.log(x)
    def coss(x):
        return math.cos(x)
    def sins(x):
        return math.sin(x)
    
    print("Thank you for using Project PI: A coding project made by @u.perceus_adalian")
    print("Operation Types:")
    print("[1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide, 5 = x*PI, 6 = Sqrt(x), 7 = log(x)")
    print("8 = cos(x), 9 = sin(x)], 10 = end")
    try:
        while True:
            response = int(input("Select an Operation Type: "))
            if response < 1 or response > 10:
                print("Invalid integer, please try again.")
                continue
            try: 
                if response == 10:
                        return
                if response in range(1,5):

                    x = int(input("Operand 1 = "))
                    y = int(input("Operant 2 = "))

                    if response == 1:
                        print(x,"+",y,"=",add(x,y))
                        continue
                    if response == 2:
                        print(x,"-",y,"=",subtract(x,y))
                        continue
                    if response == 3:
                        print(x,"*",y,"=",multiply(x,y))
                        continue
                    if response == 4:
                        print(x,"/",y,"=",divide(x,y))
                        continue
                else:
                    x = int(input("Operand x = "))
                    if response == 5:
                        print(x,"* PI =", PI(x))
                        continue
                    if response == 6:
                        print("The square root of",x, "=", squareroot(x))
                        continue
                    if response == 7:
                        print("The log(",x,") =",logs(x))
                        continue
                    if response == 8:
                        print("The cos(",x,") =",coss(x))
                        continue
                    if response == 9:
                        print("The sin(",x,") =",sins(x))
            except ValueError:
                print("Operand is a String. Please Try Again.")
                continue
    except ValueError:
        print("Operation Type is a String. Please Try Again.") 
main()