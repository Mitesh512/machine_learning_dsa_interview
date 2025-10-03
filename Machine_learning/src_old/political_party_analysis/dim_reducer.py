import pandas as pd
from sklearn.decomposition import PCA


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(
        self, type: str = "PCA", data: pd.DataFrame = pd.DataFrame(), n_components: int = 2
    ):
        self.n_components = n_components
        self.data = data
        self.model = PCA(n_components=self.n_components, random_state=42)

    ##### YOUR CODE GOES HERE #####
    def transform(self):

        transformed_data = self.model.fit_transform(self.data)

        return pd.DataFrame(transformed_data, columns=["PC1", "PC2"], index=self.data.index)
