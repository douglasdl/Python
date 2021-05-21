# callback
def double(x):
    print(x,' double is ', x*2)
def triple(x):
    print(x, ' triple is ', x*3)

def someAction(i,cb):
    cb(i)

someAction(5,double)     # 5 double is 10

someAction(3,triple)     # 3 triple is 9