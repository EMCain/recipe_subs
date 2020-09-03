from app.reviews.generate import review
from time import sleep

while True:
    print(review())
    sleep(1)