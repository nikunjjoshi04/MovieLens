import numpy as np
import pandas as pd
import Data_Preparation as dp

# Read All CSV Files
rd = dp.Read_data(dp.RatingsCsvFile, dp.UsersCsvFile, dp.MoviesCsvFile)
ratings = rd.Read_Ratings_csv()
users = rd.Read_Users_csv()
movies = rd.Read_Movies_csv()

# show Movies Head
# print(movies.head())

# show Movies Head
# print(ratings.head())

# count the number of unique Users and Movies
n_users = ratings.user_id.unique().shape[0]
# print(n_users)
n_movies = movies.movie_id.unique().shape[0]
# print(n_movies)
# print("Number of Users = " + str(n_users) + " | Number of Movies = " + str(n_movies))


# make a Matrix user par movie Ratings
Ratings = ratings.pivot(index = "user_id", columns = "movie_id", values = "rating").fillna(0)
# print(Ratings.head(20))


R = Ratings.as_matrix()
user_ratings_mean = np.mean(R, axis = 1)
Ratings_demeaned = Ratings - user_ratings_mean.reshape(-1, 1)
print(Ratings_demeaned)

sparsity = round(1.0 - len(ratings) / float(n_users * n_movies), 3)
print ('The sparsity level of MovieLens1M dataset is ' +  str(sparsity * 100) + '%')


print("\n END \n")