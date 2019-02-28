import os
import click
from config_writer import Config as Cfg
from logger_file import Logger

@click.group()
def main():
    '''
     A testing project for blogger-cli project
    '''
    pass

@main.command()
def hi():
    '''
    A comand test if succesfully installed
    '''
    message = '''
            WELCOME TO BLOGGER_CLI
Blogger cli is succesfully installed and working!

use blogger-cli --help for more info!
    '''
    print(message)

@main.command()
@click.option('--remove','-rm',help='key to remove')
@click.option('--test','-t',help='test option')
def config(key, remove, test):
    '''
    give me a suitable key to store
    '''
    arguments = (key, value, all_keys, all_values)
    given_args= [1 for i in arguments if i]
    if given_args == 0:
        print("Running a config setup")
        file = "~/blogger-cli.cfg"
        cfg = Cfg(file)
        key = click.prompt('Input the key to store', default=key)
        cfg.write('key', key)
        test = click.prompt('Input the test to store', default=test)
        logger.debug("written to config file")
    else:
        for args in given_args:
            pass

@click.option('--test','-t',help='test option')
def read(key):
    pass

if __name__ == "__main__":
    logger_cls = Logger(level='debug', console=False)
    logger = logger_cls.get_logger()
    main()
