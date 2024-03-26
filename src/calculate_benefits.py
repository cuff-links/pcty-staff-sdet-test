NUMBER_OF_PAYCHECKS = 26
ANNUAL_SALARY = 52000.00
ANNUAL_COST_PER_EMPLOYEE = 1000.00
ANNUAL_COST_PER_DEP = 500.00

def calculate_total_benefits_cost_per_check(deps: int, annual_cost_dep=ANNUAL_COST_PER_DEP, annual_cost_emp= ANNUAL_COST_PER_EMPLOYEE, num_of_checks=NUMBER_OF_PAYCHECKS):
  return ( calculate_employee_benefits_cost_per_check(annual_cost_emp, num_of_checks) + calculate_dependants_benefits_cost_per_check(deps, annual_cost_dep, num_of_checks) )

def calculate_employee_benefits_cost_per_check(annual_cost_emp, number_of_checks):
  return (annual_cost_emp / number_of_checks)

def calculate_dependants_benefits_cost_per_check(deps: int, annual_cost_dep, num_of_checks):
  return (annual_cost_dep * deps) / num_of_checks

