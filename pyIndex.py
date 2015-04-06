import string
def revIndex (FileIn):
    '''Creates an index of words from input file and writes them to output in reverse order.'''
    InF = open(FileIn, 'r')
    store = []
    readMe = InF.read()
    listFile = readMe.split()
    InF.close()
    for word in listFile:
        if word not in store:
            store.append(word)
            revStore = store[::-1]
            revS1 = map(str.strip, revStore)
            #revStri = str(revS1)
            #newStore = "".join(revS1)
            #revCap = revStore.lower()
            #newStore.split('\n')
            #newStore.split()
            #newStore.strip(",")
            #newStore.strip(".")
            revPrnt = ( '\n'.join(revS1))
            #print(revPrnt )
            OutF = open('output.txt', 'w')
            OutF.writelines(revPrnt)
            #OutF.strip(",")
           # OutF.strip(".")
           # OutF.lower()
            #print(OutF)
            #OutF.writelines(newStore + '\n')
            OutF.close()
            with open('output.txt', 'r') as fileinput:
                for line in fileinput:
                    line = line.lower()
                    print(fileinput)     
            
             

print(revIndex('indexer.txt'))
