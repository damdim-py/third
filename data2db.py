from data import teachers
from json import dump

booking = {}

with open("db/teachers.json", "w") as f:
    for idx, teacher in enumerate(teachers):
        booking[int(teacher["id"])] = teacher["free"]
        del teachers[idx]["free"]
    dump(teachers, f)

with open("db/booking.json", "w") as f:
    dump(booking, f)

