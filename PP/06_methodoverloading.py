class Num:
    def sum(self,a=4,c=3,b=3):
        print('Sum=',a+b+c)
n=Num()
n.sum() # 10
n.sum(2,1) # 6  , a=2 , b=1 and by default c value is 3
n.sum(5,6,7) # 18  , a=5 , b=6 and c=7
n.sum(a=2,b=8,c=9) # 19
''' Note: the line numbers 6,7 and 8 are called as method overloading '''

