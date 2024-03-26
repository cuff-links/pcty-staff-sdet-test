from pages.login_page import LoginPage
import requests


class TestEmployeePage():
   
  def teardown_method(self):
      api_url = 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees'
      headers = {
         'Content-type': 'application/json', 
         'Authorization': 'Basic VGVzdFVzZXIzNTk6aWJNTDNjI08pTz9B'
      }
      r = requests.get(api_url, headers=headers)
      for employee in r.json():
         requests.delete('{url}/{id}'.format(url=api_url,id=employee['id']), headers=headers)


  def test_login_and_create_single_employee(self, driver):
    login_page = LoginPage(driver)
    employee_page = login_page.login()
    employee_page.add_new_employee('Joe', 'Schmoe', 1)
    assert employee_page.employee_count == 1

  def test_login_and_create_single_employee_and_update(self, driver):
    login_page = LoginPage(driver)
    employee_page = login_page.login()
    result = employee_page.add_new_employee('Joe', 'Schmoe', 1)
    assert result == True


  def test_login_and_create_employee_and_delete(self, driver):
    login_page = LoginPage(driver)
    employee_page = login_page.login()
    employee_added = employee_page.add_new_employee('Joe', 'Schmoe', 1)
    assert employee_added == True
    employee_deleted = employee_page.delete_employee()
    assert employee_deleted == True


