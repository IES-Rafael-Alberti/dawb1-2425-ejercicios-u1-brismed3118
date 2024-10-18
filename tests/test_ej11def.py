#
#
#

import pytest
from src.ej11_def import calculo

@pytest.mark.parametrize("num, expected",[

    (10, "55.0")

])
def test_calculo(num, expected):
    assert calculo(num) == expected