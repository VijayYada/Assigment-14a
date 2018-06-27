#1.f=open('new.txt','r',encoding="utf8")
#content=f.readlines()
#n=int(input("enter number of lines you want to read from last"))
#while n>0:
#print(content[-n])
#n-=1
#f.close()


#2. f=open('new.txt','r',encoding="utf8")
# w=input('enter the word you want to search')
# x=f.read()
# c=0
# for w in x:
# if w==x:
# c=c+1
# print(c)

#from collections import Counter
#def word_count(fname,encoding="utf8"):
#with open(fname,encoding="utf8") as f:
#return Counter(f.read().split())
#print("Frequency of words in the file :",word_count("new.txt",encoding="utf8"))

#3.with open('new.txt','r',encoding="utf8") as f1:
#with open('abc.txt','w',encoding="utf8")as f2:
#for line in f1:

#4.with open('new.txt',encoding="utf8")as f1,open('abc.txt',encoding="utf8")as f2:
#for line1,line2 in zip(f1,f2):
#print(line1+line2)

#5.import random
#f=open('num.txt','w')
#for i in range(10):
#x=str(random.randint(1,50))
#f.write(x)
#f.write("\n")
#print(x)
#f.close()
#f=open('num.txt','r')
#l=f.readlines()
#print(l)
#l.sort()
#print(l)
#with open('abc.txt','w')as f2:      
#for n in l:
#f2.write(n)
#f2.write("\n")
#f.close()
#f2.close()