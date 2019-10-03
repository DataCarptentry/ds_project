import importlib
import numpy.testing as npt

country = importlib.import_module('.03_country-subset', 'notebooks') #file to get, . means 'belong to'

processed_data = "../data/processed/2019-10-03-winemag_Chile.csv"

def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    assert mean_price == 20.7865
    npt.assert_allclose(country.get_mean_price(processed_data), 20.787, rtol = 0.01)