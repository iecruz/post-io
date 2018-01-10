from flask import Blueprint, render_template, url_for
from core.models import *

app = Blueprint('posts', __name__)

@app.route('/')
def index():
    return render_template('index.html', posts = Post.select().order_by(Post.date.desc()))
