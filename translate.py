from code import morse_dict

def translate(text):
    res = ""
    for i in text.lower():
        if i in morse_dict:
            res += morse_dict[i]
        elif i == ' ':
            res += '/'
    return res

print(translate('hola'))
