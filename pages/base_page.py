class BasePage:

  def __init__(self, driver) -> None:
    self.driver = driver

  def _navigate(self, url):
    self.driver.get(url)

  def refresh(self):
    self.driver.refresh()