#!/bin/python3

from flask import Flask
from flask import request


def conv(string_time):
    # make sure the data is correct
    try:
        hh, mm = string_time.split(":")
        hour = int(hh)
        minute = int(mm)
    except:
        return None, None

# convert to 12-hour format
    if hour > 12:
        hour = hour - 12

# yet again make sure the data is correct
    if minute not in list(range(0, 60)):
        return None, None
    if hour not in list(range(1, 13)):
        return None, None

    return hour, minute


def mirror_hour(hour, minute):
    # converts hours
    if minute == 0:
        if hour == 12:
            return 12
        else:
            return (12 - hour)
    else:
        if hour == 12:
            return 11
        elif hour == 11:
            return 12
        else:
            return (11 - hour)


def mirror_minute(minute):
    # converts minutes
    if minute == 0:
        # unique case
        return str("00")
    else:
        # another unique case
        if minute > 50:
            return ("0" + str(60 - minute))
        else:
            return (60 - minute)


app = Flask(__name__)


@app.route("/")
def index():
    original = request.args.get("original", "")
    if original:
        hh, mm = conv(original)
        if hh is None or mm is None:
            mirror = "This ain't gonna work"
        else:
            hour, minute = mirror_hour(hh, mm), mirror_minute(mm)
            mirror = f"{hour}:{minute}"
    else:
        mirror = ""
    return (
        """<form action="" method="get">
                The clock in the mirror: <input type="text" name="original">
                <input type="submit" value="Mirror the time">
            </form>"""
        + "Mirrored time: "
        + mirror
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
