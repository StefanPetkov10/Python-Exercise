def count_it(sequence):
    count_dict = {}
    for num_str in sequence:
        num = int(num_str)
        if (num in count_dict):
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    sorted_counts = dict(sorted(count_dict.items()))
    result_dict = dict(sorted_counts)

    return result_dict

sequence = "0156294826510561"
result = count_it(sequence)
print(result)
