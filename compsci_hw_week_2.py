scores = []

def getMax():
    global max_score
    max_score = scores[0]
    for num in range(0, len(scores)):
        if scores[num] > max_score:
            max_score = scores[num]

def getMin():
    global min_score
    min_score = scores[0]
    for num in range(0, len(scores)):
        if scores[num] < min_score:
            min_score = scores[num]

def getRange():
    getMin()
    getMax()
    return max_score - min_score

def getSum():
    sum = 0
    for number in scores:
        sum += number
    return sum

def getMean():
    sum = 0
    for number in scores:
        sum += number
    mean = sum / len(scores)
    return mean

def getMode():
    highest_count = 0
    for score in scores:
        count = 0
        for duplicate in scores:
            if score == duplicate:
                count += 1
            if count > highest_count:
                highest_count = count
                mode = score
    return mode

def studentScores():
    try:
        score = int(input("Input student score: "))
        scores.append(score)
        choice()
    except ValueError:
        print("Input a numerical value")
        studentScores()

def choice():
    choice = input("(A)dd new score or (E)nd: ").strip().upper()
    if choice == "A":
        studentScores()
    elif choice == "E":
        dataChoice()
    else:
        print("Input a valid choice")
        choice()

def dataChoice():
    choice = input("Find max, min, range, sum, mean, or mode: ").strip().lower()
    if choice == "max":
        getMax()
        print(max_score)
    elif choice == "min":
        getMin()
        print(min_score)
    elif choice == "range":
        print(getRange())
    elif choice == "sum":
        print(getSum())
    elif choice == "mean":
        print(getMean())
    elif choice == "mode":
        print(getMode())
    else:
        print("Input a valid choice")
        dataChoice()

print("Welcome!")
studentScores()
