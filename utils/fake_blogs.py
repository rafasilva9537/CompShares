from faker import Faker
from random import randint, choice
from datetime import timedelta
from pprint import pprint

faker = Faker()

def create_fake_blog() -> dict:
    creation_date = faker.date_time_this_decade()
    update_date = choice(
        [creation_date, creation_date + timedelta(days=randint(1, 15))]
    )

    blog = {
        "user": {
            "first_name": faker.first_name(), 
            "last_name": faker.last_name()
        },
        "title": faker.sentence(7),
        "description": faker.sentence(20),
        "creation_date": creation_date,
        "upadte_date": update_date,
        "cover_image" : "blog/images/image-test.jpeg",
        "post_text": faker.sentence(400),
        "tags": [ { "name": faker.word() } for _ in range(randint(2, 5))],
        "users_reactions": [ { "is_liked": choice([True, False]) } for _ in range(randint(0, 150))]
    }

    return blog

def main():
    pprint(create_fake_blog(), sort_dicts=False)

if __name__ == "__main__":
    main()