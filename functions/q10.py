def even(list):
    lis = []
    for i in list:
        if i%2==0:
            lis.append(i)
    print("even number are : ",lis)    
even([1,2,3,4,5,6])            