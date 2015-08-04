#!/usr/bin/env python3

#
# Timeline comes from:
# http://www.aph.gov.au/About_Parliament/House_of_Representatives/Powers_practice_and_procedure/practice/chapter3
#


import argparse
import datetime


def snap_saturday(dt, delta):
    while dt.weekday() != 5:
        dt = dt + datetime.timedelta(days=delta)
    return dt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'date',
        type=str,
        nargs='?',
        default=datetime.date.today().strftime("%d/%m/%Y"),
        help='date writs are issued in dd/mm/yyyy format')
    args = parser.parse_args()
    dt = datetime.datetime.strptime(args.date, '%d/%m/%Y').date()
    last_legal_day = dt + datetime.timedelta(days=58)

    # Constitution, s. 32; Commonwealth Electoral Act, ss. 151, 152
    print("  Writs issued on:", dt, "at 6pm")
    # Commonwealth Electoral Act, ss. 102(4), 155
    print(" Enrolment closes:", dt + datetime.timedelta(days=7), "at 8pm (local time)")
    # Commonwealth Electoral Act, ss. 156, 175
    print(" Nomination close:", dt + datetime.timedelta(days=10), "-", dt+datetime.timedelta(days=27))
    # Commonwealth Electoral Act, ss. 157, 158
    saturday = snap_saturday(dt + datetime.timedelta(days=33), 1)
    # Commonwealth Electoral Act, s. 159
    print("Writs returned by:", dt + datetime.timedelta(days=100))

    print()
    while saturday <= last_legal_day:
        print("   Candidate date:", saturday)
        saturday += datetime.timedelta(days=7)


if __name__ == '__main__':
    main()
