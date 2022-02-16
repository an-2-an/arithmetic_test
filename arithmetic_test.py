import random

RIGHT, WRONG = 'right!', 'wrong!'

def get_expression():
    a, b = (random.randint(2, 9) for _ in range(2))
    operation = random.choice('+*')
    expression = f'{a} {operation} {b}'
    return expression


def is_correct(expression, answer):
    return eval(expression) == answer


def get_answer():
    got = input('> ')
    return int(got)



def main():
    expression = get_expression()
    print(expression)
    try:
        answer = get_answer()
        if is_correct(expression=expression, answer=answer):
            print(RIGHT)
        else:
            print('WRONG')
    except ValueError:
        pass



if __name__ == '__main__':
    main()