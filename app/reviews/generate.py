import constants as c
from random import choice, sample, randint

def review():
    template = choice(c.TEMPLATES)
    opinion = choice(c.OPINIONS)
    x, y = sample(c.INGREDIENTS, 2)

    sub = template.format(x, y)
    stars = c.STAR * randint(1, 3)

    return '{} {} {}'.format(sub, opinion, stars)

if __name__ == '__main__':
    for i in range(0, 5):
        print(review())
