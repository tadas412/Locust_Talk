import time

debug = False
time_start = time.time()


# Debugger decorator - adds a timer and notes what you're calling/finished
def debug(func):
    if not debug:
        return func

    def debugged_func(*arguments):
        print "Calling function: {0} with args {1}".format(func.__name__,
                                                           arguments)
        print "Seconds since start: {0}".format(time.time() - time_start)
        result = func(*arguments)
        print "Done running: {0}".format(func.__name__)
        return result
    return debugged_func
