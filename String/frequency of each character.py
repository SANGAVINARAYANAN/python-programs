text=input()
freq=""
for ch in text:
    if ch not in freq:
        count=0
        for i in text:
             if ch==i:
                 count+=1
                 freq+=ch
        print(ch,"=",count)
        
