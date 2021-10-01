try:
    rawinput = input("Please give us a duration in seconds: ")
    sumOfSeconds = int(rawinput)
    if sumOfSeconds < 0:
        print("Invalid input")
    elif sumOfSeconds == 0:
        print("Now")
    else:
        secondsInMinute = 60
        secondsInHour = 60 * secondsInMinute
        secondsInDay = 24 * secondsInHour
        secondsInYear = 365 * secondsInDay

        years = sumOfSeconds // secondsInYear
        sumOfSeconds = sumOfSeconds - years * secondsInYear

        days = sumOfSeconds // secondsInDay
        sumOfSeconds = sumOfSeconds - days * secondsInDay

        hours = sumOfSeconds // secondsInHour
        sumOfSeconds = sumOfSeconds - hours * secondsInHour

        minutes = sumOfSeconds // secondsInMinute
        seconds = sumOfSeconds - minutes * secondsInMinute

        numberOfUnits = 0
        if years > 0:
            numberOfUnits += 1
        if days > 0:
            numberOfUnits += 1
        if hours > 0:
            numberOfUnits += 1
        if minutes > 0:
            numberOfUnits += 1

        output = ""
        if years > 0:
            output += str(years) + "year"
            if years > 1:
                output += "s "
            if numberOfUnits > 2:
                output += ", "
            elif numberOfUnits == 2:
                output += " and "
            numberOfUnits -= 1
        if days > 0:
            output += str(days) + "day"
            if days > 1:
                output += "s "
            if numberOfUnits > 2:
                output += ", "
            elif numberOfUnits == 2:
                output += " and "
            numberOfUnits -= 1
        if hours > 0:
            output += str(hours) + "hour"
            if hours > 1:
                output += "s "
            if numberOfUnits > 2:
                output += ", "
            elif numberOfUnits == 2:
                output += " and "
            numberOfUnits -= 1
        if minutes > 0:
            output += str(minutes) + "minute"
            if minutes > 1:
                output += "s "
            elif numberOfUnits == 2:
                output += " and "
            numberOfUnits -= 1
        if seconds > 0:
            output += str(seconds) + "second"
            if seconds > 1:
                output += "s "
            elif numberOfUnits == 2:
                output += " and "
            numberOfUnits -= 1
    print(output)
except ValueError:
    print("Invalid input")



