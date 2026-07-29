n=input()
count=0
for ch in n:
    if ch in "aeiouAEIOU":
        count=count+1
print(count)
