from locust import HttpLocust, TaskSet, task


class WebTask(TaskSet):

    @task
    def home(self):
        self.client.get("/")


class WebUser(HttpLocust):
    task_set = WebTask
    min_wait = 5000
    max_wait = 5000
