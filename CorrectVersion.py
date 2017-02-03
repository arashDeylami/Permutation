# Permutation

def permutation(newString):
        if len(newString) == 1:
                return newString
        else:
                result = []
                for i in newString:
                        eleminatedString = newString.replace(i,'',1)
                        for j in permutation(eleminatedString):
                                result.append(i+j)
        return result
    
    

