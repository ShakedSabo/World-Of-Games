from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        score_file = open("Scores.txt", "r")
        score = score_file.read()
        print(score)
        return render_template("score.html", SCORE=score)
    except FileNotFoundError or FileExistsError:
        return render_template("error.html", ERROR='Unknown Error')


if __name__ == '__main__':
   app.run()

