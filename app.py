from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Prodcuts")
def products():
    return "This is the product pages."


@app.route("/")
def hello_world():
    return render_template('index.html')



if __name__ == "__main__":
  app.run(debug=True, port=8000)