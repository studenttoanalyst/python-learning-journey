# Exploded Pie Chart
# Q: Create a pie chart that explodes one slice.
Labels= ['A', 'B', 'C']
Sizes= [50, 30, 20]
explode = (0.1,0,0)
import matplotlib.pyplot as ptl
ptl.pie(Sizes,labels=Labels,autopct="%1.1f%%",explode=explode)
ptl.title("Explode")
ptl.show()