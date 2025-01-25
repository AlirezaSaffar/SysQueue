import threading
import time
import random
from queue import Queue
from ss4task import Task


class ProcessorCoreFCFS(threading.Thread):
    def __init__(self, core_id, subsystem):
        super().__init__()
        self.core_id = core_id
        self.subsystem = subsystem
        self.running = True
        self.current_task = None

    def run(self):
        while self.running:
            if not self.current_task:
                self.fetch_task()  
            elif self.current_task.state == "Error":
                self.retry_task() 
            elif self.current_task.state == "Completed":
                self.complete_task()  
            else:
                self.execute_task() 

            self.subsystem.process_waiting_queue() 
            time.sleep(1) 

    def fetch_task(self):
        if not self.subsystem.ready_queue.empty():
            self.current_task = self.subsystem.ready_queue.get()
            print(f"Core {self.core_id}: Started Task {self.current_task.task_id}.")

    def execute_task(self):
        if self.current_task:
            self.current_task.execute(1)  

    def retry_task(self):
        print(f"Core {self.core_id}: Retrying Task {self.current_task.task_id}.")
        self.current_task.remaining_time = self.current_task.execution_time 
        self.current_task.state = "Ready"  

    def complete_task(self):
        print(f"Core {self.core_id}: Task {self.current_task.task_id} completed.")
        self.subsystem.release_resources(self.current_task) 
        self.subsystem.completed_tasks.add(self.current_task.task_id) 
        self.current_task = None  
        