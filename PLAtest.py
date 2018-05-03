W= [0,0,0,0]
def data():
    with open('C:\\Users\\lovexl\\Desktop\\hw1_15_train.dat', 'r') as f:
        data = f.readlines()
#    trainDataList = processData(data)  # 训练数据
        dataList=[]
        for dataLine in data:
            line = dataLine.strip().split()  # 按空格切分字符串
            line = [float(data) for data in line]  # 字符串转化为Int
            dataList.append(line)
        count = 0
        while True:
            isComplete=True
            for i in range(len(dataList)):
                for j in range(len(W)):
                    if sign(W,dataList[i])==dataList[i][-1]:
                        continue
                    else:
                        W[j] = W[j] + dataList[i][-1] * dataList[i][j]
                        isComplete=False



def sign(W,dataList):    #定义sign函数，并让sign(0)=-1
    sum = 0
 #   for i in range(len(dataList)):
    for j in range(len(W)):
        sum += dataList[j]*W[j]
    if sum>0:
        return 1
    else:
        return -1

data()