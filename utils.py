def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


myDict = {0:"",1:"one", 2:"two", 3:"three", 4:"four", 5: "five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
          10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
myDict2 = {0:"",2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}


def numToString(num):
    if(num<20):
        return(myDict[num])
    elif(20<=num<100):
        return(myDict2[num//10]) +" "+numToString(num%10)
    elif(100<=num<1000):
        return(myDict[num//100] +" hundred "+ numToString(num%100))
    elif(1000<=num<1000000):
        return(numToString(num//1000) +" thousand " + numToString(num%1000))
