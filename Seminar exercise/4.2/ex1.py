def count_chars(string):
    result_dic = {}
    for char in string:
        if char in result_dic:
            result_dic[char] += 1
        else:
            result_dic[char] = 1
    return result_dic

string = input("Enter a string: ").split(" ")
print(count_chars(string))