from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from gradebookapp import app, db, session, Student, Quiz, Result, engine



class AddStudentForm(FlaskForm):
    student_id = StringField('Student ID')
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Add Student to Roster')


class AddQuizForm(FlaskForm):
    quiz_id = StringField('Quiz ID')
    subject = StringField('Subject', validators=[DataRequired()])
    num_questions = StringField('Number of Questions', validators=[DataRequired()])
    date = StringField('Due Date', validators=[DataRequired()])
    submit = SubmitField('Add Quiz to Gradebook')


class AddResultForm(FlaskForm):
    student_id = SelectField('Student ID', coerce=int, validators=[DataRequired()])
    quiz_id = SelectField('Quiz ID', coerce=int, validators=[DataRequired()])
    result = StringField('Result', validators=[DataRequired()])
    submit = SubmitField('Add Result to Student Record')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


