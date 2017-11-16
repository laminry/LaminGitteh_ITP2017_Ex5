def log(original_function, logfilename="log.txt"):
    def function(*args, **kwargs):
        result = original_function(*args, **kwargs)

        with open(logfilename, "w") as logfile:
            logfile.write("The Function '%s' called with arguments %s and keyword arguments %s. The result %s.\n" % (original_function.__name__, args, kwargs, result))

        return result

    return function
@log
def div(x, y):
    return x / y
with open("log.txt", "r") as logfile:
    print(logfile.read())