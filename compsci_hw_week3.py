import math

def angle_or_length():
    choice = input("Press A to find an angle, press L to find a length: ").strip().upper()
    if choice == "A":
        angle()
    elif choice == "L":
        length()
    else:
        print("Invalid input")
        angle_or_length()

def angle():
    choice = input("Press S to find the sine, C to find the cosine, or T to find the tangent: ").strip().upper()
    if choice == "S":
        value = f_sine()
        print(f"The angle is: {value}")
    elif choice == "C":
        value = f_cosine()
        print(f"The angle is: {value}")
    elif choice == "T":
        value = f_tangent()
        print(f"The angle is: {value}")
    else:
        print("Invalid input")
        angle()

def f_sine():
    opp = float(input("Enter the opposite: "))
    hyp = float(input("Enter the hypotneuse: "))
    return math.degrees(math.asin(opp / hyp))

def f_cosine():
    adj = float(input("Enter the adjacent: "))
    hyp = float(input("Enter the hypotneuse: "))
    return math.degrees(math.acos(adj / hyp))

def f_tangent():
    opp = float(input("Enter the opposite: "))
    adj = float(input("Enter the adjacent: "))
    return math.degrees(math.atan(opp / adj))

def length():
    choice = input("Press H to find the hypotneuse, O to find the opposite, or A to find the adjacent: ").strip().upper()
    if choice == "H":
        value = f_hypotneuse()
        print(f"The hypotneuse is {value}: ")
    elif choice == "O":
        value = f_opposite()
        print(f"The opposite is {value}: ")
    elif choice == "A":
        value = f_adjacent()
        print(f"The adjacent is {value}: ")

def f_hypotneuse():
    adj = float(input("Input the length of the adjacent: "))
    opp = float(input("Input the length of the opposite: "))
    return math.sqrt(adj * adj + opp * opp )

def f_opposite():
    hyp = float(input("Input the length of the hypotneuse"))
    adj = float(input("Input the length of the adjacent"))
    return math.sqrt(hyp * hyp - adj * adj)

def f_adjacent():
    hyp = float(input("Input the length of the hypotneuse"))
    opp = float(input("Input the length of the opposite"))
    return math.sqrt(hyp * hyp - opp * opp)

def start():
    angle_or_length()

start()
