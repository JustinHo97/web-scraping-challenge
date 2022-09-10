from flask import Flask, render_template
from scrape_mars import scrape_mars

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    scrape = scrape_mars()
    return render_template("scrape.html", scrape = scrape)

if __name__ == "__main__":
    app.run()