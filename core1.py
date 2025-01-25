import threading
import time
from queue import Queue
class ProcessorCore(threading.Thread):
    def __init__(self, core_id, ready_queue, subsystem, time_slice):
        super().__init__()
        self.core_id = core_id
        self.ready_queue = ready_queue
        self.subsystem = subsystem
        self.time_slice = time_slice 
        self.running = True
        self.taskss4=False
        self.tasksubnet3=None

    def run(self):
        while self.running:
            if self.taskss4 is True:
                print(f"Core {self.core_id}: Executing Task {self.tasksubnet3.task_id}")
                self.tasksubnet3.execute(1)
                if self.tasksubnet3.remaining_time == 0:
                    self.taskss4=False
                    self.tasksubnet3=None
                continue
                
            if not self.ready_queue.empty():
                task = self.ready_queue.get()
                # task_ids = [task.task_id for task in list(self.ready_queue.queue)]
                # print(f"[CORE1] updated after get: {task_ids}, for core id: {self.core_id}")
                
                if self.subsystem.check_resources(task):
                    print(f"Core {self.core_id}: Executing Task {task.task_id}")
                    weighted_time_slice = self.time_slice * task.weight  
                    time_units = 0
                    while time_units < weighted_time_slice and task.remaining_time > 0:
                        task.execute(1)
                        time_units += 1
                        time.sleep(1)
                    
                    if task.remaining_time > 0:
                        self.ready_queue.put(task)
                    else:
                        print(f"Task {task.task_id} completed on Core {self.core_id}")
                        # self.ready_queue.get()
                    
                    self.subsystem.release_resources(task) 
                else:
                    print(f"Task {task.task_id} moved to Waiting Queue due to insufficient resources")
                    task.state = "Waiting"
                    self.subsystem.add_to_waiting_queue(task)  

            else:
                time.sleep(1)