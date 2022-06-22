def disemvowel(string_):
    string_ = ''.join([i for i in filter(lambda x:x not in 'aeiouAEIOU', string_)])
    return string_


print(disemvowel("This website is for losers LOL!"))