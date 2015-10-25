from datetime import time
import re


def parse_time(arg):
    """ Returns datetime.time object
    based on parsed argument string
    Only accepts in the following format:

    [xx]:[yy] -> am/pm left out, use military time
    [xx]-> am/pm left out, use military time
    [xx]:[yy][am/pm]
    [xx][am/pm] -> xx is evaluated as hour
    [xxxx] -> xxxx is evaluated as hhmm
    [xxxx][am/pm]
    [xxx] -> evaluated as [0xxx]
    [xxx][am/pm] -> evaluated as [0xxx][am/pm]

    Currently no space is allowed between digits and am/pm
    Also, [xx] includes [x]
    """
    try:
        if re.match(r'(^\d\d:\d\d$)|(^\d:\d\d$)', arg):
            split_arg = arg.split(':')
            return time(int(split_arg[0]), int(split_arg[1]))
        elif re.match(r'(^\d$)|(^\d\d$)', arg):
            return time(int(arg))
        elif re.match(r'(^\d\d\d\d$)', arg):
            return time(int(arg[:2]), int(arg[2:]))
        elif re.match(r'(^\d\d\d$)', arg):
            return time(int(arg[:1]), int(arg[1:]))
        elif re.match(r'(^\d\d:\d\d[ap]m$)|(^\d:\d\d[ap]m$)',
                      arg,
                      re.IGNORECASE):
            split_arg = arg.split(':')
            hour = int(split_arg[0])
            minute = int(split_arg[1][:2])
            meridiem = split_arg[1][2:]

            if hour > 12 or hour == 0:
                return time(hour, minute)
            elif meridiem.lower() == 'am' and hour == 12:
                hour = 0
            elif meridiem.lower() == 'pm' and hour != 12:
                hour += 12
            return time(hour, minute)
        elif re.match(r'(^\d\d\d\d[ap]m$)', arg, re.IGNORECASE):
            hour = int(arg[:2])
            minute = int(arg[2:4])
            meridiem = arg[4:6]

            if hour > 12 or hour == 0:
                return time(hour, minute)
            elif meridiem.lower() == 'am' and hour == 12:
                hour = 0
            elif meridiem.lower() == 'pm' and hour != 12:
                hour += 12
            return time(hour, minute)
        elif re.match(r'(^\d\d\d[ap]m$)', arg, re.IGNORECASE):
            hour = int(arg[:1])
            minute = int(arg[1:3])
            meridiem = arg[3:5]

            if hour > 12 or hour == 0:
                return time(hour, minute)
            elif meridiem.lower() == 'am' and hour == 12:
                hour = 0
            elif meridiem.lower() == 'pm' and hour != 12:
                hour += 12
            return time(hour, minute)
        elif re.match(r'(^\d\d[ap]m$)', arg, re.IGNORECASE):
            hour = int(arg[:2])
            meridiem = arg[2:4]

            if hour > 12 or hour == 0:
                return time(hour)
            elif meridiem.lower() == 'am' and hour == 12:
                hour = 0
            elif meridiem.lower() == 'pm' and hour != 12:
                hour += 12
            return time(hour)
        elif re.match(r'(^\d[ap]m$)', arg, re.IGNORECASE):
            hour = int(arg[:1])
            meridiem = arg[1:3]

            if hour > 12 or hour == 0:
                return time(hour)
            elif meridiem.lower() == 'am' and hour == 12:
                hour = 0
            elif meridiem.lower() == 'pm' and hour != 12:
                hour += 12
            return time(hour)
        else:
            raise ValueError('Invalid time input')
    except ValueError:
        raise
    except:
        print("Unexpected exception")
        raise


def time_string(time):
    """ Returns string formatted date
    param time<datetime.time>
    """
    hour = time.hour
    minute = time.minute

    if hour >= 12:
        meridiem = 'PM'
    else:
        meridiem = 'AM'

    hour %= 12

    if hour == 0:
        hour += 1

    str_hour = str(hour)
    if hour < 10:
        str_hour = '0' + str(hour)

    str_minutes = str(minute)
    if minute < 10:
        str_minutes = '0' + str(minute)

    return str_hour + ':' + str_minutes + meridiem
