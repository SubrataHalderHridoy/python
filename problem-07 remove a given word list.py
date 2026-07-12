

def remove(l, word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))

    return n        
    
l=["Harry", "Subrata", "Rohan", "an"]

print(remove(l, "an"))
