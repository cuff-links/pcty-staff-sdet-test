from src.calculate_benefits import calculate_dependants_benefits_cost_per_check, calculate_employee_benefits_cost_per_check, calculate_total_benefits_cost_per_check
import pytest

@pytest.mark.parametrize("deps, annual_cost_dep, num_of_checks, expected", 
                         [(0, 500, 26, 0), (1, 500, 26,  19.23), (15, 500, 26,  288.46), (32, 500, 26,  615.38)])
def test_calculate_dependents_benefits_cost(deps, annual_cost_dep, num_of_checks, expected):
  assert round(
    calculate_dependants_benefits_cost_per_check(
      deps=deps, annual_cost_dep=annual_cost_dep, num_of_checks=num_of_checks),
        2) == expected


def test_calculate_employee_benefits_cost():
  assert round(
    calculate_employee_benefits_cost_per_check(1000, 26), 2) == 38.46
  
@pytest.mark.parametrize("deps, annual_cost_emp, annual_cost_dep, num_of_checks, expected", 
                         [(0, 1000, 500, 26, 38.46), (32, 1000, 500, 26,  653.85)])
def test_calculate_total_benefits_cost(deps, annual_cost_emp, annual_cost_dep, num_of_checks, expected):
  assert round(
    calculate_total_benefits_cost_per_check(
      deps=deps, annual_cost_emp=annual_cost_emp, annual_cost_dep=annual_cost_dep, num_of_checks=num_of_checks),
        2) == expected