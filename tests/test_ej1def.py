#
#
#

import pytest
from src.ej01_def import cadena

@pytest.mark.parametrize("nombre, expected", [

    ("benito", "Hola benito"),
    ("pablo", "Hola pablo")

])
def test_cadena(nombre, expected):
    assert cadena(nombre) == expected