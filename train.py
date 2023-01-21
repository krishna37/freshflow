import pandas as pd
from prophet import Prophet
from typing import str


exp_date ='2022-01-01'


def load_data(path: str):
    """
    :param path: path to dataframe
    :return:
    """
    return pd.load_csv(path)


def preprocess(df: pd.DataFrame):
    """
    :param df: input dataframe with data
    :return: preprocessed pd dataframe
    """
    df = df.fillna(0)  # replace nulls with zeros in sales and orders
    df = df.drop_duplicates()
    return df


def train_prophet(df_item: pd.DataFrame,
                  exp_date: str):
    """
    
    :param df_item: preprocessed pd dataframe
    :return: dataframe with future predictions
    """
    df_item = df_item.rename(columns={
        'day': 'ds',
        'sales_quantity': 'y'
    })
    model = Prophet(interval_width=0.95)

    ts_train = (df_item.query(f"ds < '{exp_date}'")
                .sort_values('ds')
                )
    ts_test = (df_item
               .query(f"ds >= '{exp_date}'")
               .sort_values('ds')
               .assign(ds=lambda x: pd.to_datetime(x["ds"]))
               )
    model.fit(ts_train)

    # at this step we predict the future and we get plenty of additional columns be cautious
    ts_hat = (model.predict(ts_test)[["ds", "yhat", 'yhat_lower', 'yhat_upper']]
              .assign(ds=lambda x: pd.to_datetime(x["ds"]))
              ).merge(ts_test, on=["ds"], how="left")  # merge to retrieve item and store index

    return ts_hat


def main():
    """
    :return: returns the
    """
    df = load_data('data.csv')
    df = preprocess(df)
    df_predict = df.groupby('item_number').apply(train_prophet)
    return df_predict


if __name__ == "__main__":
    main()