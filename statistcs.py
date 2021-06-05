https://replit.com/@hariviratmuthya/boilerplate-mean-variance-standard-deviation-calculator-3#mean_var_std.py
  
import numpy as np
import pandas as pd
class calculate:
    def __init__(self,list,axis):
        self.list=list
        self.axis=axis
    def calc(x):
        l=np.array(x.list)
        if l.size ==9:
            m=np.array([l[0:3],l[3:6],l[6:9]])
            mean=m.mean(x.axis)
            var=m.var(x.axis)
            std=m.std(x.axis)
            max=m.max(x.axis)
            min=m.min(x.axis)
            sum=m.sum(x.axis)
            return mean, var, std, max, min, sum
        else:
            print('ValueError: enter list with 9 elements')
        
c1=calculate([1,2,3,4,5,6,7,8,9],0)
c2=calculate([1,2,3,4,5,6,7,8,9],1)
c3=calculate([1,2,3,4,5,6,7,8,9],None)
df=pd.DataFrame({'Axis=0' : c1.calc(),'Axis=1' : c2.calc(),'Flattened' : c3.calc()})
df.index=['mean:','var:','std:','max:','min:','sum:']
print(df)

