# squares = []
# for i in range(6):
#     squares.append(i*i)

# print(squares)

#same
# sq=[i*i for i in range(6)]  --->list comprehension
# print(sq)




# odd number-->list comprehensions
# sq=[i*i for i in range(6) if i%2 !=0]
# print(sq)




## [-2,-4,3,5,2,-1]----->[0,0,3,5,2,0]
# nums=[-2,-4,3,5,2,-1]

# nums=[0 if val<0 else val for val in nums]
# print(nums)




words=["python", "apple", "apnacollege"]
# print(words[0].upper())
words = [val.upper() for val in words]
print(words)















