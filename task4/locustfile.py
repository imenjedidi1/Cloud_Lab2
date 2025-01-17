import time
from locust import HttpUser, task, between  # type: ignore

class QuickstartUser(HttpUser):
    @task
    def test_numerical_integration(self):
        # Test the numerical integration function
        self.client.get("/api/numericalintegralfunction")  
