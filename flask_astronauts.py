from flask import Flask, render_template, url_for

app = Flask(__name__)
link = '/Users/anthony/Desktop/astronaut_website/templates/signup.html'
@app.route("/home")
def home():
    return render_template("home.html", link="/Users/anthony/Desktop/astronaut_website/templates/signup.html")

@app.route("/about")
def about():
    return render_template("about.html", title='about')

@app.route("/analytics")
def analytics():
    return render_template("analytics.html", title='analytics')


@app.route("/signup")
def signup():
    return render_template("signup.html", title='signup')

if __name__ == '__main__':
    app.run(debug=True)
