# utils.py

def enough_spaces(data: str):
    """
    Checks whether data contain enough spaces.

    :param data: string data
    :return: True if there are more than 3 spaces
    """
    return data.count(' ') > 3


def no_numbers(data: str):
    """
    Checks whether data contain numbers.

    :param data: text line to be checked
    :return: True if the line does not contain any numbers
    """
    numbers = "0123456789"
    for c in data:
        if c in numbers:
            return False
    return True


def no_special_chars(data):
    """
    Checks whether data contain special chars.

    :param data: string to be checked
    :return: True if the data does not contain any special chars
    """
    special_chars = "~`!@#$%^&*()_-+={}[]:>;',</?*-+©|"
    for c in data:
        if c in special_chars:
            return False
    return True


def remove_special_chars(sentence):
    """
    Removes the special characters.

    :param sentence: text to be modified
    :return: modified data
    """
    filtered = sentence.strip().replace('\'', '').replace('"', '').replace('”', '')
    filtered = filtered.replace('–', '').replace('“', '').replace('  ', ' ')
    return filtered.lower()


def filter_trash(fname):
    """
    Removes special chars.

    :param fname: path to the file which will be filtered
    """
    with open(fname, 'r') as f:
        for line in f:
            for sentence in line.split('.'):
                content = remove_special_chars(sentence)
                if (len(content) > 0 and no_special_chars(content) and enough_spaces(content)
                    and no_numbers(content)):
                    print(content)