import os
import click
from cli_utils import Config as Cfg
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
    print('''WELCOME TO BLOGGER_CLI
    Blogger cli is succesfully installed and working!

use blogger-cli --help for more info!
    ''')

@main.command()
@click.option('--key','-k',help='testing config writing')
@click.option('--file','-f',help='file to write configs')
@click.option('--remove','-rm',help='key to remove')
@click.option('--test','-t',help='test option')
def config(key, file, remove, test):
    '''
    give me a suitable key to store
    '''
    print("Running a config setup")
    file = "~/blogger-cli.cfg"
    cfg = Cfg(file)
    key = click.prompt('Input the key to store', default=key)
    cfg.write('key', key)
    test = click.prompt('Input the test to store', default=test)
    logger.debug("written to config file")

@click.option('--test','-t',help='test option')
def read(key):
    pass

if __name__ == "__main__":
    logger = Logger(level="debug", console=False).get_logger()
    main()
