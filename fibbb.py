listf = [0, 1]


for x in range(1, 21):
    
    
    listf.append((listf[x]) + (listf[x - 1]))
    print(listf);