WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def add_time(start, duration, week_day=None):
    start, meredien = start.split()
    start_hour, start_min = start.split(":")
    start_hour, start_min = int(start_hour), int(start_min)
    days = 0

    if meredien == "AM" and start_hour == 12:
        hour24 = 0
    elif meredien == "PM" and start_hour == 12:
        hour24 = start_hour
    elif meredien == "AM" and start_hour < 12:
        hour24 = start_hour
    else:
        hour24 = start_hour + 12
    min24 = start_min

    dur_hour, dur_min = duration.split(":")

    end_hour = hour24 + int(dur_hour)
    end_min = min24 + int(dur_min)

    if end_min >= 60:
        end_hour += 1
        end_min -= 60

    if end_hour >= 24:
        days = round(end_hour / 24)
        end_hour %= 24

    meredien = "AM"

    if end_hour >= 12:
        end_hour -= 12
        meredien = "PM"

    final_time = f"{end_hour or 12}:{str(end_min).zfill(2)} {meredien}"

    if week_day is not None:
        week_day = week_day.lower().title()
        num_week_day = WEEKDAYS.index(week_day)
        num_week_day = (num_week_day + days) % 7
        final_week_day = WEEKDAYS[num_week_day]

        if days == 1:
            final_time += f", {final_week_day} (next day)"
        elif days > 1:
            final_time += f", {final_week_day} ({days} days later)"
        else:
            final_time += f", {week_day}"
    else:
        if days == 1:
            final_time += f" (next day)"
        elif days > 1:
            final_time += f" ({days} days later)"

    return final_time
