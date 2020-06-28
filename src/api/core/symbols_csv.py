# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 16.06.2020
# Time: 22:17
# To change this template use File | Settings | File and Code Templates.

from .exceptions import NoneCorrectFileError
import pandas as pd


def export_symbols_data(name: str, use_cols: list = None) -> pd.DataFrame:
    """
    export data from csv and return
    :return: DataFrame iterable object
    """
    if name.endswith('.csv'):
        dataframe = pd.read_csv(name, usecols=use_cols)
    else:
        raise NoneCorrectFileError(f'The file: {name} must contain extension .csv, please specify correct file!')

    return dataframe
