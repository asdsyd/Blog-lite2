import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from bloglite import app, db, bcrypt, mail
from bloglite.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                            PostForm, RequestResetForm, ResetPasswordForm)
from bloglite.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message













# # SEARCH PAGE
# @app.route("/search-user")

# # USER'S LIST OF FOLLOWERS PAGE
# @app.route("/user/followers")
#
# # USER'S LIST OF FOLLOWING PAGE
# @app.route("/user/following")
