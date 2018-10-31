import  random as rm

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
length = input('password length?')
len = int(length)
Noofpass = input('Number of Passwords?')
NoPass = int(Noofpass)
for p in range(NoPass):
    password = ''
    for c in range(len):
        password += rm.choice(chars)
    print(password)