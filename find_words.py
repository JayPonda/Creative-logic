import numpy as np


def cmpList(x, y):
    print(x, y)
    for i in x:
        if sorted(y) == sorted(i):
            return False
    return True


def appendList(x, y):
    x.append(y)
# ------------------------------------------------
# this is the function called last and most important cheaker cheak
# the word at spacific direction until word find or rejected example: c (0, 0) ,a (0, 1) meance no change in row but
# increse the col so it chake c a k e k r w ... like that


def cheaker(arr, main_row, main_col, change_in_row, change_in_col, list_of_words):
    address_of_words = []
    ii = 0
    can_i_check_diff = True
    predect = False
    p1, p2 = arr.shape

    while ii < len(list_of_words) and can_i_check_diff:

        i = 0
        word = list_of_words[ii]
        current_row = main_row
        current_col = main_col
        predect = False

        while (current_row < p1 and current_col < p2) and (current_row >= 0 and current_col >= 0) and (len(word) > i):

            if i == len(word) - 1:
                if word[i] == arr[current_row][current_col]:
                    address_of_words.append((current_row, current_col))
                    predect = True
                break
            else:
                if word[i] == arr[current_row][current_col]:
                    address_of_words.append((current_row, current_col))
                    i += 1
                    current_row += change_in_row
                    current_col += change_in_col
                else:
                    break

        if predect:
            tem = len(dic_of_words[word])

            if tem == 0:
                appendList(dic_of_words[word], address_of_words)
            else:
                if list(word) == list(word)[::-1]:
                    if cmpList(dic_of_words[word], address_of_words):
                        appendList(dic_of_words[word], address_of_words)
                else:
                    appendList(dic_of_words[word], address_of_words)

            for i in range(len(list_of_words)):
                if(i == ii):
                    continue
                elif(list_of_words[i].find(list_of_words[ii]) == -1):
                    can_i_check_diff = False
                else:
                    can_i_check_diff = True
                    predect = False
                    address_of_words.clear()
                    break

        else:
            address_of_words.clear()
        ii += 1


# -------------------------------------------------------
# this is th function called to check the words by first two letters
# this function is called to know which words can posibile with it
# example: c a => (0, 0) (0, 1) then make a list ['cat', 'cake', 'car'] and return

def list_of_possible_words(list_inp, x, y):
    temp = []
    for i in list_inp:
        if unique:
            if len(dic_of_words[i]) == 1:
                pass
            else:
                if i[0] == x and i[1] == y:
                    temp.append(i)
        else:
            if i[0] == x and i[1] == y:
                temp.append(i)
    return temp

# -------------------------------------------------------------
# this function is the helper of predicoter this
# function is call list_of_possible_words and the go to cheaker with the list(from list_of_possible_words)
# and direction , example: c at (0, 0) and a at (0, 1) so cheaker(arr, 0, 0, 0, 1, ['car', 'cat', 'cake'])


def helper(arr, main_row, main_col, change_in_row, change_in_col, list_of_inp):
    main_arr_char = arr[main_row][main_col]
    arr_char = arr[main_row + change_in_row][main_col + change_in_col]
    match = list_of_possible_words(list_of_inp, main_arr_char, arr_char)
    if match != []:
        cheaker(arr, main_row, main_col, change_in_row, change_in_col, match)


# -----------------------------------------------------------
# this function is call at first
# this function predect , if any words can start at this location
# in first array(in docstring), it check in every 8 position around it
# example : c a => (0, 0) (0, 1) / c p => (0, 0) (1, 1)/ c a => (0, 0) (1, 0)

def predicoter(arr, main_row, main_col, list_of_inp):
    p1, p2 = arr.shape
    main_arr_char = arr[main_row][main_col]

    if main_arr_char in list_of_first_char:
        if main_row - 1 >= 0:
            if(dig):
                if main_col - 1 >= 0:
                    helper(arr, main_row, main_col, -1, -1, list_of_inp)
                if main_col + 1 < p2:
                    helper(arr, main_row, main_col, -1, 1, list_of_inp)

            helper(arr, main_row, main_col, -1, 0, list_of_inp)

        if main_row + 1 < p1:
            if(dig):
                if main_col - 1 >= 0:
                    helper(arr, main_row, main_col, 1, -1, list_of_inp)

                if main_col + 1 < p2:
                    helper(arr, main_row, main_col, 1, 1, list_of_inp)

            helper(arr, main_row, main_col, 1, 0, list_of_inp)

        if main_col + 1 < p2:
            helper(arr, main_row, main_col, 0, 1, list_of_inp)

        if main_col - 1 >= 0:
            helper(arr, main_row, main_col, 0, -1, list_of_inp)


# ---------------------------------------------------
# test arrays
# if you want to take inputs from .txt file (type the individual char with space) then add this
# arr = np.loadtxt("readme.txt", dtype = str)

"""arr = np.array([['c', 'a', 'k', 'e', 'k', 'r', 'w', 'e', 'f', 'k'],
                ['a', 'p', 'i', 'g', 'w', 'w', 'h', 't', 't', 'u'],
                ['t', 'p', 'h', 'y', 'b', 'b', 'a', 'b', 'y', 'x'],
                ['f', 'l', 'o', 'w', 'e', 'r', 'n', 'a', 's', 'z'],
                ['i', 'e', 'r', 'w', 'a', 'e', 'd', 'l', 'x', 'f'],
                ['s', 'y', 's', 'i', 'r', 'a', 'b', 'l', 'i', 'r'],
                ['h', 'b', 'e', 'l', 'l', 'd', 'f', 'n', 'b', 'i'],
                ['o', 'o', 'c', 'o', 'w', 's', 'i', 's', 'u', 'n'],
                ['e', 'a', 'a', 'j', 'b', 'i', 'r', 'd', 'o', 'g'],
                ['w', 't', 'r', 'e', 'e', 'y', 'e', 'u', 'y', 'k']])"""
""" words for the searches  for above array
apple
baby
bear
bell
tree
sun
bread
hand
cat
fish
shoe
hourse
boat
car
cow
fire
ring
eye
pig
cake
flower
ball"""

arr = np.array([['l', 'f', 'l', 'o', 'w', 'e', 'r', 'm'],
                ['a', 'n', 'q', 's', 'm', 's', 'w', 'x'],
                ['m', 'e', 'w', 'a', 'd', 'm', 's', 'q'],
                ['b', 't', 'z', 'e', 'q', 's', 'p', 'q'],
                ['x', 'b', 'u', 'd', 'e', 'q', 'r', 'r'],
                ['q', 'z', 'u', 'b', 'g', 'y', 'i', 'a'],
                ['z', 'a', 'c', 'l', 'g', 'z', 'n', 'i'],
                ['b', 'i', 'r', 'd', 'q', 'j', 'g', 'n']])

"""  words for the searches  for above array
bird
bud
egg
flower
lamb
net
rain
spring"""

# ------------------------------------------------------
# time to take inputs
# unique means one value can discoverd only one time

unique = True if input("your values are unique? yes=1/no=0 ") == '1' else False
print("your values are unique:- ", unique)

dig = True if input(
    "your values are align diagnaloy? yes=1/no=0 ") == '1' else False
print("your values are unique:- ", dig)

ran = int(input("how many words do you want to search? "))
dic_of_words = {}
lis = []

print("your value is unique: ", unique, "\nwrite words:")
for i in range(ran):
    kk = input()
    dic_of_words[kk] = []
    lis.append(kk)
lis.sort()

list_of_first_char = sorted(list(set([i[0] for i in lis])))

# -------------------------------------------------------
# now start the processing

row, col = arr.shape
for i in range(row):
    for j in range(col):
        predicoter(arr, i, j, lis)

main_dix = {}
main_dix['propertyes'] = {'unique': unique, 'is_dig': dig}
main_dix['words'] = dic_of_words

# --------------------------------------------------------
# print the results

print("//results\\\\".center(75, "-"))
print("| UNIQUE VALUES: ", main_dix['propertyes']['unique'])
print("| DIAGNAL VALUES: ", main_dix['propertyes']['is_dig'])
print("| TOTAL WORDS: ", (len(main_dix['words'])))

for key, val in main_dix['words'].items():
    print("| %-20s " % key, " -- ", val)

print("|\n", "|end|".center(75, "-"))
