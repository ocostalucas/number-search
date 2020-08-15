import time

def extractor(filename):
    archive = open(filename, "r")
    data = archive.read().split('\n')[:-1]
    archive.close()
    return data

def output(filename,found, position, time):
    archive = open('resposta-'+filename+'.txt','w')
    archive.write(found)
    archive.write(position)
    archive.write(time)
    archive.close() 


def program(filename):
    start = time.time()
    content = extractor(filename+'.csv') 
    n=content[0]
    t=int(content[1])
    D=content[2:]
    for i in range(t):
        if D[i] == n:
            r=str(time.time() * 1000 - start)
            output(filename, 'TRUE\n', str(i)+'\n', r)
            return True
    r=str(time.time() * 1000 - start)
    output(filename, 'FALSE\n', '-1\n', r)
    return False
    
program('dataset-1-a')
program('dataset-1-b')
program('dataset-1-c')