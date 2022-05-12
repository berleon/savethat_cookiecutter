"""Example how to use `savethat` for a simple ols fit."""

import dataclasses
import pickle
from typing import Any

import pandas as pd
import savethat
import sklearn
import sklearn.datasets
import sklearn.linear_model
from savethat import logger
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


@dataclasses.dataclass(frozen=True)
class FitOLSArgs(savethat.Args):
    dataset: str  # path to csv dataset
    target: str  # column name of the target


@dataclasses.dataclass(frozen=True)
class FitOLSResult:
    mse: float
    params: dict[str, Any]


class FitOLS(savethat.Node[FitOLSArgs, FitOLSResult]):
    def _run(self) -> FitOLSResult:
        # Loading the data
        if self.args.dataset == "california_housing":
            cali_df = sklearn.datasets.fetch_california_housing(as_frame=True)
            df = cali_df.data
            df['MedHouseVal'] = cali_df.target

        elif self.args.dataset == "iris":
            df = sklearn.datasets.fetch_iris(as_frame=True)
        else:
            df = pd.read_csv(self.args.dataset)

        # You can access any argument from `FitOLSArgs` with `self.args`
        train_keys = [k for k in df.keys() if k != self.args.target]
        X = df[train_keys].to_numpy()
        y = df[self.args.target].to_numpy()

        # A logger is preconfigured. Just `from savethat import logger`
        logger.info(f"Got {len(X)} samples.")
        X_train, X_test, y_train, y_test = train_test_split(X, y)

        # let's save the dataset
        dataset_key = f"datasets/{self.key}"
        with self.storage.open(f"{dataset_key}/datasets.pickle", "wb") as f:
            pickle.dump((X_train, X_test, y_train, y_test), f)

        # ... and then upload to the cloud
        self.storage.upload(dataset_key)

        ols = sklearn.linear_model.LinearRegression()
        ols.fit(X_train, y_train)

        mse = mean_squared_error(y_test, ols.predict(X_test))
        logger.info(f"Mean squared error of {mse}")
        return FitOLSResult(mse, ols.get_params())
        # the results will be stored to `self.key / results.pickle`
