import os
import click
from cli_utils import config_writer

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
def config(key):
    '''
    give me a suitable key to store
    '''
    config_file = os.path.expanduser('~/.blogger_cli_config.json')
    key = click.prompt('Input the key to store', default=key)
    config_writer(key='key', value=key, file=config_file)

if __name__ == "__main__":
    main()
