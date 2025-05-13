import re, requests

#######
# utils
######
def is_valid_daf_no(string):
    return bool(re.fullmatch('[1-9][0-9]*[ab]', string))


def get_num(string):
    return int(string[:len(string)-1])


def get_let(string):
    return string[-1]


#######
# i/o
######
def get_daf_input(prompt, min_num, min_let, max_num, max_let):
    while True:
        daf = input(prompt)
        if is_valid_daf_no(daf):
            # make sure it meets the bounds
            return first_daf


def get_daf_file(number, letter):
    request = f'https://www.dafyomi.org/edafnew/Shabbos/{number}{letter}.jpg' 
    # print(request)
    res = requests.get(request)
    with open(f'Shabbos-{number}{letter}.jpg', 'wb') as f:
        f.write(res.content)


#######
# main
#####
def main():
    # get masechet using autocomplete?

    '''
    replace the two while trues with calls to get_daf_input()
    '''
    while True:
        first_daf = input('enter the first daf (e.g. 103b): ')
        if is_valid_daf_no(first_daf):
            # make sure it's at least min (2?)
            # make sure it's not out-of-upper-bounds
            break
    while True:
        last_daf = input('enter the last daf (e.g. 116a): ')
        if is_valid_daf_no(last_daf): 
            # make sure it's greater than first
            # make sure it's not out-of-upper-bounds
            break

    daf_no = get_num(first_daf)
    last_no = get_num(last_daf)

    if get_let(first_daf) == 'b':
        get_daf_file(daf_no, 'b')
        # print(first_daf)
        daf_no += 1

    for i in range(daf_no, last_no + 1):
        get_daf_file(i, 'a')
        # print(f'{i}a')
        if i == last_no and get_let(last_daf) == 'a':
            break
        get_daf_file(i, 'b')
        # print(f'{i}b')


if __name__ == '__main__':
    main()
