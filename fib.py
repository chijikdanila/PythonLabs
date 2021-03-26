import logging


logging.basicConfig(filename="fib.log", level=logging.INFO)


def fib(n):

    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():

    for i in range(1, 10):
        logging.info(fib(i))


if __name__ == "__main__":
    main()
