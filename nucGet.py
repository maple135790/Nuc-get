import os
import sys
from time import strftime
import re

def getNuc(file,start,end):
    return file[start:end]

def posDictCreate(posFilename):
    fSearchRange =500
    bSearchRange =2500
    posDict =dict()
    with open(posFilename,"r") as pfr:
        k =pfr.read()
        k =k.splitlines()
        for i in range(len(k)):
            m =k[i].split(",")[1:3]
            posDict[int(m[0])-bSearchRange] =int(m[1])+fSearchRange
    return posDict

def rlpsFileGenerate(st1,ed1,st2,ed2,rlpsType):
    
    rlpsFileName ="rlpsInfo "+strftime("%Y%m%d-%H%M%S")+".txt"
    with open(rlpsFileName,"a") as rfw:
        rfw.write(rlpsType+": "+str(st1+bSearchRange)+", "+str(ed1-fSearchRange)+" :: "+str(st2+bSearchRange)+", "+str(ed2-fSearchRange)+"\n")

def rlpsDetect(pdict):
    sortDict =dict()
    for start,end in sorted(pdict.items()):
        sortDict[start] =end

    key =list(sortDict)
    for i in range(len(key)):
        if i ==len(key)-1:
            break
        start =key[i]
        nextStart =key[i+1]
        if sortDict[start] <=nextStart:   #Case1 No rlps
            # print("No rlps")
            pass
        elif start <= nextStart <= sortDict[start]: #Case2 Head rlps
            rlpsType ="HeadRlps"
            rlpsFileGenerate(start,sortDict[start],nextStart,sortDict[nextStart],rlpsType)
            # print("------------------------------------")
            # print("start: "+str(start)+" end: "+str(sortDict[start]))
            # print("start: "+str(nextStart)+" end: "+str(sortDict[nextStart]))
            # print("Head rlps")
            # print("------------------------------------\n")
            pass
        elif start <= sortDict[nextStart] <= sortDict[start]:   #Case3 Seq. rlps
            rlpsType ="SeqRlps"
            rlpsFileGenerate(start,sortDict[start],nextStart,sortDict[nextStart],rlpsType)
            # print("------------------------------------")
            # print("start: "+str(start)+" end: "+str(sortDict[start]))
            # print("start: "+str(nextStart)+" end: "+str(sortDict[nextStart]))
            # print("Seq. rlps")
            # print("------------------------------------\n")
            pass

    # for start in sortDict:
    #     for nextStart in sortDicti:
    #         if start < nextStart:
    #             if sortDict[start] <=nextStart:   #Case1 No rlps
    #                 print("a")
    #             elif start <= nextStart <= sortDict[start]: #Case2 Head rlps
    #                 print("a")
    #             elif start <= sortDict[nextStart] <= sortDict[start]:   #Case3 Seq. rlps
    #                 print("a")
    #             break
    #         if start != nextStart:
    #             break


    
# def desFileConvert():
# 
#     if os.path.exist("dfA.bin"):
#         return
    
    # with open(desFile,"r") as f:
    #     k =f.read()
        
if __name__ == "__main__":
    srcFile ="aa.fa"
    posFile ="pos.txt"
    fSearchRange =500
    bSearchRange =2500
    posDict =posDictCreate(posFile)
    # counterDict ={"A":0,"T":0,"C":0,"G":0}

    with open(srcFile,"r") as sfr:
        storeList =list()
        k =sfr.read()
        rlpsDetect(posDict)
        # for start,end in posDict.items():
        #     sat =getNuc(k,start,end)
        #     exd =0
        #     for i in sat :
        #         if i =='\n':
        #             exd +=1
        #         else:
        #             pass
        #     for i in range(end+1,end+exd+1):
        #         if sat[end:i] =='\n':
        #             exd +=1
        #         else:
        #             pass
        #     sat =getNuc(k,start,end+exd)
        #     sat =sat.replace('\n','')
        #     storeList.append(sat)
        # for sat in storeList :
        #     for word in sat :
        #         counterDict[word] +=1
        #     MSN =max(counterDict.keys())
        #     b_sat =bytearray(len(sat))
        #     fillPos =[m.start() for m in re.finditer(MSN, sat)]
        #     for i in fillPos:
        #         b_sat[i] =1
        #     print(b_sat)
        

