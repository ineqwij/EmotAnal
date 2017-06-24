#! /usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json

word_kind=[]
#读入部分!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
positive_emotion = []
negative_emotion=[]
extreme=[]
very=[]
more=[]
alittlebit=[]
insufficiently=[]
over=[]
no = []

d = open("positive-emotion.txt")
n= open("negative-emotion.txt")
e= open("extreme-6.txt")
v= open("very-5.txt")
m= open("more-4.txt")
a= open("alittlebit-3.txt")
i= open("insufficiently-2.txt")
o= open("over-1.txt")

for line in d.readlines():
    positive_emotion.append(line[:-3])
for line in n.readlines():
    negative_emotion.append(line[:-3])
for line in e.readlines():
    extreme.append(line[:-2])
for line in v.readlines():
    very.append(line[:-2])
for line in m.readlines():
    more.append(line[:-2])
for line in a.readlines():
    alittlebit.append(line[:-2])
for line in i.readlines():
    insufficiently.append(line[:-2])
for line in o.readlines():
    over.append(line[:-2])

#识别部分!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for line in sys.stdin:
    #for line in open("out.txt").readlines():
            print "#",
            line = line.split(",")
            for word in line:
                if word in positive_emotion:
                    print ","+"7",
                #positive
                elif word in negative_emotion:
                    print ","+"8",
                #negative
                elif word in extreme:
                    print ","+"6",
                elif word in very:
                    print ","+"5",
                elif word in more:
                    print ","+"4",
                elif word in alittlebit:
                    print ","+"3",
                elif word in insufficiently:
                    print ","+"2",
                elif word in over:
                    print ","+"1",
                elif word is "!":
                    print ","+"9",
                elif word in no:
                    print ","+"10",
                else:
                    continue
            print ""
