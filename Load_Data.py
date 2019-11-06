import os
import pandas as pd
# Define file directories

DataSetDir = 'Data_Sets'
UserDataFile = 'users.dat'
MovieDataFile = 'movies.dat'
RatingsDataFile = 'ratings.dat'

# Define csv files to be saved into
UsersCsvFile = 'users.csv'
MoviesCsvFile = 'movies.csv'
RatingsCsvFile = 'ratings.csv'

Ages = { 1: "Under 18", 18: "18-24", 25: "25-34", 35: "35-44", 45: "45-49", 50: "50-55", 56: "56+" }
Occupations = { 0: "other or not specified", 1: "academic/educator", 2: "artist", 3: "clerical/admin",
                4: "college/grad student", 5: "customer service", 6: "doctor/health care",
                7: "executive/managerial", 8: "farmer", 9: "homemaker", 10: "K-12 student", 11: "lawyer",
                12: "programmer", 13: "retired", 14: "sales/marketing", 15: "scientist", 16: "self-employed",
                17: "technician/engineer", 18: "tradesman/craftsman", 19: "unemployed", 20: "writer" }

class Ratings_Data:
    def __init__(self,DataSetDir,RatingsDataFile):
        self.DataSetDir = DataSetDir
        self.RatingsDataFile = RatingsDataFile
        # Read the Ratings File
        self.ratings = pd.read_csv(os.path.join(self.DataSetDir, self.RatingsDataFile), sep='::',engine='python',
                    encoding='latin-1', names=['user_id', 'movie_id', 'rating', 'timestamp'])
        # print('\n',len(self.ratings))
        # print('\n',self.ratings.head())
        # print('\n',self.ratings.describe())
        # print('\n',self.ratings.info())


    def drop_duplicates(self):
        max_userid = self.ratings['user_id'].drop_duplicates().max()
        max_movieid = self.ratings['movie_id'].drop_duplicates().max()
        # print('\n',max_userid)

    def add_emb_id(self):
        self.ratings['user_emb_id'] = self.ratings['user_id'] - 1
        self.ratings['movie_emb_id'] = self.ratings['movie_id'] - 1

    def save_data_in_csv(self):
        # Save Data into ratings.csv
        self.ratings.to_csv(RatingsCsvFile, sep='\t', header='True', encoding='latin-1',
                       columns=['user_id', 'movie_id', 'rating', 'timestamp', 'user_emb_id', 'movie_emb_id'])


# rd = Ratings_Data(DataSetDir,RatingsDataFile)
# rd.drop_duplicates()
# rd.add_emb_id()
# rd.save_data_in_csv()

class Users_Data:
    def __init__(self,DataSetDir,UserDataFile):
        self.DataSetDir = DataSetDir
        self.UserDataFile = UserDataFile
        # Read the users File
        self.users = pd.read_csv(os.path.join(self.DataSetDir, self.UserDataFile), sep='::',engine='python',
                    encoding='latin-1', names=['user_id', 'gender', 'age', 'occupation','zipcode'])
        # print('\n',len(self.users))
        # print('\n',self.users.head())
        # print('\n',self.users.describe())
        # print('\n',self.users.info())

    def add_desc(self):
        self.users['age_desc'] = self.users['age'].apply(lambda x: Ages[x])
        self.users['occ_desc'] = self.users['occupation'].apply(lambda x: Occupations[x])
        # print(len(self.users))
        # print(self.users.head())


    def save_data_in_csv(self):
        # Save Data into users.csv
        self.users.to_csv(UsersCsvFile, sep='\t', header='True', encoding='latin-1',
                       columns=['user_id', 'gender', 'age', 'occupation', 'zipcode', 'age_desc', 'occ_desc'])

# ud = Users_Data(DataSetDir, UserDataFile)
# ud.add_desc()
# ud.save_data_in_csv()


class Movies_Data:
    def __init__(self,DataSetDir, MovieDataFile):
        self.DataSetDir = DataSetDir
        self.MovieDataFile = MovieDataFile
        # Read the movies File
        self.movies = pd.read_csv(os.path.join(self.DataSetDir, self.MovieDataFile), sep='::',engine='python',
                    encoding='latin-1', names=['movie_id', 'title', 'genres'])
        # print('\n',len(self.movies))
        # print('\n',self.movies.head())
        # print('\n',self.movies.describe())
        # print('\n',self.movies.info())
    def save_data_in_csv(self):
        # Save Data into movies.csv
        self.movies.to_csv(MoviesCsvFile, sep='\t', header='True', encoding='latin-1',
                       columns=['movie_id', 'title', 'genres'])

# md = Movies_Data(DataSetDir, MovieDataFile)
# md.save_data_in_csv()
# rd = Ratings_Data(DataSetDir, RatingsDataFile)
# rd.save_data_in_csv()
# ud = Users_Data(DataSetDir, UserDataFile)
# ud.save_data_in_csv()