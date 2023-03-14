from Task2 import logger


@logger('log_4.log')
def test_def(a, b):
    return a + b


if __name__ == '__main__':
    test_def(1234, 3466436)
    test_def(536743, 35467567)
    test_def(1242, 18765)