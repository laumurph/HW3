from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return render_template("blank_template.html")

@app.route("/favoritesnack")
def favorite_snack():
	return render_template("favoritesform.html")

@app.route("/favorite_judgement")
def judgement():
	fave_food = request.args.get("treat")
	return render_template("judgement.html", treat = fave_food)

if __name__ == '__main__':
    app.run(debug=True)