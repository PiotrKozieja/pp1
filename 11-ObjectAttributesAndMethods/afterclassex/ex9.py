class arr:
    
    @staticmethod
    def m1(noe, voe):
        arr = []
        for i in range(noe):
            arr.append(voe)
        print(arr)
    def m2(noe,minv,maxv):
        import random
        arr = []
        for i in range(noe):
            x = random.randint(minv,maxv)
            arr.append(x)
        print(arr)
array1 = arr.m2(5,1,10)
    

