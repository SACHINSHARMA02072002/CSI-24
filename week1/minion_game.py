def minion_game(string):
    n = len(string)
    vowels = 0
    cons = 0
    for idx, c in enumerate(string):
        num_substr = n - idx
        if c in 'AEIOU':
            vowels += num_substr
        else:
            cons += num_substr
    if vowels > cons:
        print(f'Kevin {vowels}')
    elif cons > vowels:
        print(f'Stuart {cons}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)