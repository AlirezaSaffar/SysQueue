import threading
import time
import random
from queue import Queue
class Task:
    def __init__(self, task_id, execution_time, dependencies=None):
       
        self.task_id = task_id
        self.execution_time = execution_time
        self.dependencies = dependencies if dependencies else []  
        self.remaining_time = execution_time
        self.state = "Ready"  
        self.retry_count = 0 

    def execute(self, time_unit):
        if self.remaining_time > 0:
            self.remaining_time -= time_unit
            print(f"Task {self.task_id}: Remaining time = {self.remaining_time}")
            if self.remaining_time <= 0:
               
                if random.random() <= 0.3:
                    self.state = "Error"
                    self.retry_count += 1
                    print(f"Task {self.task_id}: Error occurred! Retrying...")
                else:
                    self.state = "Completed"
                    print(f"Task {self.task_id}: Completed successfully.")
            return self.remaining_time
        else:
            return 0
