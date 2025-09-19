from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
app = Flask(__name__)
bootstrap = Bootstrap(app)  # Initialize Flask-Bootstrap
moment = Moment(app)

@app.route('/', defaults={'name': 'Jim'}) #default name to Jim
@app.route('/<name>')
def index(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow()) #basically go into the templates folder and user the user.html template

if __name__ == '__main__':
    app.run(debug=True)