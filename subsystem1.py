import threading
from core import core
from queue import Queue
from queue import PriorityQueue
def runThread(ReadyQueue,core,number):
    while True:
        task=self.ReadyQueue[number].get()
        self.
        
    return
def runCore(ReadyQueue,core):
    threadCore1= threading.Thread(target=runThread,args=(ReadyQueue,core,0))
    threadCore2= threading.Thread(target=runThread,args=(ReadyQueue,core,1))    
    threadCore3= threading.Thread(target=runThread,args=(ReadyQueue,core,2))
    threadCore1.start()
    threadCore2.start()
    threadCore3.start()
    
    return
class subsystem1:
    def __init__(self,queue):
        self.core=[]
        self.core.append(core())
        self.core.append(core())
        self.core.append(core())
        self.WaitingQueue = Queue()
        self.ReadyQueue = []
        self.ReadyQueue.append(PriorityQueue())
        self.ReadyQueue.append(PriorityQueue())
        self.ReadyQueue.append(PriorityQueue())
        pass
    def addTask(self,task):
        self.WaitingQueue.put(task)
        return
    def run(self):
        thread1=threading.Thread(target=runThread,args=(self.ReadyQueue,self.core))
        thread1.start()
        return
        
