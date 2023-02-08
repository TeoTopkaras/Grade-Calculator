import numpy as np
import pandas as pd
import plotly.express as px

# Make the width of all shells wider
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))


grades = pd.read_csv('Files\INPUT_NAME.txt', delimiter = '\t')
fig = px.histogram(grades, x='Grade')
fig.update_layout(xaxis_title='Grades', yaxis_title='N',width = 900, height = 600)
fig.show()

for i in range(len(grades)):
    mult = grades['ECTS']*grades['Grade']
    sum_ECTS = np.sum(grades['ECTS'])
    sum_mult = np.sum(mult)

    
print('Your final grade is:', round(sum_mult/sum_ECTS,2))





