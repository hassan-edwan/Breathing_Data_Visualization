import numpy
import pandas as pd

df = pd.read_csv("breathing_Data_Sample.csv")

stddev = df['breathing_force'].std()
mean = df['breathing_force'].mean()



print(mean-stddev)