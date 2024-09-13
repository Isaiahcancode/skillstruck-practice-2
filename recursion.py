this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']

def feeding(this_list):
    if len(this_list) == 1:
        this_list = [0]

    else:
        mid = len(this_list) // 2
        first_half = this_list[:mid]
        second_half = this_list[mid:]


feeding(this_list)