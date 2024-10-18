#
#
#

import pytest
from src.ej02_def import total

@pytest.mark.parametrize("cost, horas, expected",[

    (10, 5, 50)

])
def test_total(cost, horas, expected):
    assert total(cost, horas) == expected