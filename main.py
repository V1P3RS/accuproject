import csv
import collections

file = open('data.csv')

csvreader=csv.reader(file)

curset=set()
lis =[]

for eid,fid in csvreader:
    try:
        if (eid,fid) in curset:
            raise Exception("Bad dataset")
        else:
            curset.add((eid,fid))
            lis.append(fid)
    except Exception as e:
        print(e)
        exit(0)


counts = collections.Counter(lis)
new_list = sorted(set(lis), key=counts.get, reverse=True)
print(new_list)
