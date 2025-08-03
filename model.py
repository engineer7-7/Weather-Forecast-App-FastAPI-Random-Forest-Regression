import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# convert 'datetime' column to datetime type and split to year-month-day-hour, and drop the datetime column
def to_datetime(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])
    dataframe['year'] = dataframe['datetime'].dt.year
    dataframe['month'] = dataframe['datetime'].dt.month
    dataframe['day'] = dataframe['datetime'].dt.day
    dataframe['hour'] = dataframe['datetime'].dt.hour
    return dataframe.drop('datetime', axis=1)


# split set to features and target
def split_to_features_target(dataframe):
    X = dataframe.iloc[:, 1:].copy()
    y = dataframe.iloc[:, :1].copy()
    return X, y


# convert object columns from object type to numerical
def object_to_numerical(X):
    ct = ColumnTransformer(
        transformers=[(
            'encoder', OneHotEncoder(), [2, 3]
        )], remainder='passthrough'
    )
    X = ct.fit_transform(X)
    return X


# split set to Train-Test set
def split_set(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


# feature scaling
def feature_scaling_model_training_prediction(dataframe):
    X, y = split_to_features_target(dataframe)
    X = object_to_numerical(X)

    X_train, X_test, y_train, y_test = split_set(X, y)

    sc_X = StandardScaler()
    sc_y = StandardScaler()

    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)

    y_train = sc_y.fit_transform(y_train)

    y_train = y_train.ravel()

    forest_regressor = RandomForestRegressor()
    forest_regressor.fit(X_train, y_train)

    forest_predictions = sc_y.inverse_transform(forest_regressor.predict(X_test).reshape(-1, 1))
    mean_temp = int(forest_predictions.mean())

    far_mean_temp = int((mean_temp * 1.8) + 32)

    mean_temp = f'{mean_temp}°C'
    far_mean_temp = f'{far_mean_temp}°F'

    return mean_temp, far_mean_temp
