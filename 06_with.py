f=open("file.txt")
print(f.read())
f.close()

#tHE same can be wriiten using with statement like this:

with  open("file.txt") as f:
    print(f.read())