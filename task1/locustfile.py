import time
from locust import HttpUser, task, between # type: ignore

class QuickstartUser(HttpUser):

    @task
    def test_numerical_integration(self):
        # Test the numerical integration service
        self.client.get("/numericalintegralservice/0/3.14159")
