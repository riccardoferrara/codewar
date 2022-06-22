def accum(s):
    return '-'.join([j.upper() + i*j.lower() for i, j in enumerate(s)])



print(accum("ZpglnRxqenU")) # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")