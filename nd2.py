import pandas as pd
import plotly.figure_factory as pff
import csv
reading=pd.read_csv('Student Marks vs Days Present.csv')
figure=pff.create_distplot([reading['Days Present'].tolist()],["Days Present"],show_hist=False)
figure.show()