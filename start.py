from fibonacci_iterator import Fibonacci


def main():

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

    f = Fibonacci(first=first, last=last, start=start)
    right_iterator = f.right_order_iterator()
    reverse_iterator = f.reverse_order_iterator()

    print('Enter "+" or "-" to iter next or previous fibonacci value. "exit" to end program.')

    while True:
        command = input('-> ')
        _do_command(f, command)


if __name__ == '__main__':
    main()
