import time

do_debug = False # Potentially changed by command line args in app.py
time_start = time.time()

def set_debug(val):
    global do_debug
    do_debug = val

# Debugger decorator - adds a timer and notes what you're calling/finished
def debug(func):
    def debugged_func(*arguments):
        if not do_debug:
            return func(*arguments)
        print "Calling function: {0} with args {1}".format(func.__name__,
                                                           arguments)
        print "Seconds since start: {0}".format(time.time() - time_start)
        result = func(*arguments)
        print "Done running: {0}".format(func.__name__)
        return result
    return debugged_func
