from utils import add
import pytest

def setup_module():
  print("module sets up")

def teardown_module():
  print("module ends")

def setup_function():
  print("before each test")

def teardown_function():
  print("after each test")

def test_add_zeros():
  # Arrange / Given
  # Act     / When
  result = add(0,0)
  # Assert  / Then
  assert result == 0

def test_adds_two_negative_numbers_properly():
  result = add(-4, -6)
  assert result == -10

def test_raises_a_value_error_if_adding_non_numbers():
  with pytest.raises(ValueError):
    add("a", "b")  

@pytest.mark.parametrize('input1, input2, expected', [
 (1,1,2),
 (-1, 0, -1),
 (1.1, -0.1, 1.0)
])
def test_all_additions_are_correct(input1, input2, expected):
  result = add(input1, input2)
  assert result == expected

@pytest.fixture
def data_list():
  return [4,1,6,1,7,8, 0, 10]

# @pytest.fixture
# def calculator():
#   return Calculator()

def test_max_of_a_list(data_list):
  assert max(data_list) == 10

def test_min_of_a_list(data_list):
  assert min(data_list) == 0