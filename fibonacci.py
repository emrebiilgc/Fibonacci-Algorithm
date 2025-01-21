import sys


def naive(number, output_file):  # Naive Fibonacci calculation function

    if number > 2:
        output_file.write("fib(%d) = fib(%d) + fib(%d)\n" % (int(number), int(number) - 1, int(number) - 2))
        x = naive(number - 1, output_file) + naive(number - 2, output_file)
        return x
    # only fib(1) and fib(2) are known
    elif number == 1:
        output_file.write("fib(1) = 1\n")
        return 1
    elif number == 2:
        output_file.write("fib(2) = 1\n")
        return 1
    else:
        return 0


def eager(number, output_file):  # Eager Fibonacci calculation function
    if number <= len(memory):
        # only fib(1) and fib(2) are known at first
        if number == 1 or number == 2:
            output_file.write("fib({}) = 1\n".format(number))
        elif number <= 0:
            return 0
        else:
            output_file.write("fib({}) = {}\n".format(number, memory[number - 1]))
        return memory[number - 1]   # memory-1 because of lists

    if number > 2:
        output_file.write("fib({}) = fib({}) + fib({})\n".format(number, number - 1, number - 2))
        x = eager(number - 1, output_file) + eager(number - 2, output_file)
        memory.append(x)    # If a value other than fib(1) or fib(2) is calculated, it is appended to memory.
        return x
    else:
        return 0


def print_to_text(input_file, output_file1, output_file2):
    # Global memory for eager solution
    global memory
    memory = [1, 1]
    # Naive Fibonacci calculations
    for number in input_file:
        output_file1.write("--------------------------------\n")
        output_file1.write("Calculating {}. Fibonacci number:\n".format(number.strip()))
        result = naive(int(number), output_file1)
        if result == 0:
            output_file1.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n")
            output_file1.write("{}. Fibonacci number is: nan\n".format(number.strip()))
        else:
            output_file1.write("{}. Fibonacci number is: {}\n".format(number.strip(), result))
    output_file1.write("--------------------------------")
    input_file.close()
    input_file = open(sys.argv[1], 'r')  # input_file is repopened for eager solution
    # Eager Fibonacci calculations
    for number in input_file:
        output_file2.write("--------------------------------\n")
        output_file2.write("Calculating {}. Fibonacci number:\n".format(number.strip()))
        result = eager(int(number), output_file2)

        if result == 0:
            output_file2.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n")
            output_file2.write("{}. Fibonacci number is: nan\n".format(number.strip()))
        else:
            output_file2.write("{}. Fibonacci number is: {}\n".format(number.strip(), result))

    output_file2.write("--------------------------------\n")
    output_file2.write("Structure for the eager solution:\n")
    output_file2.write("[{}]\n".format(', '.join(map(str, memory))))
    output_file2.write("--------------------------------")


def main():
    input_file = open(sys.argv[1], 'r')
    output_file1 = open(sys.argv[2], 'w')
    output_file2 = open(sys.argv[3], 'w')
    print_to_text(input_file, output_file1, output_file2)
    input_file.close()
    output_file1.close()
    output_file2.close()


if __name__ == '__main__':
    main()
