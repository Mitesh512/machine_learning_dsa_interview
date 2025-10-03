import pandas as pd
from sklearn.mixture import GaussianMixture


class DensityEstimator:
    """
    Class to estimate Density/Distribution of the given data.
    1. Write a function to model the distribution of the political party dataset
    2. Write a function to randomly sample 10 parties from this distribution
    3. Map the randomly sampled 10 parties back to the original higher dimensional
    space as per the previously used dimensionality reduction technique.
    """

    def __init__(self, data: pd.DataFrame, dim_reducer, high_dim_feature_names):
        self.data = data
        self.dim_reducer_model = dim_reducer.model
        self.feature_names = high_dim_feature_names
        self.sample = 10

    ##### YOUR CODE GOES HERE #####
    def fit(self, n_components: int = 10):
        self.model = GaussianMixture(n_components, random_state=42)
        self.model.fit(self.dim_reducer_model.transform(self.data))

    ## Randomly samples 10 parties from distribution
    def sample_parties(self):
        samples, _ = self.model.sample(self.sample)
        samples_df = pd.DataFrame(samples, columns=["PC1", "PC2"])
        return samples_df

    def inverse_transform_samples(self, samples_df):
        high_dim_data = self.dim_reducer_model.inverse_transform(samples_df)
        return pd.DataFrame(high_dim_data, columns=self.feature_names)
