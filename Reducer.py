#! /usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json

positive = 0
negative = 0

for line in sys.stdin:
    #for line in open("data.txt").readlines():
        line = line.strip()
        line = line.replace(" ","")
        line = line.split(",")
        #单句总结部分!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        emotion_value=0
        not_num=0
        emotion_times=1
        for word in line:
            if word == "6":
                emotion_times=emotion_times+3
                elif word== "5":
                    emotion_times=emotion_times+2.5
                elif word=="4":
                    emotion_times=emotion_times+2
                elif word=="3":
                    emotion_times=emotion_times+1
                elif word=="2":
                    emotion_times=emotion_times-0.5
                elif word=="1":
                    emotion_times=emotion_times-1
                elif word=="10":
                    not_num=not_num+1
                elif word== "7":
                    emotion_value=emotion_value+1*((-1)**not_num)*emotion_times
                    not_num=0
                    emotion_times=1
                elif word=="8":
                    not_num=not_num+1
                    emotion_value=emotion_value+1*((-1)**not_num)*emotion_times
                    not_num=0
                    emotion_times=1
                elif word=="9":
                    if emotion_value>0:
                        emotion_value=emotion_value+2
                    else:
                        emotion_value=emotion_value-2
        print emotion_value
        if emotion_value<0:
            negative += 1
        else:
            positive +=1

print "positive number: "+str(positive)
print "negative number: "+str(negative)
