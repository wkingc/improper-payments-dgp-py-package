from improper_payments_dgp import improper_payments_dgp
import pandas as pd
import numpy as np
import numpy.testing as npt
import pytest

def test_improper_payments_dgp():
    pop_data = improper_payments_dgp(mean_target = 100, cv_target = 1/2, A = 0, B = 1000, b = (0.4, 0.6), p_improper = 0.1, size = 100000, random_state = 123)
    
    assert isinstance(pop_data, pd.DataFrame)
    assert list(pop_data.columns) == ['X', 'B', 'Z', 'Y']
    assert len(pop_data) == 100000
    
    mean_X = pop_data.X.mean()
    total_X = pop_data.X.sum()
    cv_X = pop_data.X.std()/pop_data.X.mean()
    min_B = pop_data.B.min()
    max_B = pop_data.B.max()
    mean_Z = pop_data.Z.mean()
    mean_Y_improper = pop_data.Y[pop_data.Y > 0].mean()
    total_Y = pop_data.Y.sum()
    
    assert round(mean_X, 2) == round(np.float64(99.96861105724925), 2)
    assert round(total_X, 2) == round(np.float64(9996861.105724925), 2)
    assert round(cv_X, 2) == round(np.float64(0.49977019979482173), 2)
    assert round(min_B, 2) == round(np.float64(0.4000001820563135), 2)
    assert round(max_B, 2) == round(np.float64(0.5999945536761311), 2)
    assert round(mean_Z, 2) == round(np.float64(0.09952), 2)
    assert round(mean_Y_improper, 2) == round(np.float64(59.655189118224804), 2)
    assert round(total_Y,2) == round(np.float64(593688.4421045732), 2)