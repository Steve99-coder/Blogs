from app.requests import get_quotes
from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from app.models import User,Blog,Comment,Subscriber

@main.route('/')
def index():
    quotes = get_quotes()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page, per_page = 3)
    title = 'Welcome to blog app'
    
    return render_template('index.html', title = title,blogs=blogs,quote=quotes)