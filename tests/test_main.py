import pytest
import subprocess
import sys
from io import StringIO
from main_test import main_for_test


@pytest.fixture  
def input_data():  
    #return 'Пн Вт\nУтро'
    with open("./tests/input.txt", "r", encoding='utf-8') as file_i:
        input_value = file_i.read()
    return input_value


@pytest.fixture
def output_data():
    #return '0\n1'
    with open("./tests/output.txt", "r", encoding='utf-8') as file_o:
        output_value = file_o.read()
    return output_value 


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
    
def test_main_for_test3():
    with open("./tests/input.txt", "r", encoding='utf-8') as file_i:
        input_value = file_i.read()
    with open("./tests/output.txt", "r", encoding='utf-8') as file_o:
        output_value = file_o.read()
    result = subprocess.run([sys.executable, './main_test.py'], input=input_value, capture_output=True, text=True)
    assert  result.stdout.rstrip('\n') == output_value
    