import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid')
sns.set(font_scale=1.5)
import Data_Preparation as dp

# Read All CSV Files
rd = dp.Read_data(dp.RatingsCsvFile, dp.UsersCsvFile, dp.MoviesCsvFile)
movies = rd.Read_Movies_csv()
ratings = rd.Read_Ratings_csv()
users = rd.Read_Users_csv()


# Join all 3 Data Sets CSV files into one dataframe
# datasets = pd.merge(pd.merge(movies, ratings),users)

# print("\n>>> DataSets\n")
# print(datasets.head())
# # Check the file info of DataSets
# print("\n>>> DataSets Information\n")
# print(datasets.info())
# # Check the file Description of DataSets
# print("\n>>> DataSets Description\n")
# print(datasets.describe())

# statistic summary of ratings
# print(ratings.describe())

# heatmap graph of column dependency
# cor_df = datasets.corr()
# mpl.xticks(rotation = 60)
# mpl.yticks(rotation = 360)
# sns.heatmap(cor_df,annot = True, linewidths = .5)
# mpl.show()

# # Display Graph distribution of rating
# sns.distplot(ratings['rating'].fillna(ratings['rating'].median))
# mpl.show()

# for count no of Users in In Age Group
# def count_word(census):
#     keyword_count = dict()
#     lst1 = ["Under 18", "18-24", "25-34", "35-44", "45-49", "50-55", "56+"]
#     lst = []
#     for x in census:
#         lst.append(x)
#     for x in lst1:
#         keyword_count[x] = lst.count(x)
#     # print(keyword_count)
#     return keyword_count
# age_counts = count_word(datasets['age_desc'])

# # Bar Graph of Number of Users In Age Group
# objects = age_counts.keys()
# y_pos = np.arange(len(objects))
# performance = age_counts.values()
# colors = ['#9A031E', '#FB8B24', '#5F0F40', '#373072', '#FDCF21', '#59A775', '#0EA723']
# # Plot
# mpl.bar(y_pos, performance, color = colors, align='center', alpha=0.5)
# mpl.xticks(y_pos, objects)
# mpl.ylabel('Number of Users')
# mpl.xlabel('Age Groups')
# mpl.title('Users By Age Group' )
# mpl.show()



# Display 20 movies with highest ratings
# x = datasets[['title', 'genres', 'rating']].sort_values('rating', ascending=False).head(20)
# print(x)

# short List all genre keywords
genre_labels = set()
mylst = []
for s in movies['genres'].str.split('|').values:
    mylst.append(s)
    # print(mylst)
    # c=c+1
    # print(c)
    # s.strip()
    genre_labels = genre_labels.union(set(s))
# print(genre_labels)

# print all genres
# for x in genre_labels:
#     print(x,end="\n")
# print(len(genre_labels))

# for count no of genres
def count_word(ref_col,census):
    keyword_count = dict()
    lst = []
    for s in census:
        keyword_count[s] = 0
    # print(keyword_count)
    for x in ref_col:
        for i in x.split('|'):
                lst.append(i)
    for xx in census:
        keyword_count[xx] = lst.count(xx)
    # print(keyword_count)
    # keyword_occ = []
    # for k,v in keyword_count.items():
    #     keyword_occ.append([k,v])
    # keyword_occ.sort(key=lambda x: x[1], reverse=True)
    # # print(keyword_occ)
    return keyword_count
keyword_occurences = count_word(movies['genres'],genre_labels)
print(keyword_occurences)


# # Function that counts the number of times each of the genre keywords appear
# def count_word(dataset, ref_col, census):
#     keyword_count = dict()
#     for s in census:
#         keyword_count[s] = 0
#     for census_keywords in dataset[ref_col].str.split('|'):
#         if type(census_keywords) == float and pd.isnull(census_keywords):
#             continue
#         for s in [s for s in census_keywords if s in census]:
#             if pd.notnull(s):
#                 keyword_count[s] += 1
#     #______________________________________________________________________
#     # convert the dictionary in a list to sort the keywords by frequency
#     keyword_occurences = []
#     for k,v in keyword_count.items():
#         keyword_occurences.append([k,v])
#     keyword_occurences.sort(key = lambda x:x[1], reverse = True)
#     return keyword_occurences, keyword_count
#
# # Calling this function gives access to a list of genre keywords which are sorted by decreasing frequency
# keyword_occurences, dum = count_word(movies, 'genres', genre_labels)
# # print(keyword_occurences)



# Break up the big genre string into a string array
movies['genres'] = movies['genres'].str.split('|')
# Convert genres to string value
movies['genres'] = movies['genres'].fillna("").astype('str')
# print(movies["genres"])

# #pie plot
# labels = keyword_occurences.keys()
# sizes = keyword_occurences.values()
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice
# # Plot
# mpl.pie(sizes, labels=labels, colors=colors,
# autopct='%1.1f%%', shadow=True, startangle=140)
# mpl.axis('equal')
# mpl.show()


#  TfidfVectorizer function
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(movies['genres'])
# print(tfidf_matrix.shape)


#  Cosine Similarity to calculate a numeric quantity
from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# print(cosine_sim[:4, :4])


# Build a 1-dimensional array with movie titles
titles = movies['title']
indices = pd.Series(movies.index, index=movies['title'])
# print(titles)
# print(indices)


# Function that get movie recommendations based on the cosine similarity score of movie genres
def genre_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

print(genre_recommendations("Agneepath").head())

# print(datasets.head())

# print(indices.head(50))


print("\n End")