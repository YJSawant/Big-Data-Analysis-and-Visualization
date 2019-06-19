from collections import defaultdict
dictionary=defaultdict(int)
with open('output/part-00000.txt','r') as f:
        for line in f:
            temp=line.split('\t')
            dictionary[temp[0]]=int(temp[1])
counter=0

newfile=open('top10_WcCommonCrawl.txt','w')
for w in sorted(dictionary, key=dictionary.get, reverse=True):
  if counter==50:
      break
  temp=w+'\t'+str(dictionary[w])
  print(temp)
  newfile.write(temp+'\n')
  counter+=1
