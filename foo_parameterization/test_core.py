import pytest
from foo_parameterization.core import foo_volume

def test_foo_volume():
    assert foo_volume(1) == pytest.approx(4.18879, 0.00001)
    assert foo_volume(2) == pytest.approx(33.51032, 0.00001)
    
    with pytest.raises(ValueError):
        foo_volume(-1)