def log_attendance(category, student_name):
    with open("attendance.txt", "a") as file:
        file.write(category + student_name + "\n")

def check_attendance(category, student_name):
    log = category + student_name
    count = 0
    with open("attendance.txt", "r") as file:
        for entry in file:
            if entry.rstrip("\n") == log:
                count = count + 1
    print(f"{student_name} was marked {category}{count} time/s.")

L = "Late: "
A = "Absent: "
P = "Present: "

def option(category, student_name):
    choice = str(input("(C)heck attendance or (L)og attendance: ").upper())
    if choice == "C":
        check_attendance(category, student_name)
    elif choice == "L":
        log_attendance(category, student_name)

option(L, "Elliot")
