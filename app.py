from flask import Flask
from flask import render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Cristian'
    course = 'Python'
    is_premium = False
    courses = ['Python', 'Ruby', 'Java', 'Elixir']
    return render_template("index.html", 
    username=name,course_name=course,
    is_premium=is_premium,
    courses=courses
    )

@app.route('/about')
def about():
    print("Estamos en el about")
    return render_template('about.html')

@app.after_request
def after_request(res):
    print("despues del la petición")
    return res


@app.before_request
def before_request():
    print('Antes de la petición')

@app.route('/datos')
def datos():
      nombre = request.args.get('nombre', '')
      curso =  request.args.get('curso', '')
      
      return 'Listado de datos : ' + nombre + ' '  + curso

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def user(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def path(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)



if __name__ == '__main__':
    app.run(debug=True)