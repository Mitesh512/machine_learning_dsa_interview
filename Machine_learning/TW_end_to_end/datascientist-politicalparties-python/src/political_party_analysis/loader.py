
from typing import List
from sklearn.preprocessing import StandardScaler
import pandas as pd


class DataLoader:
    """Class to load the political parties dataset"""

    data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self):
        self.party_data = self._download_data()
        self.non_features = []
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        # data_path, _ = urlretrieve(
        #     self.data_url,
        #     Path(__file__).parents[2].joinpath(*["data", "CHES2019V3.dta"]),
        # )
        data_path = "data/raw_data/CHES2019V3.csv"
        return pd.read_csv(data_path)

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to remove duplicates in a dataframe"""
        df = df.copy()
        ##### YOUR CODE GOES HERE #####
        n_duplicates = df.duplicated()

        if n_duplicates > 0:
            df.drop_duplicates(keep="first", inplace=True)
        return df

    def remove_nonfeature_cols(
        self, df: pd.DataFrame, non_features: List[str], index: List[str]
    ) -> pd.DataFrame:
        """Write a function to remove certain features cols and set certain cols as indices
        in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        if non_features:
            self.non_features = non_features

        non_features = [col for col in self.non_features if col in df.columns]
        if len(non_features):
            df.drop(non_features, axis=1, inplace=True)

        # set index
        if index:
            self.index = index

        df.set_index(index, inplace=True)

        return df

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to handle NaN values in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        # Identify Nulls
        # null_cols = list(df[df.isnull().sum()].columns)
        # Numeric column # Median, Mean
        numerical_cols = [col for col in df.columns]  # dtype dtype == float'
        self.numerical_cols = numerical_cols
        medians = df[numerical_cols].median()
        df[numerical_cols].fillna(medians, inplace=True)

        # Categorical Mode, missing_col
        categorical_cls = [col for col in df.columns]
        df[categorical_cls].fillna(value="missing", inplace=True)

        # We can have a mapping eu_cohesion
        mapping = {"eu_cohesion": 4}
        mapping_cols = ["eu_cohesion"]
        df[mapping_cols].fillna(mapping, inplace=True)
        return df

    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to normalise values in a dataframe. Use StandardScaler."""
        ##### YOUR CODE GOES HERE #####
        # Numerical Columns
        numerical_cols = [col for col in df.columns]  # dtype dtype == float
        scaler = StandardScaler()
        return pd.DataFrame(scaler.fit_transform(df[numerical_cols]), columns=numerical_cols)

    def preprocess_data(self):
        """Write a function to combine all pre-processing steps for the dataset"""
        ##### YOUR CODE GOES HERE #####
        self.party_data = self.remove_duplicates(self.party_data)
        self.party_data = self.remove_nonfeature_cols(self.party_data)
        self.party_data = self.handle_NaN_values(self.party_data)
        self.party_data = self.scale_features(self.party_data)
