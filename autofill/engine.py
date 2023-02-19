import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold

class AutoFill():
    """Analyze and fill missing values for features in dataframe.
    
    The analysis is either performed using a train-test-split or k-fold cross-validator.
    Each method is analysed based on a goodness-of-fit test.
    
    The following methods are included for filling missing values:
    - Mean
    - Median
    - Mode
    - kNN
    - Regression
    
    The following goodness-of-fit tests are included:
    - Mean Squared Error (MSE)
    - Mean Absolute Error (MAE)
    - Mean Absolute Percentage Error (MAPE)
    - Root-Mean-Square Deviation (RMSE) 
    
    Parameters
    ----------
    
    
    Attributes
    ----------
    
    """
    
    def __init__(self, k_fold=True):
        self.k_fold = k_fold
        self.columns = None
        self.data = None
        self.missing_info = {}
    
    def _split_data(self, dataframe, test_size=0.2):
        self.train_data, self.test_data = train_test_split(dataframe, test_size=test_size)
        
    def _k_fold_split(self, dataframe, n_splits=5):
        kf = KFold(n_splits=n_splits)
        # Create a new column in the DataFrame to store the fold indices
        dataframe["fold"] = -1
        # Loop over the folds and set the values in the "fold" column
        for fold, (train_indices, val_indices) in enumerate(kf.split(dataframe)):
            dataframe.loc[val_indices, "fold"] = fold
            
    def _get_column_names(self, dataframe):
        self.columns = dataframe.columns[dataframe.isnull().any()].tolist()
    
    def get_missing_columns(self, dataframe, normalize=False, return_output=True):
        if not self.data:
            self.data = dataframe.copy()
        if not self.columns:
            self._get_column_names(self.data)
            
        if return_output and self.columns:
            if not normalize:
                return self.data[self.columns].isna().sum().sort_values(ascending=False).to_dict()
            else:
                return {column: missing_count / dataframe.shape[0] for column, missing_count in dataframe[self.columns].isna().sum().sort_values(ascending=False).to_dict().items()}
        
    def missing_analysis(self, dataframe, test_size=0.2, n_splits=5, export_results=False):
        if not self.data:
            self.data = dataframe.copy()
        if not self.columns:
            self._get_column_names(self.data)
            
        if self.k_fold:
            self._k_fold(dataframe, n_splits=n_splits)
        else:
            self._split_data(dataframe, test_size=test_size)
            
    def fit(self, dataframe, column=None, method="mean"):
        if not self.data:
            self.data = dataframe.copy()
        if not self.columns:
            self._get_column_names(self.data)
        
    def transform(self):
        pass
    
    def fit_transform(self, dataframe, column=None, method="mean"):
        self._get_column_names(dataframe)
        pass
    
    