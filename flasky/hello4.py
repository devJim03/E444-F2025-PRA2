from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-very-secret-key'  # required for sessions and flashing

bootstrap = Bootstrap(app)

# Define the form
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your Uoft email?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# Main route
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    
    current_name = session.get('name', 'Stranger')
    current_email = session.get('email', '')

    if form.validate_on_submit():
        new_name = form.name.data
        new_email = form.email.data

        # Name flash
        old_name = session.get('name')
        if old_name is not None and old_name != new_name:
            flash("Looks like you have changed your name!")
        session['name'] = new_name
        current_name = new_name

        # Email flash
        old_email = session.get('email')
        if old_email is not None and old_email != new_email:
            flash("Looks like you've changed your email!")
        session['email'] = new_email
        current_email = new_email

        return redirect(url_for('index'))

    return render_template(
        'section4.html',
        form=form,
        name=current_name,
        email=current_email
    )

if __name__ == '__main__':
    app.run(debug=True)
