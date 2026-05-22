from flask import Flask, render_template, request
import random

app = Flask(__name__)

points = 0
calculations = 0
num = random.randint(1, 10)
table = random.randint(2, 10)

@app.route("/", methods=["GET", "POST"])
def index():
    global points, calculations, num, table

    feedback = ""

    if request.method == "POST":
        answer = request.form.get("answer")

        try:
            answer = int(answer)
            correct = num * table

            if answer == correct:
                feedback = "correct"
                points += 1
            else:
                feedback = f"wrong, correct was {correct}"

        except:
            feedback = f"wrong, correct was {num * table}"

        calculations += 1
        num = random.randint(1, 10)

    return render_template(
        "index.html",
        num=num,
        table=table,
        points=points,
        calculations=calculations,
        feedback=feedback
    )

if __name__ == "__main__":
    app.run(debug=True)