import time

def extractor(directory):
    file = open(directory, "r")
    content = file.read()
    file.close()
    list = content.split('\n')
    return list

def program(D, n):
    start = time.time() 
    r=0
    p=0
    for x,y in enumerate(D):
        if(y == n):
            p=x
            r = int(round(time.time() * 1000 - start))
            break
        else:
            p=-1
            r = int(round(time.time() * 1000 - start))
    return str(p) +" "+str(r)

D = extractor('data/dataset-1-a.csv')
output = open('result.csv', 'w')
for i in range(3):
    n = input('Digite o número que deseja encontrar:')
    output.write(str(program(D, n)+ '\n'))
output.close()