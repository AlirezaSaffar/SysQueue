import threading
import time

class LoggerThread(threading.Thread):
    def __init__(self, barrier, subsystems):
        super().__init__()
        self.barrier = barrier
        self.subsystems = subsystems
        self.current_time = 0
        self.running = True
        
    def run(self):
        while self.running:
            # 1) Wait for all cores to reach the end of their quantum
            try:
                self.barrier.wait()
            except threading.BrokenBarrierError:
                break
            
            # 2) Now *all* cores have completed a scheduling step for "current_time"
            #    Print the system snapshot
            self.print_system_snapshot(self.current_time)
            self.current_time += 1
            
            # 3) Wait again so the cores can start the next quantum
            #    This second wait ensures the logger doesn't race ahead
            try:
                self.barrier.wait()
            except threading.BrokenBarrierError:
                break

    def print_system_snapshot(self, t):
        print(f"\nTime: {t}")
        for i, subsystem in enumerate(self.subsystems, start=1):
            print(f"Sub{i}:")
            # Print resources
            print(f"  Resources: R1: {subsystem.r1} R2: {subsystem.r2}")
            
            # If subsystem has a waiting queue
            if hasattr(subsystem, 'waiting_queue'):
                waiting_list = list(subsystem.waiting_queue.queue)
                print(f"  Waiting Queue: {[task.task_id for task in waiting_list]}")
            
            # If subsystem has multiple ready queues (like Subsystem1)
            if hasattr(subsystem, 'ready_queues'):
                for core_index, queue in enumerate(subsystem.ready_queues):
                    q_list = list(queue.queue)
                    print(f"  Core{core_index}:")
                    # Print running task
                    running_task_id = self.get_running_task_id(subsystem, core_index)
                    print(f"    Running Task: {running_task_id if running_task_id else 'idle'}")
                    # Print ready queue
                    print(f"    Ready Queue: {[t.task_id for t in q_list]}")
            
            # If subsystem has a single PriorityQueue or ready_queue
            elif hasattr(subsystem, 'ready_queue'):
                # For SRJF (Subsystem2) or RateMonotonic (Subsystem3)
                print(f"  Ready Queue: {self.inspect_priority_queue(subsystem.ready_queue)}")
                
                # Print each core’s running task
                if hasattr(subsystem, 'cores'):
                    for c_index, core in enumerate(subsystem.cores):
                        rt = self.get_core_running_task_id(core)
                        print(f"  Core{c_index+1}: Running Task: {rt if rt else 'idle'}")
                # or if subsystem3 has a single core
                elif hasattr(subsystem, 'core'):
                    rt = self.get_core_running_task_id(subsystem.core)
                    print(f"  Core1: Running Task: {rt if rt else 'idle'}")

    def get_running_task_id(self, subsystem, core_index):
        """Return the task_id of the running task on a specific core (if any)."""
        try:
            core = subsystem.cores[core_index]
            # Many of your cores have `current_task` or `tasksubnet3` or `taskss4`
            # Adjust as necessary:
            if hasattr(core, 'current_task') and core.current_task is not None:
                return core.current_task.task_id
            elif hasattr(core, 'tasksubnet3') and core.tasksubnet3 is not None:
                return core.tasksubnet3.task_id
        except IndexError:
            pass
        return None

    def get_core_running_task_id(self, core):
        """Similar helper for subsystems that have a single ready queue and 2 or 1 cores."""
        if hasattr(core, 'current_task') and core.current_task is not None:
            return core.current_task.task_id
        if hasattr(core, 'tasksubnet3') and core.tasksubnet3 is not None:
            return core.tasksubnet3.task_id
        # fallback
        return None

    def inspect_priority_queue(self, pq):
        """Return a list of task_ids in the priority queue without popping them."""
        with pq.mutex:
            # pq.queue is a list of (priority, Task) or (remaining_time, Task)
            return [item[1].task_id for item in pq.queue]