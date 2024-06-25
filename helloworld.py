import sys

def helloWorld(name):
    print("Hello, " + name+"!")

def main():
    name = sys.argv[1]
    helloWorld(name)

if __name__ == "__main__":
    main()