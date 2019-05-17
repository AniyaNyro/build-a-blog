from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:giraFFe17@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'giraFFE17'



class blog_entries(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_text  = db.Column(db.String(2000))

    def __init__(self, blog_title, blog_text):
        self.blog_title = title
        self.blog_text = text


@app.route('/add-post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post = User.query.filter_by(title=title).first()
        if user:
            flash("New Blog Entry")
            return redirect('/')
    return render_template('/add-post')



@app.route('/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        # TODO - validate user's data

        existing_user = User.query.filter_by(email=email).first()
        if not existing_user:
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            session['email'] = email
            return redirect('/')
        else:
            # TODO - user better response messaging
            return "<h1>Duplicate user</h1>"

    return render_template('register.html')



@app.route('/delete-post', methods=['POST'])
def delete_task():

    blog_id = int(request.form['id'])
    id = Task.query.get(blog_id)
    id.completed = True
    db.session.add(id)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()