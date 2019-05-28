from locust import HttpLocust, TaskSet, task

class BasicTaskSet(TaskSet):

    @task(1)
    def demo(self):
        self.client.get('/')

    @task(2)
    def main(self):
      self.client.get('/')

class BasicTasks(HttpLocust):
    task_set = BasicTaskSet
    min_wait = 5000
    max_wait = 10000