import string
import random


def email():
    N = 4

    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.ascii_letters.lower(), k=N))
    mail = "manu" + str(res) + "@gmail.com"

    return mail


def password():
    N = 8

    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.ascii_letters.lower(), k=N))

    return str(res)


def firstName():
    N = 5

    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.ascii_letters.lower(), k=N))

    fname = "Jayesh" + " " + str(res)

    return fname


def adminComment():
    N = 20

    res = ''.join(random.choices(string.ascii_lowercase + " " +
                                 string.ascii_letters.lower() + " ", k=N))

    return res


def lastName():
    N = 5

    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.ascii_letters.lower(), k=N))

    lname = str(res)

    return lname


def company():
    N = 6

    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.ascii_letters.lower(), k=N))

    lname = str(res)

    return lname


def phoneNumber():
    N = 10

    res = ''.join(random.choices(string.digits, k=N))

    phone = str(res)

    return phone

print(adminComment())
