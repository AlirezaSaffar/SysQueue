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
