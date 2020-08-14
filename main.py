def extractor(directory):
    file = open(directory, "r")
    content = file.read()
    file.close()
    list = content.split('\n')
    return list

print(extractor('data/dataset-1-a.csv'))