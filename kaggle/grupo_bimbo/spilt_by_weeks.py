import csv
fout = open('train_9.csv', 'wb')
wr = csv.writer(fout, quoting=csv.QUOTE_ALL)
with open('train.csv','r') as fin:
    writer = csv.writer(fout, delimiter=' ')            
    for row in csv.reader(fin, delimiter=' '):
        if row[0] == '9':
             writer.writerow(row)
