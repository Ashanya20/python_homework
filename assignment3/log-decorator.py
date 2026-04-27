# Task 1: Writing and Testing a Decorator

# one time setup
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# Decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # Log function name
        log_msg = f"function: {func.__name__}\n"
        # Log positional args
        if args:
            log_msg += f"positional parameters: {list(args)}\n"
        else:
            log_msg += "positional parameters: none\n"
        # Log keyword args
        if kwargs:
            log_msg += f"keyword parameters: {kwargs}\n"
        else:
            log_msg += "keyword parameters: none\n"
        # Call function and get result
        result = func(*args, **kwargs)
        # Log return value
        log_msg += f"return: {result}\n"
        # Write to log
        logger.log(logging.INFO, log_msg)
        return result
    return wrapper

# Functions
@logger_decorator
def say_hello():
    print("Hello, World!")
    return None

@logger_decorator
def take_args(*args):
    return True

@logger_decorator
def take_kwargs(**kwargs):
    return logger_decorator

# Mainline
if __name__ == "__main__":
    say_hello()
    take_args(1, 2, 3, "test")
    take_kwargs(a=10, b=20)
# to print run: cat decorator.log