from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class EmployeePage(BasePage):

  _EMPLOYEE_TABLE_LOCATOR = (By.ID, "employeesTable")
  _ADD_EMPLOYEE_BUTTON_LOCATOR = (By.ID, 'add')
  _LOGOUT_BUTTON_LOCATOR = (By.LINK_TEXT, 'Log Out')
  _FIRSTNAME_FIELD_LOCATOR = (By.ID, 'firstName')
  _LASTNAME_FIELD_LOCATOR = (By.ID, 'lastName')
  _ADD_TO_TABLE_BUTTON_LOCATOR = (By.ID, 'addEmployee')
  _DEPENDANTS_FIELD_LOCATOR = (By.ID, 'dependants')
  _EMPLOYEE_TABLE_ROWS_LOCATOR = (By.CSS_SELECTOR, '#employeesTable > tbody > tr')
  _EMPLOYEE_RECORD_DELETE_LOCATOR = (By.CLASS_NAME, 'fa-times')
  _DELETE_EMPLOYEE_MODAL_LOCATOR = (By.ID, 'deleteEmployee')
  _EMPLOYEE_NO_ROWS_CELL_LOCATOR = (By.CSS_SELECTOR, '#employeesTable > tbody > tr > td')


  def __init__(self, driver):
    super().__init__(driver)
    Wait(self.driver, 10).until(
        EC.presence_of_element_located(self._EMPLOYEE_TABLE_LOCATOR)
    )

  @property
  def employees_table(self):
    return self.driver.find_element(*self._EMPLOYEE_TABLE_LOCATOR)
  
  @property
  def employee_delete_button(self):
    return self.driver.find_element(*(self._EMPLOYEE_RECORD_DELETE_LOCATOR))

  @property
  def add_employee_button(self):
    return self.driver.find_element(*self._ADD_EMPLOYEE_BUTTON_LOCATOR)
  
  @property
  def add_employee_info_to_table_button(self):
    return self.driver.find_element(*self._ADD_TO_TABLE_BUTTON_LOCATOR)
  
  @property
  def first_name_input(self):
    return self.driver.find_element(*self._FIRSTNAME_FIELD_LOCATOR)
  
  @property
  def last_name_input(self):
    return self.driver.find_element(*self._LASTNAME_FIELD_LOCATOR)
  
  @property
  def logout_link(self):
    return self.driver.find_element(*self._LOGOUT_BUTTON_LOCATOR)
  
  @property
  def dependant_input(self):
    return self.driver.find_element(*self._DEPENDANTS_FIELD_LOCATOR)
  
  @property
  def employee_count(self) -> int:
    return len(self.driver.find_elements(*self._EMPLOYEE_TABLE_ROWS_LOCATOR))
  
  @property
  def no_employee_rows_text(self) -> str:
    return self.driver.find_element(*self._EMPLOYEE_NO_ROWS_CELL_LOCATOR).text
  
  @property
  def employee_modal_delete_button(self):
    return self.driver.find_element(*(self._DELETE_EMPLOYEE_MODAL_LOCATOR))
  
  def add_new_employee(self, first_name, last_name, deps) -> bool:
    self.add_employee_button.click()
    Wait(self.driver, 10).until(
        EC.presence_of_element_located(self._FIRSTNAME_FIELD_LOCATOR)
    )
    self.first_name_input.send_keys(first_name)
    self.last_name_input.send_keys(last_name)
    self.dependant_input.send_keys(deps)
    self.add_employee_info_to_table_button.click()
    Wait(self.driver, 10).until(
        EC.visibility_of_element_located(self._EMPLOYEE_TABLE_LOCATOR)
    )
    return True

  def delete_employee(self) -> bool:
    self.employee_delete_button.click()
    Wait(self.driver, 10).until(
      EC.visibility_of_element_located(self._DELETE_EMPLOYEE_MODAL_LOCATOR)
    )
    self.employee_modal_delete_button.click()
    Wait(self.driver, 10).until(
        EC.text_to_be_present_in_element(self._EMPLOYEE_NO_ROWS_CELL_LOCATOR, 'No employees found.')
    )
    return True

  def logout(self):
    self.logout_link.click()
    from pages.login_page import LoginPage
    return LoginPage(self.driver)