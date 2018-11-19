import constants as c
from random import choice, sample

def review():
    template = choice(c.TEMPLATES)
    opinion = choice(c.OPINIONS)
    x, y = sample(c.INGREDIENTS, 2)

    sub = template.format(x, y)
    return '{} {}'.format(sub, opinion)

if __name__ == '__main__':
    for i in range(0, 5):
        print(review())
