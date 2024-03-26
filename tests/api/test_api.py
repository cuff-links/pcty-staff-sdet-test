import pytest
import requests


class TestEmployeeApi():
      
      api_url = 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees'
      headers = {
         'Content-type': 'application/json', 
         'Authorization': 'Basic VGVzdFVzZXIzNTk6aWJNTDNjI08pTz9B',
         'Accept':'application/json'
      }
      
      def test_get_all_employees(self):
        r = requests.get(self.api_url, headers=self.headers)
        assert len(r.json()) == 0

      def test_add_employee(self):
          data = {
              'firstName': 'Joe',
              'lastName': 'Schmoe',
              'dependants': 1
          }
          r = requests.post(self.api_url, headers=self.headers, json=data)
          r2 = requests.get(self.api_url, headers=self.headers)
          
          assert r.status_code == 200

          json = r2.json()
          assert len(json) == 1

          assert json[0]['firstName'] == data['firstName']
        
      
      def test_update_employee(self):
          initial_id = requests.get(self.api_url, headers=self.headers).json()[0]['id']
          data = {
              'id': initial_id,
              'firstName': 'James',
              'lastName': 'Jones',
              'dependants': 2
          }
          r = requests.put(self.api_url, headers=self.headers, json=data)
          r2 = requests.get(self.api_url, headers=self.headers)

          assert r.status_code == 200
          json = r2.json()

          assert len(json) == 1
          assert json[0]['firstName'] == data['firstName']

      def test_delete_employee(self):
          initial_id = requests.get(self.api_url, headers=self.headers).json()[0]['id']
          r2 = requests.delete('{0}/{1}'.format(self.api_url, initial_id), headers=self.headers)

          assert r2.status_code == 200
          r3 = requests.get(self.api_url, headers=self.headers).json()

          # Check if employee is deleted.
          assert len(r3) == 0

