import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Create a dataset of user-movie ratings
data = {
    'user': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Inception': [5, 4, np.nan, 2, 1],
    'Avatar': [3, 5, 4, 4, 2],
    'The Dark Knight': [4, 5, 5, np.nan, 3],
    'Interstellar': [5, np.nan, 4, 3, 4],
    'The Matrix': [4, 4, 4, 2, 5]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Step 2: Create a user-item matrix
# Replace NaN values with 0 for simplicity in cosine similarity calculation
user_item_matrix = df.set_index('user').fillna(0)

# Step 3: Calculate the cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert the similarity matrix into a DataFrame for easier reading
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Step 4: Function to recommend movies based on similarity
def recommend_movies(user, user_item_matrix, user_similarity_df):
    # Get the list of users similar to the given user
    similar_users = user_similarity_df[user].sort_values(ascending=False)

    # Remove the given user from the list of similar users
    similar_users = similar_users.drop(user)

    # Get the movies that the similar users liked
    similar_user_ratings = user_item_matrix.loc[similar_users.index]
    
    # Calculate the weighted average ratings of each movie from similar users
    weighted_ratings = similar_user_ratings.T.dot(similar_users).div(similar_users.sum())

    # Sort the movies by their weighted ratings (high to low)
    recommendations = weighted_ratings.sort_values(ascending=False)

    # Get the top 3 movie recommendations
    return recommendations.head(3)

# Example: Recommend movies for 'Alice'
recommended_movies = recommend_movies('Alice', user_item_matrix, user_similarity_df)

print("Recommended Movies for Alice:")
print(recommended_movies)
