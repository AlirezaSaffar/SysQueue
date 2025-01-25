import threading
import time

class Worker(threading.Thread):
    def __init__(self, barrier, thread_id):
        super().__init__()
        self.barrier = barrier
        self.thread_id = thread_id

    def run(self):
        for step in range(3):
            # Simulate doing some "work"
            print(f"[Thread {self.thread_id}] Starting step {step}")
            time.sleep(0.2 * (self.thread_id + 1))  # just to vary the timing
            
            print(f"[Thread {self.thread_id}] Finished step {step}, waiting at barrier...")
            
            # Wait at the barrier
            self.barrier.wait()
        
        print(f"[Thread {self.thread_id}] All steps are done!")

def main():
    # We have 3 threads (workers), so make a barrier for 3 parties:
    num_threads = 3
    barrier = threading.Barrier(num_threads)
    
    # Create and start each thread
    threads = [Worker(barrier, i) for i in range(num_threads)]
    for t in threads:
        t.start()
    
    # Wait for all threads to finish
    for t in threads:
        t.join()
    
    print("All worker threads have finished execution!")

if __name__ == "__main__":
    main()
