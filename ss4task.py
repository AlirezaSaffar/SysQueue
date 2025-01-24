import random
class Task:
    def __init__(self, task_id, execution_time, required_r1, required_r2, dependencies=None):
        
        self.task_id = task_id
        self.execution_time = execution_time
        self.remaining_time = execution_time
        self.required_r1 = required_r1
        self.required_r2 = required_r2
        self.dependencies = dependencies if dependencies else []  
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
