"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    freq_dict = {}
    if text == '' or text is None:
        return freq_dict
    text = str(text)
    text1 = text.lower()
    for i in text1:
        if not i.isalpha():
            text1 = text1.replace(i, ' ')
    text_new = text1.split()
    for word in text_new:
        if word.isalpha() and word not in freq_dict.keys():
            dict_key = word
            dict_value = text_new.count(word)
            new_dict = {dict_key: dict_value}
            freq_dict.update(new_dict)
    return freq_dict
    print(calculate_frequences(text))


def filter_stop_words(freq_dict, stop_words: tuple) -> dict:
    filter_dict = {}
    if freq_dict is not None and stop_words is not None:
        for key, value in freq_dict.items():
            if key == str(key):
                if key not in stop_words:
                    filter_dict.update({key: value})
    return filter_dict
    print(filter_stop_words(freq_dict, stop_words))


def get_top_n(filter_dict, number: int) -> tuple:
    if number <= 0:
      return()
    new_list = sorted(filter_dict, key=filter_dict.get, reverse=True)
    print(new_list)
    return tuple(new_list[:number])
    print(get_top_n(filter_dict, number))
