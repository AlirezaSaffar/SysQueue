import threading
import time
from queue import PriorityQueue, Queue
from core3 import ProcessorCoreRateMonotonic
from subsystem1 import Subsystem1
from subsystem2 import Subsystem2
class Subsystem3:
    def __init__(self, r1_count, r2_count,subsystem1:Subsystem1,subsystem2:Subsystem2):
        self.r1 = r1_count  
        self.r2 = r2_count  
        self.ready_queue = PriorityQueue()  
        self.waiting_queue = Queue() 
        self.lock = threading.Lock() 
        self.core = ProcessorCoreRateMonotonic(self)  
        self.running = True  
        self.tasks = []
        self.sub1=subsystem1
        self.sub2=subsystem2
        self.num=0
    def add_task(self, task):
       
        with self.lock:
           
            self.tasks.append(task)
            check=self.check_schedulability()
            print(check)
            if check is False:
                if self.num%5 < 3:
                    self.sub1.cores[self.num%3].taskss4=True
                    self.sub1.cores[self.num%3].tasksubnet3=task
                if self.num%5 >2 :
                    self.sub2.cores[self.num-3].taskss4=True
                    self.sub1.cores[self.num%3].tasksubnet3=task
                self.tasks.remove(task)
                self.num= self.num+1
                return
            self.ready_queue.put((task.period,task.task_id, task))
            print(f"Task {task.task_id} added to Ready Queue with period {task.period}")
            
    def check_schedulability(self):
        
        n = len(self.tasks) 
        if n == 0:
            return True 

       
        total_utilization = sum(task.execution_time / task.period for task in self.tasks)
        
        
        u_max = n * (2 ** (1 / n) - 1)

        print(f"Total Utilization: {total_utilization:.4f}, U_max: {u_max:.4f}")

        
        return total_utilization <= u_max
    def check_resources(self, task):
       
        return self.r1 >= task.required_r1 and self.r2 >= task.required_r2
    def allocate_resources(self, task):
       
        self.r1 -= task.required_r1
        self.r2 -= task.required_r2
    def release_resources(self, task):
      
        self.r1 += task.required_r1
        self.r2 += task.required_r2
    def process_waiting_queue(self):
        
        with self.lock:
            for _ in range(self.waiting_queue.qsize()):
                task = self.waiting_queue.get()
                if self.check_resources(task):
                    self.allocate_resources(task)
                    self.ready_queue.put((task.period, task))
                    print(f"Task {task.task_id} moved from Waiting Queue to Ready Queue.")
                else:
                    self.waiting_queue.put(task)  
    def start(self):
       
        self.core.start()
    def stop(self):
        
        self.running = False
        self.core.running = False
        self.core.join()