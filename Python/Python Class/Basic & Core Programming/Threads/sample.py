'''
    (1).. using a function
         t=Thread(target=functionName,arg)
         t.start()

    (2)..Extending the thread class
        class MyThread(Thread)
        override the run()
        t.start()


    (3)..hibrid
      class myThread
      display()
      t=Thread(target=myobj.display,args)
      t.start()
'''


#main thread
import threading
print("Current thread that is running:",threading.current_thread().getName())
if threading.current_thread()==threading.main_thread():
    print("main thread")
else:                            # comparing main thread with other thread
    print("some other thread")
