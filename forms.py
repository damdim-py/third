from wtforms.form import Form
from wtforms.fields import StringField, HiddenField
from wtforms import validators
from json import load, dumps


class BookingForm(Form):
    clientName = StringField('Вас зовут', validators=[validators.input_required()])
    clientPhone = StringField('Ваш телефон', validators=[validators.input_required()])
    clientWeekday = HiddenField()
    clientTime = HiddenField()
    clientTeacher = HiddenField()

    def save(self):
        with open("db/booking.json", "r+") as f:
            booking = load(f)
            booking[str(self.clientTeacher.data)][self.clientWeekday.data][self.clientTime.data] = False
            f.seek(0)
            f.write(dumps(booking))