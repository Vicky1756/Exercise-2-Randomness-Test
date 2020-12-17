from random import sample


def random_balls():
    balls = (sorted(sample(list(range(1, 51)), 10)))
    return balls


if __name__ == "__main__":
    balls = random_balls()
    print(balls)
