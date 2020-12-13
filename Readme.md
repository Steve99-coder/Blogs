# BLOGS

## Author
 Stephen Nderitu

## Description
This is a personal blogging website where you can create and share your opinions and other users can read and comment on them,view the blog posts on the site,see random quotes on the site,create a blog from the application.
There is also an option for one to subscribe and receive updates.

## Behaviour Driven Development

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Sign Up| **Enter Username**,**Enter Email Address** and **Password** | Redirect to login page|
| Log in | **Username** and **password** | Log on to main page with blogs and functionality for adding blogs|
| Comment | **Comment** | Input your comment form|
| On Submit  |  | Redirect to All comments section page|
|Subscription | **Email Address**| Shows "Subscribed successfully to Steve's blogs"|

## User Story

As a user you

* view the most recent posts.
* View and comment the blog posts on the site.
* Receive an email alert after subscribing then you get posted on the blogs If added.
* Sign up then log in access various features
* View random quotes on the site
* Create a blog,update it or delete blogs created.


## Development Installation

* Git clone my repo
  ```bash
  https://github.com/steve99-coder/Blogs.git
  ```
* Use Visual Studio Code or Editor of your choice and install the requirements to run the applicaton
  ```bash
  pip install -r requirements.txt
  ```
* Export your configurations and replace the username and password with your database
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
* Run the application with the command below
  ```bash
  python3 manage.py runserver
  ```
* Test the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.

## Technologies Used
- Python3.8

- PIP

- Flask

- Heroku

## Contact Info
For any assistance or suggestions reach me on stevenderitu99@gmail.com

## License 
[MIT](https://github.com/Steve99-coder/Blogs/blob/master/LICENSE.md)

 © [Stephen Nderitu](https://github.com/steve99-coder)


