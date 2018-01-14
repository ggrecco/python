def vestibular():
    t = 93
    p = t // 5
    while (t - p * 5) % 7 != 0:
        p = p - 1
    g = (t - p * 5) // 7
    return "{} menores e {} maiores".format(p,g)
