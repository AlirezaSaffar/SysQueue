import threading
import time
from queue import PriorityQueue

class ProcessorCoreSRJF(threading.Thread):
    def __init__(self, core_id, subsystem):
        super().__init__()
        self.core_id = core_id
        self.subsystem = subsystem
        self.running = True
        self.current_task = None
        self.taskss4=False
        self.tasksubnet3=None

    def run(self):
        while self.running:
            if self.taskss4 is True:
                print(f"Core {self.core_id}: Executing Task {self.tasksubnet3.task_id}")
                self.tasksubnet3.execute(1)
                if self.tasksubnet3.remaining_time is 0:
                    self.taskss4=False
                    self.tasksubnet3=None
                continue
            
            if not self.current_task:
                
                self.fetch_task()
            elif self.current_task.state == "Completed":
               
                self.subsystem.release_resources(self.current_task)
                print(f"Core {self.core_id}: Task {self.current_task.task_id} completed.")
                self.current_task = None
            else:
               
                self.execute_task()

            time.sleep(1)  

    def fetch_task(self):
        if not self.subsystem.ready_queue.empty():
            _, task = self.subsystem.ready_queue.get()
            if self.subsystem.check_resources(task):
               
                self.subsystem.allocate_resources(task)
                self.current_task = task
                print(f"Core {self.core_id}: Started Task {task.task_id} with remaining time {task.remaining_time}")
            else:
               
                self.subsystem.partial_allocate_resources(task)
                self.subsystem.ready_queue.put((task.remaining_time, task)) 

    def execute_task(self):
        if self.current_task:
            self.current_task.execute(1) 

    def preempt(self):
   
        if not self.subsystem.ready_queue.empty():
            next_task_time, next_task = self.subsystem.ready_queue.queue[0]  
            if self.current_task and next_task_time < self.current_task.remaining_time:
                print(f"Core {self.core_id}: Preempting Task {self.current_task.task_id} for Task {next_task.task_id}")
                self.subsystem.ready_queue.put((self.current_task.remaining_time, self.current_task)) 
                self.subsystem.release_resources(self.current_task)
                self.current_task = None