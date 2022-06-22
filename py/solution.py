def solution(string, ending):
    return False if ending not in string else string.replace(ending, '*')[-1:] == '*'

print(solution('abcde', 'cde')) # True