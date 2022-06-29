# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:


# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].


def snail(snail_map):
    left_to_right = True
    up_to_down = False
    right_to_left = False
    down_to_up = False
    s = [] #solution vector
    l = len(snail_map)*len(snail_map[0]) #lenght of the solution
    min_i = -1
    min_j = -1
    max_i = l**0.5
    max_j = l**0.5
    i = -1
    j = -1
    while len(s) < l:
        if left_to_right:
            i += 1
            j += 1
            while i < max_i:
                s.append(snail_map[j][i])
                i += 1
            max_i = i
            min_j = j
            left_to_right = False
            up_to_down = True
            if len(s) == l:
                return s
        if up_to_down:
            j += 1
            i -= 1
            while j < max_j:
                s.append(snail_map[j][i])
                j += 1
            max_j = j
            max_i = i
            up_to_down = False
            right_to_left = True
            if len(s) == l:
                return s
        if right_to_left:
            i -= 1
            j -= 1
            while i > min_i:
                s.append(snail_map[j][i])
                i -= 1
            min_i = i
            max_j = j
            right_to_left = False
            down_to_up = True
            if len(s) == l:
                return s
        if down_to_up:
            i += 1
            j -= 1
            while j > min_j:
                s.append(snail_map[j][i])
                j -= 1
            min_j = j + 1
            min_i = i
            down_to_up = False
            left_to_right = True
            if len(s) == l:
                return s
    return s


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array))


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))