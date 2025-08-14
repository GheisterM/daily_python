import csv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
FILEPATH = '47_coffee_and_wifi/cafe-data.csv'


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField(
        'Location URL', validators=[DataRequired(), URL()]
    )
    open_time = TimeField('Opening Time', validators=[DataRequired()])
    close_time = TimeField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(
        'Coffee Rating',
        choices=['☕️', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
        validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        'Wifi strength Rating',
        choices=['✘', '🛜', '🛜🛜', '🛜🛜🛜', '🛜🛜🛜🛜', '🛜🛜🛜🛜🛜'],
        validators=[DataRequired()]
    )
    power_rating = SelectField(
        'Power Socket Availability',
        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = [
            form.cafe.data,
            form.location_url.data,
            form.open_time.data.strftime('%-I:%M%p'),
            form.close_time.data.strftime('%-I:%M%p'),
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data
        ]
        with open(FILEPATH, 'r+', newline='', encoding='utf-8') as csv_file:
            lines = csv_file.read()
            if lines[-1] != '\n':
                csv_file.write('\n')
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(new_row)
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(FILEPATH, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
