from Project4.Stack import Stack
from Project4.Stack import reverse


def main():
    stu_stack = Stack(10)
    #stu_stack.push(1)
    for i in range(0, 10):
        stu_stack.push(i)
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))
    stu_stack.pop()
    print(str(stu_stack))




    print("Expected: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] Capacity: 10")
    print("Output:", str(stu_stack))
    print("Top:", stu_stack.top())
    stu_stack = reverse(stu_stack)
    print("Reverse:", stu_stack)


main()
