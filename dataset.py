from data_collector import get_final_data
import pandas as pd



def create_dataframe(city, api_key):
    df = pd.DataFrame(data=get_final_data(city, api_key))
    df['temp'] = df['temp'] - 273.15
    return df




