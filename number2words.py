fristDitgit = {'0': '', '1': 'یک', '2': 'دو', '3': 'سه', '4': 'چهار', '5': 'پنج', '6': 'شش', '7': 'هفت',
               '8': 'هشت', '9': 'نه'}
secondDigit = {'10': 'ده', '11': 'یازده', '12': 'دوازده', '13': 'شیزده', '14': 'چهارده', '15': 'پانزده',
               '16': 'شانزده', '17': 'هفت ده', '18': 'هیجده', '19': 'نوزده', '2': 'بیست',
               '3': 'سی', '4': 'چهل', '5': 'پنجاه', '6': 'شصت', '7': 'هفتاد', '8': 'هشتاد',
               '9': 'نود', '0': ''}
thirdDigit = {'1': ' صد', '2': 'دویست', '3': 'سی  صد', '4': 'چهار  صد',
              '5': 'پنج  صد', '6': 'شش  صد', '7': 'هفتصد', '8': 'هشتصد',
              '9': 'نه  صد', '0': ''}
unitlist = ['تیلیارد', 'میلیارد', 'میلیون', 'هزار']


def two_digits(x) -> str:
    if x[0] == '0':
        return fristDitgit[x[1]]
    if len(x) == 2 and x[0] == '1':
        return secondDigit[x]
    if len(x) == 2 and x[1] == '0':
        return secondDigit[x[0]]
    if len(x) == 2:
        return f'{secondDigit[x[0]]}و{fristDitgit[x[1]]}'

def three_digits(x: str) -> list[str]:
    if x == '0':
        return ['zero']
    if len(x) == 1:
        return [fristDitgit[x]]
    if len(x) == 2:
        return [two_digits(x)]
    if len(x) == 3 and x[-2:] == '00':
        return [thirdDigit[x[0]]]
    else:
        return [thirdDigit[x[0]]] + [two_digits(x[1:])]

def add_unit(x) -> str:
    word_list = three_digits(x[-1])
    if len(x) > 1:
        for i in range(-2, -len(x) - 1, -1):
            if x[i] == '000':
                continue
            word_list = three_digits(x[i])+ [unitlist[i + 1]] + ["و"]+ word_list
    while True:
        if '' in word_list:
            word_list.remove('')
            continue
        break
    word = ' '.join(word_list)
    return word

def number2words(x:int) -> str:
    x = str(x)
    number_clusters = []
    n = len(x)
    for i in range(1, len(x) + 1):
        if -len(x) - 3 >= -3 * i:
            break
        number_clusters.insert(0, x[-3 * i: n])
        n = -3 * i
    return add_unit(number_clusters)





