import threading
import time
from queue import PriorityQueue
from core2 import ProcessorCoreSRJF 
class Subsystem2:
    def __init__(self, r1_count, r2_count):
        self.r1 = r1_count  
        self.r2 = r2_count  
        self.ready_queue = PriorityQueue()  
        self.cores = [ProcessorCoreSRJF(i, self) for i in range(2)] 
        self.lock = threading.Lock()  
        self.available = [r1_count, r2_count] 
        self.allocation = {} 
        self.maximum = {} 

    def add_task(self, task):
        self.maximum[task.task_id] = [task.required_r1, task.required_r2]
        self.allocation[task.task_id] = [0, 0]  
        if self.banker_algorithm(task) is False:
            print("reject")
            return
        self.ready_queue.put((task.remaining_time, task))
        print(f"Task {task.task_id} added to Ready Queue with remaining time {task.remaining_time}")
        self.preempt_check()

    def check_resources(self, task):
        
        return self.r1 >= task.required_r1 and self.r2 >= task.required_r2

    def allocate_resources(self, task):
       
        with self.lock:
            self.r1 -= task.required_r1
            self.r2 -= task.required_r2

    def release_resources(self, task):
        
        with self.lock:
            self.r1 += task.required_r1
            self.r2 += task.required_r2

    def partial_allocate_resources(self, task):
        
        with self.lock:
            allocated_r1 = min(self.r1, task.required_r1)
            allocated_r2 = min(self.r2, task.required_r2)
            self.r1 -= allocated_r1
            self.r2 -= allocated_r2
            task.required_r1 -= allocated_r1
            task.required_r2 -= allocated_r2
            print(f"Task {task.task_id} partially allocated: R1={allocated_r1}, R2={allocated_r2}")

    def preempt_check(self):
        
        for core in self.cores:
            core.preempt()

    def start(self):
       
        for core in self.cores:
            core.start()

    def stop(self):
        
        for core in self.cores:
            core.running = False
        for core in self.cores:
            core.join()
    def banker_algorithm(self, task):
        
        with self.lock:
           
            work = self.available[:]
            finish = {tid: False for tid in self.maximum}  

            
            need = [self.maximum[task.task_id][0] - self.allocation[task.task_id][0],
                    self.maximum[task.task_id][1] - self.allocation[task.task_id][1]]
            
            if need[0] > self.available[0] or need[1] > self.available[1]:
                
                return False
            
            
            work[0] -= need[0]
            work[1] -= need[1]
            self.allocation[task.task_id][0] += need[0]
            self.allocation[task.task_id][1] += need[1]

           
            while True:
                found = False
                for tid, alloc in self.allocation.items():
                    if not finish[tid]: 
                        task_need = [self.maximum[tid][0] - alloc[0],
                                     self.maximum[tid][1] - alloc[1]]
                        if task_need[0] <= work[0] and task_need[1] <= work[1]:
                           
                            work[0] += alloc[0]
                            work[1] += alloc[1]
                            finish[tid] = True
                            found = True
                            break
                if not found:
                    break
            
            
            if all(finish.values()):
                return True  
            else:
                
                self.allocation[task.task_id][0] -= need[0]
                self.allocation[task.task_id][1] -= need[1]
                return False


