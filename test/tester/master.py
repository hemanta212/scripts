from slave import run
from otherslave import otherrun
from logger_file import Logger

def main():
    run(Logger)
    otherrun(Logger)

if __name__ == '__main__':
    logger = Logger().get_logger()
    main()
