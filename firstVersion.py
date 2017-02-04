newString ='arash'

result=[]

for i in newString:
    for j in newString:
        if i != j:
            for k in newString:
                if k != i and k != j:
                    result.append(i+j+k)
           
                    
print(result)
