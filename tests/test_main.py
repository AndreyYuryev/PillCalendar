import pytest
import sys
from io import StringIO
from main import main_for_test


@pytest.fixture  
def input_data():  
    return 'Пн Вт\nУтро'


@pytest.fixture
def output_data():
    return '0\n1' 


@pytest.mark.parametrize( "input, expected", 
                         ([('Пн Вт\nУтро', '0\n1'), 
                           ('Ср Чт\nДень', '2\n3')]))  
def test_main_for_test(capsys, input, expected, monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO(input))
    main_for_test() 
    captured = capsys.readouterr() 
    result = captured.out.strip() 
    assert result == expected


def test_main_for_test2(capsys, input_data, output_data, monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    main_for_test() 
    captured = capsys.readouterr() 
    result = captured.out.strip() 
    assert result == output_data
    