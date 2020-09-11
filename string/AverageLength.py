import math


def average_length(str):
    print("Input String : {}".format(str))
    split_str = str.strip().split(" ")
    word_len_arr = []
    total_word_len = 0
    for i in split_str:
        word_len = len(i.replace(" ", "").replace(",", ""))
        if word_len > 0:
            word_len_arr.append(word_len)

    for word_len in word_len_arr:
        total_word_len = total_word_len + word_len

    print("Length of all words : {}".format(total_word_len))
    print("Total words : {}".format(len(word_len_arr)))
    return math.floor(total_word_len / len(word_len_arr))


str = " Hello   ,  Python   "
print("Average Length : {}".format(average_length(str)))
