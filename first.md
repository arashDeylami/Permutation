# Permutation

newString =[‘a’ ,  ‘r’ ,  ’a’ , ’s’ , ’h’]

def factor (n):
	result = 1
	for j in range(n):
		result = result * j
	return result 

for i in range(len(newString)):
	numS = (factor(len(newString))/factor(len(newString)-i))
	result = []
	for i  in range (n):
		for j in range(n):
			if i not j:
				reslut.append(i)
				reslut.append(j)	
				return result
