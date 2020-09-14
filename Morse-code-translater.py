"""
Additional Contribution: Shubhankar31 (using string.split() concept)
"""

morse_dict = { 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

# sentence1 = "HELLO HELLO2"
# sentence2 = ".... . .-.. .-.. ---   .... . .-.. .-.. --- ..---"
# sentence_c = "···· · −·−−   ·−−− ··− −·· ·"
def eng_to_morse(s):
    a = ""
    s2 = s.upper()
    for i in s2:
        if i == " ":
            a += "  "
        elif i != " ":
            a += morse_dict[i] + " "
    return a[:-1]


def morse_to_eng(s):
    s2 = s.split("   ")
    a = ""
    for word in s2:
        ch = word.split(" ")
        for i in ch:
            for x, y in morse_dict.items():
                if y == i:
                    a += x
        a += " "
    return a[:-1]


def main():
    q1 = input("""
              Type the option No. and press Enter-
              1: eng_to_morse
              2: morse_to_eng
              """)
    q2 = input("Enter the code here: ")
    if q1 == "1":
        print(eng_to_morse(q2))
    elif q1 == "2":
        print(morse_to_eng(q2))
    else:
        print("You have entered something wrong!!!")


main()


# To interchange the keys and values in a python dictionary
# dict2 = dict(zip(dict1.values(), dict1.keys()))
