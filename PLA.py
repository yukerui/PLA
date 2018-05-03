W = [0,0,0,0]
def creatData():     #读取数据
    with open('C:\\Users\\lovexl\\Desktop\\hw1_15_train.dat','r') as f:
        data = f.readlines()
        trainDataList = processData(data)            #训练数据
        return trainDataList

def processData(lines):                              #将读取的字符串转化成float形式
    dataList=[]
    for line in lines:
        dataLine = line.strip().split()              #按空格切分字符串
        dataLine = [float(data) for data in dataLine]    #字符串转化为Float
        dataList.append(dataLine)


    return dataList

def sign(W,dataList):                                  #定义sign函数，并让sign(0)=-1
    sum = 0
    for j in range(len(W)):
        sum += dataList[j]*W[j]
    if sum>0:
        return 1
    else:
        return -1

def renewW(W,trainData):                                #更新W
    count =0
    while True:
        iscomplete = True
        for i in range(0,len(trainData)):
            signResult = sign(W, trainData[i])        #对数据的每一项都进行计算
            if signResult  == trainData[i][-1]:
                continue
            else:
                iscomplete =False
                for k in range(len(W)):
                    W[k] = W[k] + trainData[i][-1]*trainData[i][k]         #如果与数据中的y不同，则更新W，并将count+1
                    count+=1
        if iscomplete:
            break
        print("count is",count)
#        print(W)
        return W

renewW(W,creatData())











