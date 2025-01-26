# RT-Sceduling
This is a project of task sceduling and soruce sceduling of Dr.Allah Bakhsh. Implemented by Afshar and Saffar. 
there is a system that includes 4 subsystems. and also, as we implement the forntend (with qt/qml/pyside6), there is also a thread for frontend.

#### A queick overview of our implementation:
if you openup the main.py, you see nothing special nor readable. that is beacuse in the main, we just open up the frontend logic class, which is the pyside_back.
about that `pyside_back.py` : that is where everything is managed.
there are several setter and getters, dont mind those, as they relate to the front end. the front end file is the single file of main.qml btw.
as you see, in the `Monitorer` class, which is the main class of the app, it inherites from the QObject, which is also related to the qt, and you dont nedd to mind that either, but the important thing is in the constructor, which we got the :
```python
t = threading.Thread(target=self.the_main_func)
        t.start()
```
and that is where the whole logic for those 3 subsyses are managed. this way by adding a thread to that, in makes sure both fornt-end and back are synchronized perfectly.
ok, now that the schema is known, lets go back to the project itself:
- **Subsystems with Ready and Waiting Queues.**
- **Three scheduling algorithms:** 
  - Weighted Round Robin (First Subsystem)
  - Shortest Remaining Time First (Second Subsystem)
  - Rate Monotonic (Third Subsystem)
  - SCFS (the fourth)

which we have implemented all of those. even the forth one. 
you would see this file format:

- core_i.py
which belongs to and specialized to the subsys_i th.
there are also two different classes related to tasks:
- task.py
- ss4task.py
- realtimetask.py
which the task.py implements the ones for the subsys1 and subsys2. also there is ss4task for subsys4 and realtimetask for subsys3.

### load balancing on the subsys1:
as the tasks arived to the subsys1, the tasks are assigned in the format of 1, 2, 3, 1, 2, 3, and so on and that way, it is made sure that the balancing is done.
### deadlock on subsys2:
for that, we used the bancker algorighm, which handles the deadlock smoothly and nicly.
### resource shiar on subsys3:
we got a func on subsys3 named as `check_schedulability`, which is having the job of making sure if one task is feasible to be done. if not, it gets help from other subsyses. 
### reapeated task on subsys4:
there is a chance of 30 % of an error on a task , which we handle that agian.
