import numpy
import pandas
import pytest

from ironhelpers.helpers import normalize_cols

def test_inplace_false():

    df = pandas.DataFrame(data=numpy.random.rand(2,2),
                          columns=['coluna 1', 'Coluna 2 '])
    
    df_returned = normalize_cols(df, inplace=False)
    
    assert (df_returned.columns == ['coluna_1', 'coluna_2']).all()
    assert (df.columns == ['coluna 1', 'Coluna 2 ']).all()
    
def test_inplace_true():    
    df = pandas.DataFrame(data=numpy.random.rand(2,2),                                                                  
                          columns=['coluna 1', 'Coluna 2 '])
    
    df_returned_foo = normalize_cols(df, inplace=True)
    
    assert (df_returned_foo == None)
    assert (df.columns == ['coluna_1', 'coluna_2']).all()