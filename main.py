from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '11cbef399d872e8001d3aa2a92a34c16'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=True, nullable=False)

posts = [
    {
        'author': 'Asad sayeed',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'December 29, 2022'
    },
    {
        'author': 'Jane sayeed',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'December 30, 2022'
    }
]


# HOME PAGE OF WEBSITE
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
# # USER PROFILE PAGE
# @app.route("/user")
#

# # SIGN UP PAGE
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',
                           form=form)

# # LOGIN PAGE
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'asad@blog.com' and form.password.data == 'password':
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password','danger')
    return render_template('login.html', title='Login',
                           form=form)
# # SEARCH PAGE
# @app.route("/search-user")
#
# # POST BLOG PAGE
# @app.route("/post")
#
# # FEED PAGE
# @app.route("/myfeed")
#
# # USER'S LIST OF FOLLOWERS PAGE
# @app.route("/user/followers")
#
# # USER'S LIST OF FOLLOWING PAGE
# @app.route("/user/following")
