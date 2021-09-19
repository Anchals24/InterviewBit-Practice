#Problem Statement : 
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. 
The numbers cannot be 0 prefixed unless they are 0.

"""

def validip( ip):
    ip = ip.split(".")
    for i in ip:
        l = len(i)
        if (l > 3 or int(i) > 255 or int(i) < 0):
            return False
        if (l > 1 and int(i) == 0):
            return False
        if (l > 1 and int(i) != 0 and i[0] == "0"):
            return False
    return True
    
def restoreIpAddresses(A):
    size = len(A)
    if size > 12:
        return []
    news = A 
    Ips = []
    for i in range(1 , size-2):
        for j in range(i+1 , size-1):
            for k in range(j+1 , size):
                news = news[:k] + "." + news[k:]
                news = news[:j] + "." + news[j:]
                news = news[:i] + "." + news[i:]

                if validip(news):
                    Ips.append(news)
                news = A 
        
    Ips.sort()
    return Ips    

restoreIpAddresses(25525511135)

	


