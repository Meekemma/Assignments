#fibonacci series generator
def fibonnacci():
    a=0
    b=1
    for i in range(20):
        print(b)
        a,b= b,a+b
obj = fibonnacci()        