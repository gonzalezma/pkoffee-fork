import pytest

def test_data():
    from .. import data
    dt = data.load_csv("analysis/coffee_productivity.csv")
    
    assert (dt is not None)
    
    assert dt.cups[0] == 9
    
    assert dt.cups[50] == 11
    
    assert dt.cups[199999] == 1
    
    assert dt.productivity[0] == pytest.approx(0.4243156703924034)
    
    assert dt.productivity[199999] == pytest.approx(3.5939198332281443)
    

import pandas as pd

def test_validate() -> None:
    """Test validate with valide DataFrame."""
    from ..data import validate
    assert validate(pd.DataFrame({"cups": [0], "productivity": [1.2]})) is None    
    