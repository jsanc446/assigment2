#Juan Sanchez Assignment2

class Assignment2:
    def __init__(self,age=int):
        
    def sayWelcome(self,name):
        self.name=name
        print('Welcome to the assignment',name ,'Havent seen you for',self.age,'years!')
        
    def doubleList(self, theList):
        list=theList
        for x in list:
           
            x=x * 2
            print(x)
        count = 1
        for each in list:
            if count % 2 != 0:
                print(each)
                count+=1
            else:
                count+=1
        count = 1
        for each in list:
            if count % 2 == 0:
                print(each)
                count+=1
            else:
                count+=1
    def modifyString (self,name):
        theName=name
        count = 1
        for x in theName:
            if count%3==0:
                x = x.upper()
                print(x)
                count+=1
            else:
                if count % 4==0 and ord(x) %3 != 0 :
                    x = x.lower()
                    print(x)
                    count+=1
                else:
                        if count %5==0 and (ord(x) %3 != 0 or ord(x) %4 != 0):
                            x=" "
                            print(x)
                            count+=1
                        else:
                            print(x)
                            count+=1
    def isGoodPassword(self, str):
            if(len(str)<9):
                return False
            smalls = 0
            bigs = 0
            spl = 0
            num = 0
            for val in str[0:-1:1]:
                if(val.isnumeric()):
                 num +=1
                elif(val.isupper()):
                    bigs+=1
                elif(val.islower()):
                    smalls+=1
                elif(val==',' or val == '.' or val == '#'):
                    spl += 1
            if(smalls >= 2 or bigs >= 3):
                if(spl >= 2 or num >= 1):
                 return True
            return False
    def connectTcp(self,host,port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,port))            
            print("Connection established correctly")
        except:
            print("Some error")
        





        
