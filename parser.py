import argparse
from typing import List
from time_utils import Date


def configure_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--usr", help="the username of the email-account which will send the notification messages")
    parser.add_argument("--pw", help="the password of the email-account which will send the notification messages")
    parser.add_argument("--r", help="The list of email-accounts which will receive a notification when a slot is avaliable. Email-accounts should be separated with a comma")
    parser.add_argument("--d", help="The list of days for which a reservation is desired. Days should be separated with a comma")
    return parser


def get_args() -> (str, str, List[str], List[Date]):
    parser = configure_parser()
    args = parser.parse_args()
    if args.usr is None:
        raise ValueError("A username must be specified")
    username = args.usr
    if args.pw is None:
        raise ValueError("A password must be specified")
    password = args.pw
    if args.r is None:
        raise ValueError("At least one receiver must be specified")
    receivers = args.r.split(",")
    if args.d is None:
        raise ValueError("At least one day must be specified")
    days = parse_days(args.d)
    return username,password,receivers,days


def parse_days(days_raw: str) -> List[Date]:
    list_of_days = days_raw.split(",")
    parsed_days = []
    for day in list_of_days:
        parsed_days.append(Date(day))
    return parsed_days
