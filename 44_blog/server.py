from flask import Flask, render_template
from post import Post

app = Flask(__name__)
posts = Post()


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


@app.route('/contact-us')
def contact():
    return render_template('contact.html')


@app.route('/posts/<int:index>')
def get_post(index):
    current_post = posts.get_blog(index)
    return render_template('post.html', post=current_post)


if __name__ == '__main__':
    app.run(debug=True)
