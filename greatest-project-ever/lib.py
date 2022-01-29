import argparse, random
from termcolor import colored


def try_me(sign,payment):
    planets = ['Saturn', 'Mars', 'Jupyter', 'Uranus', 'Venus', 'The Moon', 'The Sun']
    funny_fortunes = ['see a ghost!', 'learn to play the piano!', 'win a fortune!', "'get lucky'!",'eat a burger!']
    bad_fortunes = ['get bitten by a dog!', 'slip on a bannana peel!', 'catch a cold!','hit your toe on a table corner!','get hit in the face with a cake!']

    if payment <= 0:
        answer = "You cheap bastard!"

    elif payment < 20:
        answer = f"You are unlucky for being a {sign}, tonight {random.choice(planets)} is passing in front of {random.choice(planets)} and you will {random.choice(bad_fortunes)}"

    elif payment >= 20:
        answer = f"You are in luck for being a {sign}, tonight {random.choice(planets)} is passing in front of {random.choice(planets)} and you will {random.choice(funny_fortunes)}"

    return answer


if __name__ == '__main__':
    description = 'stkrgcp_description'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--fortune',
                        nargs='+',
                        help='zodiac sign and payment',
                        required=False)
    parser.add_argument('--prod',
                        action='store_true',
                        default=False,
                        help='Example here')
    args = parser.parse_args()
    sign, payment = args.fortune
    answer = try_me(str(sign), int(payment))
    print(colored("###### YOUR FORTUNE ######", "blue"))
    print(colored(answer, "red"))
