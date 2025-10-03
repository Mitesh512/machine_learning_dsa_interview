from typing import List
from sklearn.preprocessing import StandardScaler
import pandas as pd


class DataLoader:
    """Class to load the political parties dataset"""

    # data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self):
        self.party_data = self._download_data()
        ## Non feature columns: high NANs and these are only about Including Turkey into the EU
        self.non_features = ["eu_econ_require", "eu_political_require", "eu_googov_require"]
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        # data_path, _ = urlretrieve(
        #     self.data_url,
        #     Path(__file__).parents[2].joinpath(*
        # ["data", "CHES2019V3.dta"]),
        # )
        data_path = "data/raw_data/CHES2019V3.csv"
        return pd.read_csv(data_path)

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        """Write a function to remove duplicates in a dataframe"""
        n_duplicates = df.duplicated().sum()
        if n_duplicates > 0:
            print(f"Found and removed {n_duplicates} duplicate row(s).")
            return df.drop_duplicates(keep="first")

        print("No duplicate rows found.")
        return df

    def remove_nonfeature_cols(
        self, df: pd.DataFrame, non_features: List[str], index: List[str]
    ) -> pd.DataFrame:
        df = df.copy()
        """Write a function to remove certain features cols and set certain cols as indices
        in a dataframe"""
        # Cross checking if all these feature are there in the dataframe or not
        # remove only columns which are part of df to avoid the error
        columns_to_drop = [col for col in non_features if col in df.columns]
        df.drop(columns_to_drop, axis=1, inplace=True)

        # set columns as index, cross check these as well,if they are part of the df or not
        cols_to_set_as_ind = [col for col in index if col in df.columns]
        df.set_index(cols_to_set_as_ind, inplace=True)

        return df

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to handle NaN values in a dataframe"""

        ##### YOUR CODE GOES HERE #####
        ## Critical NANs
        df = df.copy()

        ## Drop columns with very high NAN values
        cols_with_high_nan = list(df.columns[df.isnull().sum() > df.shape[0] * 0.90])
        df.drop(cols_with_high_nan, axis=1, inplace=True)

        ## Moderate NANs
        moderate_nan_cols_dict = {
            "eu_cohesion": 4,
            "eu_foreign": 4,
            "eu_intmark": 4,
            "eu_budgets": 4,
            "eu_asylum": 4,
        }
        moderate_nan_cols_dict = {
            col: val for col, val in moderate_nan_cols_dict.items() if col in df.columns
        }
        df.fillna(moderate_nan_cols_dict, inplace=True)

        ## Low NANs
        medians = df.median(numeric_only=True)
        df = df.fillna(medians)
        return df

    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to normalise values in a dataframe. Use StandardScaler."""
        ##### YOUR CODE GOES HERE #####
        df = df.copy()
        scaler = StandardScaler()
        columns_to_be_scaled = df.columns  # [col for col in df.columns if col != "eastwest"]
        df[columns_to_be_scaled] = scaler.fit_transform(df[columns_to_be_scaled])
        return df

    def preprocess_data(self):
        """Write a function to combine all pre-processing steps for the dataset"""
        ##### YOUR CODE GOES HERE #####
        # 1. remove_duplicates
        self.party_data = self.remove_duplicates(self.party_data)

        # 2. handle_NaN_values
        self.party_data = self.handle_NaN_values(self.party_data)

        # 3. remove_nonfeature_cols
        self.party_data = self.remove_nonfeature_cols(
            self.party_data, self.non_features, self.index
        )

        # 4. scale_features
        self.party_data = self.scale_features(self.party_data)
