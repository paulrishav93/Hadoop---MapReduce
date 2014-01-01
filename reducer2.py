# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", maxSale
        oldKey = thisKey;
        maxSale = -1

    if float(thisSale) > maxSale:
        maxSale = float(thisSale)

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", maxSale
