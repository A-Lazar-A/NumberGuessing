import click
from art import text2art
from random import randint


@click.command()
@click.option('--bottom', default=0, show_default=True, help='Set bottom bound')
@click.option('--up', default=100, show_default=True, help='Set upper bound')
@click.option('--easy', is_flag=True, default=False, show_default=True, help='Set easy mode' )
def guess_the_number(bottom, up, easy):
    print(text2art('Guess The Number'))
    answer = randint(bottom, up)
    guess = int(input(f'Guess the number from {bottom} to {up}\n'))
    if easy:
        while guess != answer:
            if guess < answer:
                print(f'{guess} lower than answer')
            else:
                print(f'{guess} bigger than answer')
            guess = int(input('You are wrong! Try once more\n'))
    else:
        while guess != answer:
            guess = int(input('You are wrong! Try once more\n'))

    print('Congratulations!')


if __name__ == '__main__':
    guess_the_number()
