import sys

def helloWorld(name):
    print("Hello, " + name+"!")

def greetEveryone(sys):
    for i in range(len(sys.argv)):
        if(i!=0):
            print("Hello, " + sys.argv[i] + "!")

def main():
    #name = sys.argv[1]
    #helloWorld(name)
    greetEveryone(sys)

if __name__ == "__main__":
    main()