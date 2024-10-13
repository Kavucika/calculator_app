from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            expression = request.form["display"]
            result = eval(expression)  # Evaluate the mathematical expression
        except:
            result = "Error"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
