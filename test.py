import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid')
sns.set(font_scale=1.5)
import Data_Preparation as dp
import re

# rd = dp.Read_data(dp.RatingsCsvFile, dp.UsersCsvFile, dp.MoviesCsvFile)
# movies = rd.Read_Movies_csv()

str = "nikunj joshi 29 (1995)"
dict = dict()

print(re.search(r'\((.*?)\)',str).group(1))

print(re.split(r'\((.*?)\)',str))