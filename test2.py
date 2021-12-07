from collections import Counter
import sys
def top_words():    
    text = input("Write here: ").split()

    top = []
    box = Counter(text).most_common(3)
    top.append(box)

    a = 0
    b = 1 
    result = 0

    while a <= 2:
        box_number = top[0][a][b]
        if box_number >= 2:
            result += 1
        else: 
            print("' '")
            sys.exit(0)
    
        a+= 1
    if result == 3:
        print(top)

top_words()