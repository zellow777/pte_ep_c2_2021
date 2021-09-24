input = int(input("Adja meg az időtartalmat másodpercben:"))


def yearcount(x):
    years = x // (365 * 24 * 60 * 60)
    return(years)


years = yearcount(input)


def daycount(x):
    days = (x - years * (365 * 24 * 60 * 60)) // (24 * 60 * 60)
    return(days)


days = daycount(input)


def hourcount(x):
    hours = (x - years * (365 * 24 * 60 * 60) - days * (24 * 60 * 60)) // (60 * 60)
    return(hours)


hours = hourcount(input)


def minutecount(x):
    minutes = (x - years * (365 * 24 * 60 * 60) - days * (24 * 60 * 60) - hours * (60 * 60)) // 60
    return(minutes)


minutes = minutecount(input)


def secondcount(x):
    seconds = x - years * (365 * 24 * 60 * 60) - days * (24 * 60 * 60) - minutes * (60 * 60)
    return(seconds)


seconds = secondcount(input)

print(years, days, hours, minutes, seconds)
