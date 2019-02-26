# -*- coding: utf-8 -*-
"""Python Matplotlib

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_hic_fB-rs6WsrQj9SiV6aHPsaBDtiuf

1. Write a Python program to draw a line with suitable label in the x axis, y axis and a title
"""

import matplotlib.pyplot as plt
x = range(1,100)
y = [value*5 for value in x]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show

"""2. Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title"""

import numpy as np

# Prepare the data
x = [1,2,3,4]
y = [11,44,555,1]
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.plot(x,y)

plt.show()

"""3. Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
Test Data:
test.txt
1 2
2 4
3 1
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

with open('textfile.txt') as f:
    data = f.readlines()
print(data[0].split('\n'), type(data))    
    
# data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x,y)
plt.show()

#/home/admin1/Akanksha/PycharmProjects/Machine-Learning-master

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import matplotlib.pyplot as plt
import csv

x = []
y = []

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('housing.csv', index_col=0)
df.plot(x=df.index, y=df.columns)
plt.show()



"""5. Write a Python program to plot two or more lines on same plot with suitable legends of each line."""

import matplotlib.pyplot as plt
# plt.title = ("sine wave form") 
x1 = [1,2,3]
y1 = [4,22,3]
plt.plot(x1,y1,label='line-1')
x2 = [1,2,3]
y2 = [11,22,2]
plt.plot(x2,y2,label='line-2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show

"""6. Write a Python program to plot two or more lines with legends, different widths and colors."""

import numpy as np
import matplotlib.pyplot as plt

# make some data


y1 = [1,22,33]
y2 = [22,1,44]

plt.plot(y1, c='b', label='y1',linewidth=7.0)
plt.plot(y2, c='r', label='y2',linewidth = 3.0)

leg = plt.legend()
plt.show()

"""7. Write a Python program to plot two or more lines with different styles"""

import matplotlib.pyplot as plt
# plt.title = ("sine wave form") 
x1 = [1,2,3]
y1 = [4,22,3]
plt.plot(x1,y1,label='line-1', color = 'green', linewidth = 2.9, linestyle = 'dashed')
x2 = [1,2,3]
y2 = [11,22,2]
plt.plot(x2,y2, label = 'line-2' ,color = 'blue', linewidth = 5.5, linestyle = 'dotted',marker='o')
markers_on = [1,2,3]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()

"""8. Write a Python program to plot two or more lines and set the line markers."""

x1 = [4,22,3]
y1 = [4,22,3]
plt.plot(x1,y1,label='line-1', color = 'green', linewidth = 2.9, marker='o')
x2 = [1,2,3]
y2 = [11,22,2]
plt.plot(x2,y2, label = 'line-2' ,color = 'blue', marker='o')
markers_on = [1,2,3]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()

"""9. Write a Python program to display the current axis limits values and set new axis values."""

x = [1,22,33]
y = [22,1,35 ]
plt.xlabel('a-axis')
plt.ylabel('y-axis')
plt.axis()
plt.plot(x,y,label = 'line-2' ,color = 'blue', marker='o')
plt.axis([0, 100, 0, 200]) 
plt.show()

"""10. Write a Python program to plot quantities which have an x and y position."""

x = [i for i in range(5,10)]
y = [j for j in range(10,15)]
plt.xlabel('a-axis')
plt.ylabel('y-axis')
plt.axis()
plt.scatter(x,y,label = 'line-2' ,color = 'blue', marker='o')
plt.axis([0, 20, 0, 20]) 
plt.show()

"""11. Write a Python program to plot several lines with different format styles in one command using arrays."""

import numpy as np
arr = np.array([(1,2,3),(22,33,44),(44,3,2)])
plt.xlabel('a-axis')
plt.ylabel('y-axis')
plt.axis()
for i in range(len(arr)):
  plt.plot(arr[i],label = 'line-2' ,color = 'blue', marker='o')
plt.show()

"""12. Write a Python program to create multiple types of charts
*italicized text*
"""

x = [i for i in range(5,10)]
y = [j for j in range(10,15)]
x1 = [4,22,3]
y1 = [4,22,3]
plt.xlabel('a-axis')
plt.ylabel('y-axis')
plt.axis()
plt.scatter(x,y,label = 'line-2' ,color = 'blue', marker='o')
plt.plot(x1,y1,label = 'line-2' ,color = 'blue', marker='o')



plt.axis([0, 30, 0, 30]) 
plt.show()

x2 =[3,4,5,6,7]
y2 = [772.559998,776.429993,776.469971,776.859985,775.080017]
plt.xlabel("Date")
plt.ylabel("Day")
plt.plot(x2,y2, linewidth = 0.5,color = 'blue', linestyle = 'dashed')
plt.show()

fig = plt.figure()
fig.subplots_adjust(bottom=0.20, left=0.20, top = 0.800, right=1)

plt.subplot(2,1,2)
plt.xticks(()), plt.yticks(())

plt.subplot(2,3,4)
plt.xticks(()), plt.yticks(())

plt.subplot(3,2,4)
plt.xticks(()), plt.yticks(())

plt.show()

"""1. Write a Python programming to display a bar chart of the popularity of programming Languages. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

"""2. Write a Python programming to display a horizontal bar chart of the popularity of programming Languages. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color = 'pink')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()

"""3. Write a Python programming to display a bar chart of the popularity of programming Languages. Use uniform color. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color = (0.4, 0.6, 0.8, 1.0))
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()

"""4. Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color = ["grey",'yellow','pink','blue','black','purple'])
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()

"""5. Write a Python programming to display a bar chart of the popularity of programming Languages. Attach a text label above each bar displaying its popularity (float value). 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color='pink')
plt.xlabel("Languages")
plt.ylabel("Popularity")

def autolabel(rects):
   
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, 1.05*height,'%f' % float(height),ha='center', va='bottom')
autolabel(rects1)

plt.show()

"""6. Write a Python programming to display a bar chart of the popularity of programming Languages. Make blue border to each bar."""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color = "pink", edgecolor='blue')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()

"""7. Write a Python programming to display a bar chart of the popularity of programming Languages. Specify the position of each bar plot."""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [0.8,1,3,4,6,8]
plt.barh(x_pos, popularity, color = "pink", edgecolor='blue')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()

"""8. Write a Python programming to display a bar chart of the popularity of programming Languages. Select the width of each bar and their positions."""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
width = [0.1,0.22,0.63,0.5,0.7,1]
x_pos = [0.8,1,3,4,6,8]
plt.bar(x_pos, popularity, width=width)
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()

"""9. Write a Python programming to display a bar chart of the popularity of programming Languages. Increase bottom margin."""

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
width = [0.1,0.22,0.63,0.5,0.7,1]
x_pos = [0.8,1,3,4,6,8]
plt.subplots_adjust(bottom=0.4, top=1)

plt.bar(x_pos, popularity, width=width)
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.show()

"""10. Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
Sample Data:
Means (men) = (22, 30, 35, 35, 26)
Means (women) = (25, 32, 30, 35, 29)
"""

import numpy as np
men = [22,30,35,35,26]
women = [25,32,30,35,29]
# plt.bar(x,y)
n = 5
fig, ax = plt.subplots()
index = np.arange(n)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, men, bar_width, alpha=opacity, color='pink', label='Men')

rects2 = plt.bar(index + bar_width, women, bar_width, alpha=opacity, color='purple', label='Women')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()
plt.tight_layout()
plt.show()

"""11. Write a Python program to create bar plot from a DataFrame. 
Sample Data Frame:
a b c d e 
2 4,8,5,7,6
4 2,3,4,2,6
6 4,7,4,7,8
8 2,6,4,8,6
10 2,4,3,3,2
"""

from pandas import DataFrame
import matplotlib.pyplot as plt
a=np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df=DataFrame(a, columns=['a','b','c','d','e'], index=[2,4,6,8,10])

df.plot(kind='bar')

plt.show()

"""12. Write a Python program to create bar plots with error bars on the same figure. Sample Date
Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
"""

mean = [0.2474, 0.1235, 0.1737, 0.1824 ]
standard_deviation = [0.3314, 0.2278, 0.2836, 0.2645]

"""14. Write a Python program to create a stacked bar plot with error bars. 
Note: Use bottom to stack the women?s bars on top of the men?s bars.
Sample Data:
Means (men) = (22, 30, 35, 35, 26)
Means (women) = (25, 32, 30, 35, 29)
Men Standard deviation = (4, 3, 4, 1, 5)
Women Standard deviation = (3, 5, 2, 3, 3)
"""

import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

"""1. Write a Python programming to create a pie chart of the popularity of programming Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

import matplotlib.pyplot as plt
popularity = [22.2,17.6,8.8,8,7.7,6.7]
languages = ['Java','Python', 'PHP', 'JavaScript', 'C#', 'C++']
color = ['red','blue','green','pink','purple','yellow']
plt.pie(popularity, labels = languages, colors = color)
# plt.axis('equal')
plt.show()

"""2. Write a Python programming to create a pie chart with a title of the popularity of programming Languages. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
languages = ['Java','Python', 'PHP', 'JavaScript', 'C#', 'C++']
color = ['red','blue','green','pink','purple','yellow']
plt.pie(popularity, labels = languages, colors = color)
plt.title("The popularity of programming Languages")
plt.show()

"""3. Write a Python programming to create a pie chart with a title of the popularity of programming Languages.Make multiple wedges of the pie. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

import matplotlib.pyplot as plt
plt.figure()
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
languages = ['Java','Python', 'PHP', 'JavaScript', 'C#', 'C++']
explode = (0.1, 0, 0, 0, 0, .1)  
color = ['red','blue','green','pink','purple','yellow']
plt.pie(popularity, labels = languages, colors = color, explode = explode, autopct='%.2f')
plt.title("The popularity of programming Languages")
plt.show()

"""4. Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file. 
Sample data: 
medal.csv
country,gold_medal
United States,46
Great Britain,27
China,26
Russia,19
Germany,17
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import matplotlib.pyplot as plt
import csv



import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('csvfile.csv', header=None)
explode = (0.1, 0, 0, 0, 0)  
color = [ 'purple','pink', 'blue', 'yellow'] 

plt.pie(data[1],labels = data[0], colors = color)
plt.axis('equal')
plt.show()



"""1. Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other."""

import numpy as np
import matplotlib.pyplot as plt
# np.random.seed(19680801)



x = [11,-33,4]
y = [22,55,66]
colors = ['orange','green','red']
area = 100*6  

plt.scatter(x, y,area, c=colors, alpha=0.7)
plt.show()

"""2. Write a Python program to draw a scatter plot with empty circles taking a random distribution in X and Y and plotted against each other."""

x = [11,33,4,1,2,3,4]
y = [22,55,66,4,3,2,1]
# colors = ['orange','green','red']
area = 100*6

plt.scatter(x, y,area,  facecolors='none', edgecolors='blue')
plt.show()

"""3. Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes."""

x = [np.random.randn(60)]
y = [np.random.randn(60)]
# colors = ['orange','green','red']
area = [100 * np.random.randn(60)] 

plt.scatter(x, y,area, c = 'purple', alpha = 0.5)
plt.show()

"""4. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students.
Test Data:
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

math =  [88, 92, 80, 89, 100, 80, 60, 100, 80, 34] 
science =  [35, 79, 79, 48, 100, 88, 32, 45, 20, 30] 
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# colors = ['orange','green','red']

plt.scatter(grades_range, math, color='purple')
plt.scatter(grades_range, science, color='g')
plt.legend(math)
plt.show()

# color = ['blur','purple','orange','green','red','yellow','pink', 'black','grey', 'white']
# plt.scatter(math,science,c=color)
# # plt.scatter([months[-1]],[data[-1]], color=['red'])
# plt.show()

"""5. Write a Python program to draw a scatter plot for three different groups camparing weights and heights."""

h1 = [1,2,3,4]
h2=[2,3,4,1]
h3=[5,4,3,6]
w1=[44,55,66,77]
w2 = [33,44,32,55]
w3 = [33,44,22,11]
weight=np.concatenate((w1,w2,w3)) 
height=np.concatenate((h1,h2,h3))
color = ['purple', 'black']
plt.scatter(weight,height, c = color)
plt.show()

"""6. Write a Python program to draw a scatter plot to find sea level rise in past 100 years."""

rise = [np.random.rand(100)*2]
year = [np.random.rand(100)*0.02]
plt.scatter(rise,year)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
mean_v = [ 0.2474, 0.1235, 0.1737, 0.1824]
sd_v = [0.3314, 0.2278, 0.2836, 0.2645]
# materials = ['v1', 'v2', 'v3', 'v4']
x_pos = np.arange(len(materials))
fig, ax = plt.subplots()
ax.bar(x_pos, mean_v, yerr=sd_v, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
# ax.set_xticklabels(materials)
ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()

"""13. Write a Python program to create bar plots with errorbars on the same figure. Attach a text label above each bar displaying men means (integer value).
Sample Data
Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
"""

import numpy as np
import matplotlib.pyplot as plt
mean_v = [ 0.2474, 0.1235, 0.1737, 0.1824]
sd_v = [0.3314, 0.2278, 0.2836, 0.2645]
x_pos = np.arange(len(materials))

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, mean_v, yerr=sd_v, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
# ax.set_xticklabels(materials)
ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
def autolabel(rects):
   
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, 1.05*height,'%f' % float(height),ha='center', va='bottom')
autolabel(rects1)
plt.show()

"""14. Write a Python program to create a stacked bar plot with error bars. 
Note: Use bottom to stack the women?s bars on top of the men?s bars.
Sample Data:
Means (men) = (22, 30, 35, 35, 26)
Means (women) = (25, 32, 30, 35, 29)
Men Standard deviation = (4, 3, 4, 1, 5)
Women Standard deviation = (3, 5, 2, 3, 3)
"""

import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

"""15. Write a Python program to create a horizontal bar chart with differently ordered colors. 
Note: Use bottom to stack the women?s bars on top of the men?s bars.
Sample Data Set:
languages = [['Language','Science','Math'], 
['Science','Math','Language'],
['Math','Language','Science']]
numbers = [{'Language':75, 'Science':88, 'Math':96},
{'Language':71, 'Science':95, 'Math':92},
{'Language':75, 'Science':90, 'Math':89}]
"""

import numpy as np
import matplotlib.pyplot as plt

num_set = [{'Language':75, 'Science':88, 'Math':96},
           {'Language':71, 'Science':95, 'Math':92},
           {'Language':75, 'Science':90, 'Math':89}]

lan_guage    = [['Language','Science','Math'], 
               ['Science','Math','Language'], 
               ['Math','Language','Science']] 
colors = ["r","g","b"]
names = sorted(num_set[0].keys())
values = np.array([[data[name] for name in order] for data,order in zip(num_set, lan_guage)])
xs = np.insert(np.cumsum(values, axis=1),0,0, axis=1)[:, :-1]
orders = np.array(lan_guage)
bottoms = np.arange(len(lan_guage))

for name, color in zip(names, colors):
	idx = np.where(orders == name)
	value = values[idx]
	left = lefts[idx]
	plt.bar(left=left, height=0.8, width=value, bottom=bottoms, 
	color=color, orientation="horizontal", label=name)
plt.yticks(bottoms+0.4, ["Student-%d" % (t+1) for t in bottoms])
plt.legend(loc="best", bbox_to_anchor=(1.0, 1.00))
plt.subplots_adjust(right=0.75)

plt.show()

"""16. Write a Python program to create stack bar plot and add label to each section. Sample data:
people = ('G1','G2','G3','G4','G5','G6','G7','G8')
segments = 4
# multi-dimensional data 
data = [[ 3.40022085, 7.70632498, 6.4097905, 10.51648577, 7.5330039, 7.1123587, 12.77792868, 3.44773477],
[ 11.24811149, 5.03778215, 6.65808464, 12.32220677, 7.45964195, 6.79685302, 7.24578743, 3.69371847],
[ 3.94253354, 4.74763549, 11.73529246, 4.6465543, 12.9952182, 4.63832778, 11.16849999, 8.56883433],
[ 4.24409799, 12.71746612, 11.3772169, 9.00514257, 10.47084185, 10.97567589, 3.98287652, 8.80552122]]
"""

import numpy as np
import matplotlib.pyplot as plt

people = ('G1','G2','G3','G4','G5','G6','G7','G8')
segments = 4
data = [[ 3.40022085, 7.70632498, 6.4097905, 10.51648577, 7.5330039, 7.1123587, 12.77792868, 3.44773477],
[ 11.24811149, 5.03778215, 6.65808464, 12.32220677, 7.45964195, 6.79685302, 7.24578743, 3.69371847],
[ 3.94253354, 4.74763549, 11.73529246, 4.6465543, 12.9952182, 4.63832778, 11.16849999, 8.56883433],
[ 4.24409799, 12.71746612, 11.3772169, 9.00514257, 10.47084185, 10.97567589, 3.98287652, 8.80552122]]
# X = range(8)

# for i in range(8):
#   for j in range(8):
#     plt.bar(X,data[j][i], color = 'b')
#     plt.bar(data[j][i], data[i][j], color = 'r', bottom = data[j][i])


percentages = (np.random.randint(5,20, (len(people), segments)))
y_pos = np.arange(len(people))

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

colors ='rgwm'
patch_handles = []
# left alignment of data starts at zero
left = np.zeros(len(people)) 
for i, d in enumerate(data):
    patch_handles.append(ax.barh(y_pos, d, 
      color=colors[i%len(colors)], align='center', 
      left=left))
    left += d

# search all of the bar segments and annotate
for j in range(len(patch_handles)):
    for i, patch in enumerate(patch_handles[j].get_children()):
        bl = patch.get_xy()
        x = 0.5*patch.get_width() + bl[0]
        y = 0.5*patch.get_height() + bl[1]
        ax.text(x,y, "%d%%" % (percentages[i,j]), ha='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.set_xlabel('Scores')
plt.show()

import matplotlib.pyplot as plt
fig = plt.figure()
patterns = [ "|" , "\\" , "/" , ".", "*","x", "o" ]

ax = fig.add_subplot(111)
for i in range(len(patterns)):
    ax.bar(i, 4, color='white', edgecolor='black', hatch=patterns[i])

plt.show()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

df = pd.read_csv('data.csv')

df.

