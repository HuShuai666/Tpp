from app.home.views import home
from  app.user.views import user
from flask import Blueprint
def register_blue(app):
    app.register_blueprint(user,url_prefix='/user')
    app.register_blueprint(home, url_prefix='/home')