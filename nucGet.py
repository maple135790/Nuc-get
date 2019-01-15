def getNuc(file,start,end):
    return file[start:end]

def posDictCreate(posFilename):
    with open(posFilename,"r") as pfr:
        k =pfr.read()
        k =k.splitlines()
        for i in range(len(k)):
            m =k[i].split(",")[1:3]
            posDict[m[0]] =m[1]
    return posDict

if __name__ == "__main__":
    posDict =dict()
    srcFile ="aa.fa"
    posFile ="pos.txt"
    posDict =posDictCreate(posFile)

    with open(srcFile,"r") as sfr:
        k =sfr.read()
        for start,end in posDict.items():
            sat =getNuc(k,int(start),int(end))
            print(sat)