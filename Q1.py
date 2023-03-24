l=list('abcdefghijklmnopqrstuvwxyz')
stri=input("\nEnter your string : ")
string=''
for i in stri:
    a=i.lower()
    if a in l:
        m=str(l.index(a)+1)
        string=string+m+' '
    else:
        continue

print("=============================================================")
print("\nInput : ",stri)
print("Output : ",str(string))
print("\n=============================================================")