def getNuc(file,start,end):
    return file[start:end]

if __name__ == "__main__":
    pos =dict()
    with open("aa.fa","r") as fr:
        k =fr.read()
        sat =getNuc(k,10,15)
    print(sat)