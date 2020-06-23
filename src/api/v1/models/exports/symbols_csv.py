# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 16.06.2020
# Time: 22:17
# To change this template use File | Settings | File and Code Templates.

import pandas as pd


def export_symbols_data():
    """
    :return:
    """
    dataframe = pd.read_csv("ASXListedCompanies.csv", header=None)

    for data in zip(dataframe[0], dataframe[1], dataframe[2]):
        print(data)
