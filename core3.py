import threading
import time
from queue import PriorityQueue, Queue

class ProcessorCoreRateMonotonic(threading.Thread):
    def __init__(self, subsystem):
        super().__init__()
        self.subsystem = subsystem
        self.running = True
        self.current_task = None

    def run(self):
        while self.running:
            if self.current_task is None:  
                self.fetch_task() 
            elif self.current_task.state == "Completed":  
                self.subsystem.release_resources(self.current_task)  
                print(f"Task {self.current_task.task_id} completed and resources released.")
                self.current_task = None
            else:  
                self.execute_task()

            self.subsystem.process_waiting_queue() 
            time.sleep(1)  

    def fetch_task(self):
        if not self.subsystem.ready_queue.empty():
            _, task = self.subsystem.ready_queue.get()
            self.current_task = task
            print(f"Core: Started Task {task.task_id} with period {task.period}")

    def execute_task(self):
        if self.current_task:
            self.current_task.execute(1)  
