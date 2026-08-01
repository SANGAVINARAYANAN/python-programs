text=input()
digits=0
alphabets=0
special=0
for ch in text:
    if ch.isdigit():
        digits+=1
    elif ch.isalpha():
        alphabets+=1
    else:
        special+=1
print("digits=",digits)
print("alphabets=",alphabets)
print("special=",special)
