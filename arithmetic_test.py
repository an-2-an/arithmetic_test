import random

RIGHT, WRONG = 'right!', 'wrong!'
INCORRECT = 'Incorrect format'
correct_answers = 0

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
    global correct_answers
    for i in range(5):
        expression = get_expression()
        print(expression)
        while True:
            try:
                answer = get_answer()
                if is_correct(expression=expression, answer=answer):
                    print(RIGHT + '\n')
                    correct_answers += 1
                else:
                    print(WRONG + '\n')
                break
            except ValueError:
                print(INCORRECT)
    print(f'Your mark is {correct_answers}/5.')



if __name__ == '__main__':
    main()