# pattern format: apple-egg-pork

def str_to_set(set_string):
    return set(set_string.split('-'))


def find_subset_string(pattern):
    subset = find_subset(list(pattern))
    # pop origin set
    subset.pop()

    return [
        '-'.join(items)
        for items in subset
        if len(items)
    ]

def find_subset(old_set):
    if len(old_set) == 0:
        return[set]
    elif len(old_set) == 1:
        return [[]] + [old_set]
    else:
        rest = find_subset(old_set[1:])
        a_list = []
        for item in rest:
            b_list = [old_set[0]]
            b_list += item
            a_list.append(b_list)
        return rest + a_list


def find_rules(fp_dict, min_confidence):
    rules = []

    pattern_string_list = fp_dict.keys()

    for pattern_string in fp_dict:
        pattern_set = str_to_set(pattern_string)
        subsets_string = find_subset_string(pattern_set)

        for subset_string in subsets_string:
            if subset_string in pattern_string_list:

                pattern_support = fp_dict[pattern_string]
                subset_support = fp_dict[subset_string]
                confidence = pattern_support / subset_support

                if confidence >= min_confidence:
                    difference_set = str_to_set(pattern_string) - str_to_set(subset_string)
                    rule = '{}->{}'.format(subset_string, '-'.join(difference_set))
                    rules.append([rule,confidence,pattern_support])

    return rules
