import time
import requests
from faker import Faker
import random
from locust import HttpUser, task, between

class EmployeeApiUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.client.headers = {
      'Content-type': 'application/json', 
      'Authorization': 'Basic VGVzdFVzZXIzNTk6aWJNTDNjI08pTz9B'
    }
        
    def on_stop(self):
        api_url = 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees'
        r = requests.get(api_url, headers=self.client.headers)
        for employee in r.json():
          requests.delete('{url}/{id}'.format(url=api_url,id=employee['id']), headers=self.client.headers)
          

    @task(1)
    def post_employee(self):
        fake = Faker()
        data = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "dependants": random.randint(0, 32)
        }
        self.client.post("/employees", json=data)
        time.sleep(.5)

    @task(2)
    def get_all_employees(self):
        self.client.get("/employees")