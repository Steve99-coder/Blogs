from flask import render_template,redirect,url_for,abort,request,flash
from app.requests import get_quotes
from app.main import main
from app.models import User,Blog,Comment,Subscriber
from PIL import Image
import os
import secrets
from flask_login import login_required,current_user
from .. import db
from .forms import UpdateProfile,CreateBlog
from ..email import mail_message

@main.route('/')
def index():
    quotes = get_quotes()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page, per_page = 3)
    title = 'This is your blog web app'
    
    return render_template('index.html', title = title,blogs=blogs,quote=quotes)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join('app/static/photos', picture_filename)
    
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename

@main.route('/profile',methods = ['POST','GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Profile updated successfully')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename = 'photos/'+ current_user.profile_pic_path) 
    return render_template('profile/profile.html', profile_pic_path=profile_pic_path, form = form)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)

@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_blog():
    subscribers = Subscriber.query.all()
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object().id
        blog = Blog(title=title,content=content,user_id=user_id)
        blog.save()
        for subscriber in subscribers:
            mail_message("Alert New Blog","email/new_blog",subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
        flash('New Blog Posted')
    return render_template('newblog.html', form = form)

@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    blog = Blog.query.get(id)
    return render_template('blog.html',blog=blog,comments=comments)

@main.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first()
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.filter_by(user=user).order_by(Blog.posted.desc()).paginate(page = page, per_page = 4)
    return render_template('userposts.html',blogs=blogs,user = user)

@main.route('/comment/<blog_id>', methods = ['Post','GET'])
@login_required
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment =request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save()
    return redirect(url_for('main.blog',id = blog.id))

@main.route('/blog/<blog_id>/delete', methods = ['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("Blog deleted successfully!")
    return redirect(url_for('main.index'))

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed successfully to Steve's blogs","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Subscribed successfully to Steve\'s blogs')
    return redirect(url_for('main.index'))


@main.route('/blog/<blog_id>/update', methods = ['GET','POST'])
@login_required
def updateblog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    form = CreateBlog()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash("Blog updated!")
        return redirect(url_for('main.blog',id = blog.id)) 
    if request.method == 'GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('newblog.html', form = form)

