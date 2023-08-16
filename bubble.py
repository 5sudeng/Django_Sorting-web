alist = [2,9,3,7]

size = len(alist)

for i in range(size-1) :
    if alist[i] > alist[i+1] :
        alist[i], alist[i+1] = alist[i+1], alist[i]

print(alist)