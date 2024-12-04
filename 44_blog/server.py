import smtplib
from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, request
from post import Post

load_dotenv()
app = Flask(__name__)
posts = Post()

EMAIL_USER = environ.get('MY_EMAIL')
EMAIL_PASS = environ.get('MY_EMAIL_PASSWORD')


@app.route('/')
def home():
    return render_template('index.html', posts=posts.all_posts)


@app.route('/about-us')
def about():
    return render_template('about.html', post=None)


@app.route('/about-us/<int:index>')
def about_fake(index):
    current_post = posts.get_blog(index)
    return render_template('about.html', post=current_post)


@app.route('/contact-us', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', message='Contact')
    else:
        subject = "Subject:New Message!\n\n"
        message_body = f"""
            Name: {request.form['name']}
            Email: {request.form['email']}
            Phone: {request.form['phone']}
            Message: {request.form['message']}
        """
        final_msg = subject + message_body

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_USER, password=EMAIL_PASS)
            connection.sendmail(
                from_addr=EMAIL_USER,
                to_addrs=EMAIL_USER,
                msg=final_msg
            )
        return render_template('contact.html', message='Successfully sent message')


@app.route('/posts/<int:index>')
def get_post(index):
    current_post = posts.get_blog(index)
    return render_template('post.html', post=current_post)


if __name__ == '__main__':
    app.run(debug=True)
