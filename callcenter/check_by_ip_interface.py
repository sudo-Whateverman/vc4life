from random import randint


def check_rand(ip):
    if ip is not None:
        return randint(0, 5)
    else:
        return 0

def check(ip):
    vars = [
        ('decomombulator', 'notOK'),
        ('ping', 'notOK'),
        ('thrusters', 'notOK'),
        ('wifi', 'notOK'),
        ('Blood of a virgin', 'notOK'),
        ('A plan B', 'notOK')
    ]
    number = check_rand(ip)
    for i in range(number):
        vars[i] = (vars[i][0], 'OK')
    return vars
# you were expecting an actual interface that pings the system and gets the status?
# Tough luck buddy, I implemented this random thingy that just tells me how many tests passed.
