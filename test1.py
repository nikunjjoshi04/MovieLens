import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
RATINGS_CSV_FILE = 'rat2.csv'

movies = pd.read_csv('rat2.csv', sep='\t', encoding='latin-1',usecols=['title','genres'])

# print(movies)

# for mov in movies:
#     print(mov)

# Save into ratings.csv
# movies.to_csv(RATINGS_CSV_FILE,
#                sep='\t',
#                header=True,
#                encoding='latin-1',
#                columns=['imdbId', 'title', 'releaseYear', 'releaseDate', 'genre', 'writers','actors','directors','sequel','hitFlop'])

# print(movies.loc[1270:1283])
print(movies.head(50))