from flask import Flask, render_template, redirect, request
from json import load

from forms import BookingForm


app = Flask(__name__)

def read_db():
    with open("db/teachers.json") as f:
        teachers = load(f)

    with open("db/booking.json") as f:
        booking = load(f)
    return teachers, booking

@app.route("/")
def page_home():
    return "здесь будет главная)"

@app.route("/goals/<id>")
def goal_view(id):
    return f"здесь будет цель {id}"

@app.route("/profiles/<int:id>")
def profile_view(id):
    teachers, booking = read_db()
    return render_template("profile.html", teacher=teachers[id], booking=booking[str(id)])

@app.route("/request")
def requests_list():
    return "здесь будет заявка на подбор"

@app.route("/request_done")
def request_done():
    return "заявка на подбор отправлена"

@app.route("/booking/<int:profile_id>/<day_name>/<time_value>", methods=["GET", "POST"])
def booking_add(profile_id, day_name, time_value):
    teachers, booking = read_db()
    form = BookingForm(request.form)
    form.clientTeacher.data = profile_id
    form.clientWeekday.data = day_name
    form.clientTime.data = time_value
    if form.validate():
        form.save()
        return redirect('/booking_done')
    return render_template("booking.html", teacher=teachers[profile_id], day_name=day_name, time_value=time_value, form=form)

@app.route("/booking_done")
def booking_done():
    return "заявка отправлена"



if __name__ == "__main__":
    app.run(debug=True)