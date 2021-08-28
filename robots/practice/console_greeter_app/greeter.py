import os


def greet(name):
    msg = os.environ.get("GREET_MSG", "Hello")    
    return "{} {}".format(msg, name)


if __name__ == '__main__':
    print(greet("Prem"))
