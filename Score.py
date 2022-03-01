
def add_score(difficulty):
    POINTS_OF_WINNING = str((int(difficulty) * 3) + 5)
    try:
        score_file = open("Scores.txt", "r")
        old_score = score_file.read()
        score_file.close()
        score_file = open("Scores.txt", "w")
        new_score = int(old_score)+int(POINTS_OF_WINNING)
        print("old = "+old_score)
        print("new = "+str(new_score))
        score_file.write(str(new_score))
        score_file.close()
    except FileNotFoundError:
        score = open("Scores.txt", "x")
        score.write(POINTS_OF_WINNING)



