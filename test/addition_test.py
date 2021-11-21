"""Testing Addition"""

import pandas as pd
from calculation.addition import Addition


def test_addition():
    """Testing addition method"""
    # Arrange
    addition = Addition(1, 2)
    # Act
    result = addition.get_result()
    # Assert
    assert result == 3


def test_addition_pandas():
    """Testing subtraction method for two values"""
    path = "test/test_data/addition.csv"
    # Read in the cvs file
    dataframe = pd.read_csv(path)

    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        addition = Addition(value1[i], (value2[i],))
        # Act and Assert
        assert addition.get_result() == result[i]
