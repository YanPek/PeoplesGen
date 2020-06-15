import random

def FullNameGen():
    n = open("n.txt", "r", encoding="utf8")
    ln = open("ln.txt", "r", encoding="utf8")
    mn = open("mn.txt", "r", encoding="utf8")
    Name = n.readlines()
    LastName = ln.readlines()
    MiddleName = mn.readlines()
    n.close()
    ln.close()
    mn.close()
    FullName = "Name: " + Name[random.randint(0,402)] + "LastName: " + LastName[random.randint(0,501)] + "MiddleName: " + MiddleName[random.randint(0,199)]
    return FullName

def PassGen():
    chars = "abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRSTVUWXYZ1234567890"
    minpassword = ""
    normpassword = ""
    bigpassword = ""

    for i in range(5):
        minpassword += random.choice(chars)

    for i in range(9):
        normpassword += random.choice(chars)

    for i in range(27):
        bigpassword += random.choice(chars)

    passes = "MinPass: " + minpassword + "123\nNormPass: " + normpassword + "123\nBigPass: " + bigpassword + "123"
    return passes

def DateGen():
    a = random.randint(1,28)
    if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6 or a == 7 or a == 8 or a == 9:
        a = f"0{a}"
    b = random.randint(1,12)
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9:
        b = f"0{b}"
    Date = f"\nDate: {a}/{b}/{random.randint(1955, 2000)}"
    return Date

def Start():
    f = open("Peoples.txt", "a", encoding="utf8")
    a = 0
    while True:
        a += 1
        f.write(f"\n--------------------------------------------------\n[{a}]\n{FullNameGen()}{PassGen()}{DateGen()}")
    f.close()

Start()