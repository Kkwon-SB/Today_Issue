# listlist = [1,2,3,4,5]

# a, b, c, d, e = [i for i in listlist]

# print(a, b, c, d, e,a)
# a,b,c,d,e = '0','0','0','0','0' 
# b = '0' 
# c = '0'
# d = '0'
# e = '0'

f = 0
def ttest():
    global a ,b,c,d,e    
    listlist = ['aaa','bbb','ccc','ddd','eee',]
    a, b, c, d, e = [i for i in listlist]
    f = 'kkkkkkkkkk'
    print(a, b, c, d, e, f)
    
ttest()
print(a, b, c, d, e, f)