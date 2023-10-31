#Juan Islas
#31/10/2023
#Prove that I can write a Python program and write and run test functions to help me find and fix mistakes in the program.
#Sources: CSE111 lessons

from pytest import approx
from water_flow import ji_water_column_height, ji_pressure_gain_from_water_height, ji_pressure_loss_from_pipe, ji_pressure_loss_from_fittings, ji_reynolds_number, ji_pressure_loss_from_pipe_reduction
import pytest

def test_ji_water_column_height():
    #calls water_column_height four times to verify that it is working correctly
    assert ji_water_column_height(0, 0) == 0
    assert ji_water_column_height(0, 10) == 7.5
    assert ji_water_column_height(25, 0) == 25
    assert ji_water_column_height(48.3, 12.8) == 57.9


def test_ji__pressure_gain_from_water_height():
    #calls pressure_gain_from_water_height three times to verify that it is working correctly
    assert ji_pressure_gain_from_water_height (0) == 0
    assert ji_pressure_gain_from_water_height (30.2) == approx(295.628, abs=0.001)
    assert ji_pressure_gain_from_water_height (50) == approx(489.450, abs=0.001)


def test_ji__pressure_loss_from_pipe():
    #calls pressure_loss_from_pipe seven times to verify that it is working correctly
    assert ji_pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert ji_pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert ji_pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert ji_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert ji_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert ji_pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert ji_pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_ji__pressure_loss_from_fittings():
    #calls pressure_loss_from_fittings five times to verify that it is working correctly
    assert ji_pressure_loss_from_fittings (0,3) == approx(0, abs=0.001)
    assert ji_pressure_loss_from_fittings (1.65,0) == approx(0, abs=0.001)
    assert ji_pressure_loss_from_fittings (1.65,2) == approx(-0.109, abs=0.001)
    assert ji_pressure_loss_from_fittings (1.75,2) == approx(-0.122, abs=0.001)
    assert ji_pressure_loss_from_fittings (1.75,5) == approx(-0.306, abs=0.001)

def test_ji__reynolds_number():
    #calls reynolds_number five times to verify that it is working correctly
    assert ji_reynolds_number (0.048692,0) == approx(0, abs= 1)
    assert ji_reynolds_number (0.048692,1.65) == approx(80069, abs= 1)
    assert ji_reynolds_number (0.048692,1.75) == approx(84922, abs= 1)
    assert ji_reynolds_number (0.28687,1.65) == approx(471729, abs= 1)
    assert ji_reynolds_number (0.28687,1.75) == approx(500318, abs= 1)

def test_ji__pressure_loss_from_pipe_reduction():
    #calls pressure_loss_from_pipe_reduction three times to verify that it is working correctly
    assert ji_pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692)== approx(0, abs= 0.001)
    assert ji_pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)== approx(-163.744	, abs= 0.001)
    assert ji_pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)== approx(-184.182	, abs= 0.001)

pytest.main(["-v", "--tb=line", "-rN", __file__])  




