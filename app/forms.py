from flask_wtf import Form
from wtforms import RadioField, SubmitField
from wtforms import validators, ValidationError

class GraphChoice(Form):
    # Interval = RadioField('Interval', choices = [('1','last12hrs'),('2','last24hrs'),
    #  ('3','thisweek'),('4','last7days'), ('5','thismonth'), ('6','lastmonth'), ('7','thisyear')])
    goto_subisu = SubmitField('Subisu')
    goto_wlink = SubmitField('Wlink')
    goto_cacti = SubmitField('Router')
