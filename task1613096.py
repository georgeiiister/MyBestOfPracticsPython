words = ('hello', 'it', 'is', 'language', 'python') #collection of words

result= dict()

for word in words:
    for j, a in enumerate(word):
        result.setdefault(a,dict())
        positions = result.get(a)
        positions.setdefault(j,0)
        positions[j] = positions[j]+1

mx = max(map(lambda i: max(i[1].keys()), result.items()))

for alpha, positions in result.items():
    lst = [0]
    if mx>0:
        lst *= mx+1
    for index, count in positions.items():
        lst[index] = count
    result[alpha] = tuple(lst.copy())

for i in sorted(result):
    print(i,':', result[i])