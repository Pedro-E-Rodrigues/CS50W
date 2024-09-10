def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")

@announce
def hello():
    print("Hello World")

hello()            