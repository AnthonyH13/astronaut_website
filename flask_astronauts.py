#importing flask
from flask import Flask, render_template, url_for
from signup import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#json of posts thatll go on the about.html page
posts = [
    {
        'author': 'Unknown',
        'title': 'Moon Mission',
        'content': 'fafbdskfkjdshfjkhasdkjfhsdhf',
        'date_posted': 'June 1st, 2018'
    },
    {
        'author': 'Unknown',
        'title': 'Mars Mission',
        'content': 'fafbdskfkjdshfjkhasdkjfhsdhf',
        'date_posted': 'May 1st, 2019'
    }

]

#route to home page
@app.route("/home")
def home():
    return render_template("home.html", link="/Users/anthony/Desktop/astronaut_website/templates/signup.html")

#route to article page
@app.route("/about")
def about():
    return render_template("about.html", title='about', posts=posts)

#route to graphs page
@app.route("/analytics")
def analytics():
    return render_template("analytics.html", title='analytics')

#route to signup page
@app.route("/signup", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
