import os
from flask import Flask, render_template, request, session, redirect

from game_logic import (
    multiplication_question,
    addition_question,
    subtraction_question,
    division_question
)

app = Flask(__name__)
app.secret_key = "secret-key"


def generate_question():
    game_type = session["game_type"]
    value = session["value"]

    if game_type == "multiplication":
        return multiplication_question(value)
    elif game_type == "addition":
        return addition_question(value)
    elif game_type == "subtraction":
        return subtraction_question(value)
    elif game_type == "division":
        return division_question(value)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST" and "start_game" in request.form:

        session["game_type"] = request.form["game_type"]
        session["value"] = int(request.form["value"])

        session["score"] = 0
        session["round"] = 1

        session["question_data"] = generate_question()

        return redirect("/")

    if request.method == "POST" and "answer" in request.form:

        try:
            answer = int(request.form["answer"])

            if answer == session["question_data"]["answer"]:
                session["score"] += 1
        except:
            pass

        session["round"] += 1

        if session["round"] > 10:
            final_score = session["score"]
            session.clear()
            return render_template("index.html", finished=True, score=final_score)

        session["question_data"] = generate_question()

        return redirect("/")

    return render_template(
        "index.html",
        question_data=session.get("question_data"),
        score=session.get("score", 0),
        round=session.get("round", 0),
        finished=False,
        game_type=session.get("game_type")
    )


# 🔥 ONLY NEW ADDITION
@app.route("/quit", methods=["POST"])
def quit_game():
    session.clear()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/ads.txt")
def ads_txt():
    return app.send_static_file("ads.txt")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)