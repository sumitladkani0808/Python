from time import sleep


def hello():
    sleep(3)
    print('Hello!')


if __name__ == '__main__':
    for _ in range(10):
        hello()
