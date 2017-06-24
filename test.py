#! /usr/bin/env python
# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import json

word_kind = []
# 读入部分!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
positive_emotion = []
negative_emotion = []
extreme = []
very = []
more = []
alittlebit = []
insufficiently = []
over = []
d = open("test/positive-emotion.txt")
n = open("test/negative-emotion.txt")
e = open("test/extreme-6.txt")
v = open("test/very-5.txt")
m = open("test/more-4.txt")
a = open("test/alittlebit-3.txt")
i = open("test/insufficiently-2.txt")
o = open("test/over-1.txt")
no = ['不']
f = open("out.txt")
for line in d.readlines():
    print line
    positive_emotion.append(line[:-3])
for line in n.readlines():
    negative_emotion.append(line[:-3])
for line in e.readlines():
    extreme.append(line[:-3])
for line in v.readlines():
    very.append(line[:-3])
for line in m.readlines():
    more.append(line[:-3])
for line in a.readlines():
    alittlebit.append(line[:-3])
for line in i.readlines():
    insufficiently.append(line[:-3])
for line in o.readlines():
    over.append(line[:-3])
# 识别部分!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for line in f.readlines():
    line = line.split(",")
    for word in line:

        if word in positive_emotion:
            word_kind.append([word, 7])
        # 7号为积极情绪
        elif word in negative_emotion:
            word_kind.append([word, 8])
            # 8号为消极情绪
        elif word in extreme:
            word_kind.append([word, 6])
            # 6 extreme
        elif word in very:
            word_kind.append([word, 5])
            # 5 very
        elif word in more:
            word_kind.append([word, 4])
            # 4 more
        elif word in alittlebit:
            word_kind.append([word, 3])
            # 3 alittlebit
        elif word in insufficiently:
            word_kind.append([word, 2])
            # 2 insufficiently
        elif word in over:
            word_kind.append([word, 1])
            # 1 over
        elif word in ['!']:
            word_kind.append([word, 9])
            # 9 !
        elif word in no:
            word_kind.append([word, 10])
            # 10 no!
        else:
            word_kind.append([word, 0])
    # 单句总结部分!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    emotion_value = 0
    not_num = 0
    emotion_times = 1
    for ii in range(0, len(word_kind) - 1):
        # 程度词权值计算
        if word_kind[ii][1] == 6:
            emotion_times = emotion_times + 3
        elif word_kind[ii][1] == 5:
            emotion_times = emotion_times + 2.5
        elif word_kind[ii][1] == 4:
            emotion_times = emotion_times + 2
        elif word_kind[ii][1] == 3:
            emotion_times = emotion_times + 1
        elif word_kind[ii][1] == 2:
            emotion_times = emotion_times - 0.5
        elif word_kind[ii][1] == 1:
            emotion_times = emotion_times - 1
        # 否定词否定权值计算
        elif word_kind[ii][1] == 10:
            not_num = not_num + 1
        # 情感词标记
        elif word_kind[ii][1] == 7:
            emotion_value = emotion_value + 1 * (-1) ** not_num * emotion_times
            not_num = 0
            emotion_times = 1
        elif word_kind[ii][1] == 8:
            not_num = not_num + 1
            emotion_value = emotion_value + 1 * (-1) ** not_num * emotion_times
            not_num = 0
            emotion_times = 1
        # 叹号处理
        elif word_kind[ii][1] == 9:
            if emotion_value > 0:
                emotion_value = emotion_value + 2
            else:
                emotion_value = emotion_value - 2

    print emotion_value


