import matplotlib.pyplot as plt
import pandas as pd
import math
import csv


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_csv():
    # Use a breakpoint in the code line below to debug your script.
    data = pd.read_csv('/Users/pragyatyagi/PycharmProjects/mood-prediction/data/raw/dataset_mood_smartphone.csv')
    df = pd.DataFrame(data)
    return df


def data_preprocessing(df):
    mood_value_list = df['value'].tolist()
    missing_value = [value for value in mood_value_list if pd.isnull(value)]

    # Drop all the NaN values
    df_missing = pd.DataFrame(missing_value, columns=['missing_values'])
    df_missing.dropna(inplace=True)
    print(len(df_missing))


def write_to_csv():
    user_ids = ['AS14.01', 'AS14.02', 'AS14.03', 'AS14.05', 'AS14.06', 'AS14.07', 'AS14.08', 'AS14.09', 'AS14.12',
                'AS14.13',
                'AS14.14', 'AS14.15', 'AS14.16', 'AS14.17', 'AS14.19', 'AS14.20', 'AS14.23', 'AS14.24', 'AS14.25',
                'AS14.26',
                'AS14.27', 'AS14.28', 'AS14.29', 'AS14.30', 'AS14.31', 'AS14.32', 'AS14.33']

    # Define the header row
    # header = ['userid', 'date', 'mood', 'circumplex.arousal', 'circumplex.valence', 'activity', 'screen',
    #           'appCat.builtin', 'appCat.communication', 'appCat.entertainment', 'appCat.finance', 'appCat.game',
    #           'appCat.office', 'appCat.other', 'appCat.social', 'appCat.travel', 'appCat.unknown', 'appCat.utilities',
    #           'appCat.weather']

    header = ['userid', 'date']

    filename = "/Users/pragyatyagi/PycharmProjects/mood-prediction/data/raw/mood-dataset-new.csv"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # df = read_csv()
    # data_preprocessing(df)
    write_to_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
