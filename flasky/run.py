from flask import *
from flask.ext.wtf import *
from wtforms import *
from wtforms.validators import DataRequired
import urllib2
import json
import csv

app = Flask(__name__)
app.config.from_object('config')


class userInputStatement(Form):
	statement = StringField('statement', validators=[DataRequired()])
	filtered = SelectField('filtered', choices=['yes'])

@app.route('/financial', methods=['GET', 'POST'])
def financial():

        return render_template('financial.html')

@app.route('/income', methods=['GET', 'POST'])
def income():
	
        return render_template('income.html')

@app.route('/', methods=['GET', 'POST'])
def statementInput():
	form = userInputStatement()
	return render_template('statement.html',
				form=form)

if __name__ == '__main__':
	app.run(debug=True)
