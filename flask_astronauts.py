#importing flask
from flask import Flask, render_template, url_for
from signup import RegistrationForm, LoginForm

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#json of posts thatll go on the about.html page
posts = [
    {
        'author': 'John Uri',
        'title': 'NASA Astronaut Candidates',
        'content': "The term astronaut candidate refers to individuals who have been selected by NASA as candidates for the NASA astronaut corps and are currently undergoing a candidacy training program at the Johnson Space Center. The newest class of 2018 astronaut candidates were announced June 7, 2018.",
        'date_posted': 'June 16th, 2018'
    },
    {
        'author': 'Danielle Sempsrott',
        'title': 'Astronaut Selection and Training',
        'content': 'Following the preliminary screening of applications, a week-long process of personal interviews, medical screening, and orientation are required for both civilian and military applicants under final consideration. Once final selections have been made, all applicants are notified of the outcome. Selected applicants are designated Astronaut Candidates and are assigned to the Astronaut Office at the Johnson Space Center (JSC) in Houston, Texas. ',
        'date_posted': 'May 15th, 2011'
    }

]

#route to home page
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

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
