class Task:
    def __init__(self, task_id, execution_time, weight, required_r1, required_r2):
        self.task_id = task_id
        self.execution_time = execution_time
        self.remaining_time = execution_time
        self.weight = weight  
        self.state = "Ready"  
        self.required_r1 = required_r1
        self.required_r2 = required_r2

    def execute(self, time_unit):
        if self.remaining_time > 0:
            self.remaining_time -= time_unit
            print(f"Task {self.task_id}: Remaining time = {self.remaining_time}")
            if self.remaining_time <= 0:
                self.state = "Completed"
            return self.remaining_time
        else:
            return 0
