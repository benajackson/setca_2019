"""
Test for geom_analysis.py
"""
#conda install pytest-cov

import geom_analysis as ga
import pytest

def test_calculate_distance():
    coord1 = [0,0,2]
    coord2 = [0,0,0]

    observed = ga.calculate_distance(coord1,coord2)
    assert observed == 2

def test_bond_check_false():
    bond_distance = 1.6
    min = 0
    max = 1.5
    observed = ga.bond_check(bond_distance, min, max)
    assert observed == False
def test_bond_check_true():
    bond_distance = 1.4
    min = 0
    max = 1.5
    observed = ga.bond_check(bond_distance, min, max)
    assert observed == True
def test_bond_check_error():
    bond_length = 'a'
    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_length)
