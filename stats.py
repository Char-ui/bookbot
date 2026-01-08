def word_counter(file_text):
    word_ind = file_text.split()
    return f"Found {len(word_ind)} total words"

def character_counter(file_text):
    char_counter = {}
    lower_case_everything = file_text.lower()
    for character in lower_case_everything:
        if character in char_counter:
            char_counter[character] += 1
        else:
            char_counter[character] = 1
    
    return char_counter

def sorted_dic_lists(char_counter):

    def sort_helper(individual_dic):
        return individual_dic["nums"]

    dic_list = []

    for key in char_counter:
        dic = {}
        dic["char"] = key
        value = char_counter[key]
        dic["nums"] = value
        dic_list.append(dic)
    dic_list.sort(reverse=True, key=sort_helper)
    return dic_list