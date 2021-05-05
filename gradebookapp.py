from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import re
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw13.db'


db = SQLAlchemy(app=app)


engine = create_engine('sqlite:///hw13.db', echo=True)
with open('schema.sql') as file:
    statements = re.split(r';\s*$', file.read(), flags=re.MULTILINE)
    for statement in statements:
        if statement:
            engine.execute(text(statement))


from routes import * 

session = Session(engine)



Base = automap_base()
Base.prepare(engine, reflect=True)
Student = Base.classes.students
Quiz = Base.classes.quizzes
Result = Base.classes.results






if __name__ == '__main__':
    app.run(debug=True)