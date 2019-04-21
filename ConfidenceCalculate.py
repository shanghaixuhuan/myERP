
class ConfidenceCalculate():
    def verifyExist(self,x,array):
        for i in range(len(array)):
            if(x == array[i]):
                return True
        return False

    def readFile(self,itemCount):
        f = open('./data/record.DAT','r')
        f1 = f.read().split('\n')
        recordCount = len(f1)
        for i in range(recordCount):
            f1[i] = f1[i].split(',')
        y = []
        for i in range(itemCount):
            x = []
            for j in range(itemCount):
                if(i+1<10):
                    i1 = '0' + str(i+1)
                else:
                    i1 = str(i+1)
                if(j+1<10):
                    j1 = '0' + str(j+1)
                else:
                    j1 = str(j+1)
                w = 0
                for k in range(recordCount):
                    if(self.verifyExist(i1,f1[k]) == True and self.verifyExist(j1,f1[k]) == True):
                        w = w + 1
                c = float(w)/recordCount
                oc = [j1,c]
                x.append(oc)
            y.append(x)

        s = []
        for i in range(len(y)):
            t = []
            if (i < 9):
                iw = '0' + str(i + 1)
            else:
                iw = str(i + 1)
            for m in range(3):
                max = 0
                flag = 0
                for j in range(len(y[i])):
                    if(y[i][j][0] == iw):
                        continue
                    elif(y[i][j][1] > max):
                        max = y[i][j][1]
                        flag = j
                t.append(y[i][flag][0])
                y[i][flag][1] = -1
            s.append(t)
        return s


if __name__ == "__main__":
    cc = ConfidenceCalculate()
    s = cc.readFile(15)
    print(s)