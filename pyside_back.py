from PySide6.QtCore import QObject, Property, Signal
import threading
import time

class Monitorer(QObject):
    def __init__(self):
        super().__init__()
        self.subsys1 = "help me god"  # Private attribute to store the actual value
        t = threading.Thread(target=self.the_main_func)
        t.start()    
        
    def get_subsys1(self):
        return self.subsys1
    
    def set_subsys1(self, value):
        print("the subsys is being called.")
        if self.subsys1 != value:
            self.subsys1 = value
            self.subsys1_changed.emit()  # Emit the signal when the value changes
    
    subsys1_changed = Signal()
    
    subsys1_pyside = Property(str, get_subsys1, set_subsys1, notify=subsys1_changed)


    def the_main_func(self):
        # Initialize arrays for subsystems and tasks
        subsystem_tasks = [[] for _ in range(4)]  # Create a list to store tasks for each subsystem
        subsys_resource = []

        # Step 1: Read resource allocation for each subsystem
        print("Enter resources for each subsystem:")
        for i in range(4):
            line = input()
            subsys_resource.append(list(map(int, line.split())))

        print("Subsystem Resources:", subsys_resource)

        # Step 2: Read tasks for each subsystem
        print("\nEnter tasks for each subsystem (end input for a subsystem with #):")
        for i in range(4):
            print(f"\nSubsystem {i + 1}:")
            tasks = []
            while True:
                line = input()
                if line == "$":  # Separator for subsystems
                    break

                task_details = line.split()
                task_name = task_details[0]
                task_len = int(task_details[1])
                resource1 = int(task_details[2])
                resource2 = int(task_details[3])
                enter_time = int(task_details[4])

                # Add specific fields based on the subsystem
                if i == 0:  # Subsystem 1
                    dest_cpu = int(task_details[5])
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                        "dest_cpu": dest_cpu,
                    }
                elif i == 1:  # Subsystem 2
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                    }
                elif i == 2:  # Subsystem 3
                    period = int(task_details[5])
                    num_repeats = int(task_details[6])
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                        "period": period,
                        "num_repeats": num_repeats,
                    }
                elif i == 3:  # Subsystem 4
                    pre_requisite = task_details[5]
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                        "pre_requisite": pre_requisite,
                    }

                tasks.append(task)

            subsystem_tasks[i] = tasks

        # Step 3: Print the collected tasks
        for i, tasks in enumerate(subsystem_tasks):
            print(f"\nTasks for Subsystem {i + 1}:")
            for task in tasks:
                print(task)

                
        # print("Enter the input:")
        # mystr = str(input())
        # if mystr == "hi":
        #     # Update subsys1
        #     self.set_subsys1("////////////////////////////////////////////////////////////////////////////////")
        #     print("The setter is being called.")
            
        # second_thread = threading.Thread(target=self.additional_task, args=("sd",))
        # second_thread.start()
        
        # for i in range(5):
        #     time.sleep(1)
        #     print(f"this is still main")

    def additional_task(self, hi):
        print(f"Additional thread running with argument: {hi}")
        # Perform any additional work in this thread
        for i in range(5):
            time.sleep(1)
            print(f"Additional task iteration {i}: {hi}")
        
