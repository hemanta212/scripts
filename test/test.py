import os
import click
from config_writer import Config as Cfg
from logger_file import Logger
from cli_utils import Exists, Blog


cfg = Cfg('~/.blogger_cli.cfg', backup_dir='~/.blogger_cli/backup/')
exists = Exists(cfg)
logger_cls = Logger(level='debug', console=False)
logger = logger_cls.get_logger()
 
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
@click.option('--blog', '-b', help='name of the blog')
@click.option('--delete','-d', help='delte config file')
@click.argument('key', nargs=2 )
def config(key, blog, delete):
    '''
    give me a suitable key to store
    '''
    if not blog:
        click.secho("checking for default blog")
    elif blog:
        if exists.blog_exists(blog):
            blog_obj = Blog(cfg, blog)
            if delete:
                response = click.prompt("delete the config file?[y/n]")
                if response.lower == 'y':
                    cfg.delete_config() 
                    return 'deleted config file'
                
            elif key:
                 if len(key) == 1:
                     return blog_obj.get(key[0]) 
                 else:
                    blog_attr = cfg.read(key=blog)
                    if key[0] in blog_attr:
                        blog_obj.add_key(key[0], key[1])
                        print("added",key[1],"to",key[0])
                    else:
                        print("Invalid key used")

@main.command()
@click.option('--setup','-s',help="setup all config values for a blog")
@click.option('--remove','-rm',help="remove a blog")
@click.option('--add','-a',help="add a new blog")
@click.option('--list','-l', help="args (all,key)")
def blog(setup, add, remove, list):
    if add:  
        blog_obj = Blog(cfg, add)
        if not exists.blog_exists(add):
            blog_obj.register() 
            print("Registered", add, "succesfully")
        else:
            click.secho("blog already exists")

    elif setup:
        if exists.blog_exists(setup):
            click.secho("Running a config setup for {0}".format(setup))
            blog_obj = Blog(cfg, setup)
            blog_attr = cfg.read(key=setup)
            for k,v in blog_attr.items():
                value = click.prompt(k, default=v)
                blog_obj.add_key(k, value) 
            click.secho("successfully updated configs")

    elif remove:
        blog_obj = Blog(cfg, remove)
        if not exists.blog_exists(remove):
            print(remove, "doesnot exists")
        else:
            click.secho("removing..")
            blog_obj.delete()
            click.secho("Deleted {0}".format(remove))
    elif list:
        blog_obj = Blog(cfg, setup)
        for i in blog_obj.blogs():
            print(i)
    else:
        click.secho("No option provided")  

if __name__ == "__main__":
    main()
