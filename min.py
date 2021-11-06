A = [3,4,2,1,0,8,9,-1,100,0]
print(A)
min = A.pop()
max = min
print(min)
print(max)

indexMin = len(A)
indexMax = len(A)

while A:
    print(A)
    a = A.pop()
    print(min)
    print(max)
    print(indexMin)
    print(indexMax)
    if a < min:
        min = a
        indexMin = len(A)
    if a > max:
        max = a
        indexMax = len(A)



