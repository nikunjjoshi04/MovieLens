import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define csv files to be saved into
RatingsCsvFile = 'ratings.csv'
UsersCsvFile = 'users.csv'
MoviesCsvFile = 'rat2.csv'

class Read_data:
    def __init__(self,RatingsCsvFile, UsersCsvFile, MoviesCsvFile):
        self.RatingsCsvFile = RatingsCsvFile
        self.UsersCsvFile = UsersCsvFile
        self.MoviesCsvFile = MoviesCsvFile

    def Read_Ratings_csv(self):
        # Reading ratings file
        # Ignore the timestamp column in ratings
        ratings = pd.read_csv(self.RatingsCsvFile, sep='\t', encoding='latin-', usecols=['user_id', 'movie_id', 'rating'])
        # print("1")
        return ratings

    def Read_Users_csv(self):
        # Reading users file
        users = pd.read_csv(self.UsersCsvFile, sep='\t', encoding='latin-', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])
        # print("2")
        return users

    def Read_Movies_csv(self):
        # Reading movies file
        movies = pd.read_csv(self.MoviesCsvFile, sep='\t', encoding='latin-1', usecols=["title","genres"])
        # print("3")
        return movies

    def show_Data(self):
        ratings = Read_data.Read_Ratings_csv(self)
        users = Read_data.Read_Users_csv(self)
        movies = Read_data.Read_Movies_csv(self)

        # # Check the top 5 rows of ratings
        # print("\n>>> Ratings Data\n")
        # print(ratings.head())
        # # Check the file info of ratings
        # print("\n>>> Ratings Data Information\n")
        # print(ratings.info())
        # # Check the file Description of ratings
        # print("\n>>> Ratings Data Description\n")
        # print(ratings.describe())
        #
        # # Check the top 5 rows of users
        # print("\n>>> Users Data\n")
        # print(users.head())
        # # Check the file info of users
        # print("\n>>> Users Data Information\n")
        # print(users.info())
        # # Check the file Description of users
        # print("\n>>> Users Data Description\n")
        # print(users.describe())

        # Check the top 5 rows of movies
        print("\n>>> Movies Data\n")
        print(movies.head())
        # Check the file info of movies
        print("\n>>> Movies Data Information\n")
        print(movies.info())
        # Check the file Description of movies
        print("\n>>> Movies Data Description\n")
        print(movies.describe())

# rd = Read_data(RatingsCsvFile, UsersCsvFile, MoviesCsvFile)
# rd.Read_Ratings_csv()
# rd.Read_Users_csv()
# rd.Read_Movies_csv()
# rd.show_Data()