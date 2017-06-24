#encoding=utf-8
import jieba
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
f = open('realdata.txt')
line = f.readline()
f_out = open('input.txt','w+')
count = 0;
while line:
    seg_list = jieba.cut(line, cut_all=False)
    f_out.write(str(",".join(seg_list)))
    if count%10000 == 0:
        print str(count/10000)+"%"
    count += 1
    line = f.readline()
