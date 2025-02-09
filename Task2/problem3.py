def process(operations, command):
    comm = command[0]

    if comm == "print":
        print(operations)
    elif comm == "pop":
        operations.pop()
    elif comm == "reverse":
        operations.reverse()
    elif comm == "sort":
        operations.sort()
    elif comm == "insert":
        pos = int(command[1])
        e = int(command[2])
        operations.insert(pos, e)
    elif comm == "remove":
        e =int(command[1])
        operations.remove(e)
    elif comm == "append":
        e =int(command[1])
        operations.append(e)


operations = []
n = int(input("enter the n lines of commands: "))
for i in range(n):
    command = input("enter command: ").lower().split()
    process(operations, command)