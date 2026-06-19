def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split("/")

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    percent = round((x / y) * 100)
    return percent


def gauge(percentage):
    if str( percentage ) <= 1:
        return "E"
    elif str( percentage ) >= 99:
        return "F"
    else:
        return f"{str( percentage )}%"
    

if __name__ == '__main__' :
    main(  )