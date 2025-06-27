import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


def load(path):
    df = pd.read_csv(path)
    return df

def get_flavor_values(df):
    flavor_cols = ['sweet', 'salty', 'sour', 'bitter', 'umami']
    flavor_data = df[flavor_cols]
    return flavor_data.values

def fit_knn(flavour_values, distance_metric):
    knn = NearestNeighbors(metric=distance_metric)
    knn.fit(flavour_values)
    return knn

def get_top_dishes(profiles, ks, knn_model, dishes_df):
    """
    Returns top k dishes similar to profile
    
    Args:
        profiles (list): List of Flavor profile, shape (1, 5)
        ks (int): List of Number of nearest dishes to return
        knn_model (NearestNeighbors): Fitted KNN model
        dishes_df (pd.DataFrame): Original dataframe with dish names

    """
    all_dishes = []

    for (profile_vector, k) in zip(profiles, ks):
        distance, indices = knn_model.kneighbors(profile_vector, n_neighbors=k)
        selected_dishes =  dishes_df.iloc[indices[0]]

        all_dishes.append(selected_dishes)

    all_dishes = pd.concat(all_dishes).reset_index(drop=True)

    return all_dishes


def return_all_dishes():
    dishes_df = load('./csv_data/data.csv')
    flavor_values = get_flavor_values(dishes_df)
    knn = fit_knn(flavor_values, 'euclidean')

    # Define flavor profiles
    savory_profile = np.array([[10, 25, 15, 5, 45]])
    sweet_profile = np.array([[65, 5, 10, 10, 10]])
    mixed_profile = np.array([[15, 25, 30, 10, 20]])

    profiles = [savory_profile, sweet_profile, mixed_profile]
    ks = [15, 5, 5]

    selected_dishes = get_top_dishes(profiles, ks, knn, dishes_df)

    return selected_dishes




if __name__ == "__main__":
    print(return_all_dishes())
