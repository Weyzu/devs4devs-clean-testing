import logging


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def get_user_stats(username):
    # hack, hack, hack
    return {
        "elections_hacked": 10,
        "is_laserproof": False,
    }


def get_username(user_id):
    # hack, hack, hack
    logging.info("I'm doing something!")
    return 'Pinky'
