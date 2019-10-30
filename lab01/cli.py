import click

@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('-n', '--name', help='Name of person to be greeted', required=True)
def hello(count, name):
    for x in range(count):
        print(f'Hello {name}')

if __name__ == '__main__':
    hello()