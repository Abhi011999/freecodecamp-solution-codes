import copy
import random


class Hat:
    def __init__(self, **kwarg):
        contents = []
        for key in kwarg:
            for _ in range(kwarg[key]):
                contents.append(key)
        self.contents = contents

    def draw(self, number):
        contents = self.contents
        draw_ball = []
        if number >= len(contents):
            return contents
        for _ in range(number):
            len_contents = len(contents)
            i = random.randrange(len_contents)
            x = contents[i]
            draw_ball.append(x)
            contents = contents[0:i] + contents[i + 1 :]
        self.contents = contents
        return draw_ball


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    bad = 0

    for _ in range(num_experiments):
        exp_ = copy.deepcopy(hat)
        prova = exp_.draw(num_balls_drawn)
        # print(f'drawn:  {prova} expected: {expected_balls}')
        for v in expected_balls.keys():
            count = sum(prova[x] == v for x in range(len(prova)))
            if count < expected_balls[v]:
                bad += 1
                break

    return 1 - bad / num_experiments
