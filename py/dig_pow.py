def dig_pow(n, p):
    # your code
    tot = 0
    for N in list(str(n)):
        tot += int(N)**p
        p +=1
    print(tot)
    if tot % n == 0:
        return int(tot/n)
    else:
        return -1

def dig_pow_other(n, p):
    # your code
    tot = sum([x**y for x, y in zip([int(x) for x in list(str(n))], list(range(p, p+len(str(n)))))])
    if tot % n == 0:
        return int(tot/n)
    else:
        return -1


def dig_pow_still_other(n, p):
    t = sum( [int(j)**(i+p) for i,j in enumerate(str(n)) ])
    return t//n if t % n == 0 else -1

print(dig_pow(46288, 3))
print(dig_pow_other(46288, 3))
print(dig_pow_still_other(46288, 3))


