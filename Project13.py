import random
from random import choice

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },{
        'name': 'The Rock',
        'follower_count': 282,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 300,
        'description': 'Reality TV star and entrepreneur',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 234,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 254,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 220,
        'description': 'Reality TV star and entrepreneur',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 210,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 230,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'National Geographic',
        'follower_count': 200,
        'description': 'Media company and magazine',
        'country': 'United States'
    },
    {
        'name': 'Nike',
        'follower_count': 170,
        'description': 'Sportswear brand',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 175,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 160,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Shakira',
        'follower_count': 120,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Zendaya',
        'follower_count': 120,
        'description': 'Actress and singer',
        'country': 'United States'
    },
    {
        'name': 'Dua Lipa',
        'follower_count': 110,
        'description': 'Musician',
        'country': 'United Kingdom'
    },
    {
        'name': 'NASA',
        'follower_count': 80,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 90,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo Jr.',
        'follower_count': 40,
        'description': 'Son of Cristiano Ronaldo',
        'country': 'Portugal'
    }
]
def compare(Option1,Option2):
    if Option1['follower_count']>Option2['follower_count']:
        return 'A'
    elif Option2['follower_count']>Option1['follower_count']:
        return 'B'

should_continue=True
score=0
personB = random.choice(data)

while should_continue:
    #Making Account B the next account A
    personA = personB
    personB = random.choice(data)
    if personA==personB:
        personB=random.choice(data)
    print(f"Compare A:{personA['name']} is a {personA['description']} from {personA['country']}")
    print(f"Against B:{personB['name']} is a {personB['description']} from {personB['country']}")
    choice=input("Which option do you think has more followers?(A/B)")
    result=compare(personA,personB)
    if result==choice:
        score+=1
        print("\n"*20)
    else:
        print(f"Sorry that is wrong.Your final score is {score}")
        should_continue=False



