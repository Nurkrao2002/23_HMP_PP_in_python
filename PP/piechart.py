from matplotlib import colors
import matplotlib.pyplot as plt
slices=[50,20,15,15]
depts=['Sales','Production','HR','Finance']
cols=['maroon','magenta','blue','pink']
plt.pie(slices,labels=depts,colors=cols,startangle=90,shadow=True,explode=(0,0,0.3,0),autopct='%.2f%%')
plt.title('Josh')
plt.show()