def log_highscore(score, username):
    try:
        with open("highscore.txt", "r") as file:
            current_high = file.readline()
            old_score = int(current_high.split("|")[0].strip())
        if score > old_score:
            with open("highscore.txt", "w") as file:
                file.write(f"{score} | {username}")
    except:
        with open("highscore.txt", "w") as file:
            file.write("0 | None")

def game(username):
    score = 0
    return score, username

log_highscore(*game("Meow"))
