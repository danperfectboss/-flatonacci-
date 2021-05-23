import pytest
from Flatonacci import validate_input_data

@pytest.mark.parametrize(
    "N, signature_list, expected", [
        (8,[2,3,4],True),
        (-5,[2,3,4],True),
        ("abc",[2,3,4],True),
        ("abc",[2],True),
        (8,[2,35],True),
        (10,[2],True),
        ("4",[2,3,4,5,6],True),
        (4,[2,3,4,5,6],True),
        (8,[1, 1, 1],True),
        (10,[0, 0, 1],True)

    ]
)
def test_type_n(N, signature_list,expected):
    assert validate_input_data(N,signature_list) == expected


def test_raise_errors():
    with pytest.raises(ValueError):
        validate_input_data(-2,[1,2,3])
    
    with pytest.raises(ValueError):
        validate_input_data(2,[3])
    
    with pytest.raises(TypeError):
        validate_input_data("1209380",[3,23,5,6])
