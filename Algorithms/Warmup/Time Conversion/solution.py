def timeConversion(s):
    last = s[-2:]
    new = ""
    hh = int(s[:2])

    if last == "PM" and hh < 12: 
        converted = hh + 12
        new += str(converted)
        return new + s[2:-2]

    elif last == "AM" and hh == 12:
        new += str("00")
        return new + s[2:-2]

    return s[:-2]
