lst=[]
for i in range(10):
    num = int(input()) % 42
    lst.append(num)
    
result = set(lst)    
print(len(result))