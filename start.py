from fibonacci_iterator import Fibonacci


def main():
    """
    Example of using:

    "Fibonacci iterator" started!
    Enter index of first elem [default 0]: 0
    Enter index of last elem [default 100]: 10
    Enter index of elem where iteration starts [default 0]: 5
    Enter "+" or "-" to iter next or previous fibonacci value. "exit" to end program.
    -> +
    8
    -> +
    13
    -> -
    8
    -> -
    5
    -> exit
    End.
    """
    def _do_command(_f, _command):
        try:
            if command == '+':
                print(f'{right_iterator.next()}')
            elif command == '-':
                print(f'{reverse_iterator.next()}')
            elif command == 'exit':
                print('End.')
                exit()
        except StopIteration as e:
            print(e)

    print('"Fibonacci iterator" started!')
    first = int(input('Enter index of first elem [default 0]: ') or 0)
    last = int(input('Enter index of last elem [default 100]: ') or 100)
    start = int(input('Enter index of elem where iteration starts [default 0]: ') or 0)

    fib = Fibonacci(first=first, last=last, start=start)
    right_iterator = fib.right_order_iterator()
    reverse_iterator = fib.reverse_order_iterator()

    print('Enter "+" or "-" to iter next or previous fibonacci value. "exit" to end program.')

    while True:
        command = input('-> ')
        _do_command(fib, command)


if __name__ == '__main__':
    main()
