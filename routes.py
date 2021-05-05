from gradebookapp import app, db, session, Student, Quiz, Result, engine
from flask import render_template, redirect, url_for, session, request, flash
import forms
from markupsafe import escape


@app.route('/')
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        if session['username'] == 'admin' and session['password'] == 'password':
            
            with engine.connect() as con:
                roster_table = con.execute('SELECT * FROM students')
                quiz_table = con.execute('SELECT * FROM quizzes')
                result_table = con.execute('SELECT * FROM results')
                return render_template('dashboard.html', roster_table=roster_table, quiz_table=quiz_table, result_table=result_table, current_user=escape(session['username']))

        else:
            flash('You are not logged in.')
            return redirect(url_for('login'))

        
        return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    form = forms.AddStudentForm()
    
    if form.validate_on_submit():
        s = Student(first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(s)
        db.session.commit()
        flash('Student added.')
        return redirect(url_for('dashboard'))
        
    else:
        return render_template('add_student.html', form=form)
        
        
@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    form = forms.AddQuizForm()

    if form.validate_on_submit():
       q = Quiz(subject=form.subject.data, num_questions=form.num_questions.data, date=form.date.data)
       db.session.add(q)
       db.session.commit()
       flash('Quiz added.')
       return redirect(url_for('dashboard'))

    else:
        return render_template('add_quiz.html', form=form)
        


@app.route('/result/add', methods=['GET', 'POST'])
def add_result():

    available_student_ids = db.session.query(Student).all()
    available_student_ids_list = [i.student_id for i in available_student_ids]

    available_quiz_ids = db.session.query(Quiz).all()
    available_quiz_ids_list = [i.quiz_id for i in available_quiz_ids]

    form = forms.AddResultForm()

    form.student_id.choices = available_student_ids_list
    form.quiz_id.choices = available_quiz_ids_list

    if form.validate_on_submit():
        if int(form.result.data) > 0 and int(form.result.data) < 101:
            r = Result(student_id=form.student_id.data, quiz_id=form.quiz_id.data, result=form.result.data)
            db.session.add(r)
            db.session.commit()
            flash('Result added.')
            return redirect(url_for('dashboard'))
        else:
            flash('Error: Result must be between 0 and 100')
            return render_template('add_result.html', form=form)

    else:
        return render_template('add_result.html', form=form)


@app.route('/student/<id>')
def student_record(id):

    with engine.connect() as con:
        query = '''SELECT students.first_name, students.last_name, quizzes.subject, quizzes.date, results.result
        FROM students 
        LEFT JOIN results
        ON students.student_id = results.student_id 
        LEFT JOIN quizzes 
        ON quizzes.quiz_id = results.quiz_id
        WHERE students.student_id = ''' + str(id) + ';'
        record = con.execute(query).fetchall()
        for item in record:
            first_name = item[0]
            last_name = item[1]
            subject = item[2]
            date = item[3]
            result = item[4]
            return render_template('student_record.html', record=record, student_id=id, first_name=first_name, last_name=last_name, subject=subject, date=date, result=result)
 
