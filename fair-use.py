#!/usr/bin/env python3

import argparse
import datetime

def mktime(timestring):
    return datetime.datetime.strptime(timestring, '%M:%S') - datetime.datetime.strptime('00:00', '%M:%S')

def length(a):
    return f'{round((a.stop - a.start).total_seconds(), 0):.0f} seconds'

def percent(a):
    return round((a.stop - a.start).total_seconds() / a.total.total_seconds() * 100, 0)
    return

def main():
    parser = argparse.ArgumentParser(description='Generate a paragraph explaining why you your video is fair use')
    parser.add_argument('--start', type=mktime, required=True)
    parser.add_argument('--stop', type=mktime, required=True)
    parser.add_argument('--total', type=mktime, required=True)
    parser.add_argument('--fact', action="store_true")
    args = parser.parse_args()

    purpose = 'The transformed work is a recording of an artistic and athletic performance (a figure skating routine) that uses the original work. The transformed work changes the original from a purely auditory experience to one involving a novel artistic interpretation as well as athletic demonstrations (jumps and spins). The transformed work is non-commercial in nature. '

    if args.fact:
        nature = 'The original work is fictional in nature. '
    else:
        nature = ''

    p = percent(args)
    pStr = f'{percent(args):.0f}%'

    if percent(args) < 90:
        amount = f'The new work uses {length(args)} ({pStr}) of the original work. This represents only a portion of the original work. The original work, being a musical recording, is designed to be listened to in its entirety. Thereby the new work, which includes the original as a recording over an ice rink sound system, does not serve as a substitute for the original. '
    else:
        amount = f'The new work uses {length(args)} ({pStr}) of the original work. While this represents a majority of the original work, the transformed work is entirely different in listening experience. The transformed work includes the original as a poor, live recording of the original work played over an ice rink sound system. Additionally, the choice to use the majority of the original work does not change the fair use nature---this only represents the artistic choice of the performer. '

    effect = 'Additionally, a listener derives different, augmented enjoyment from watching the performance in the transformed work as opposed to the purely auditory experience of the original. Therefore, the market for the copyrighted, original work is unaffected by the transformed work. '
    thanks = 'Thanks for taking the time to review this dispute.'

    print(purpose + nature + amount + effect + thanks)

if __name__ == '__main__':
    main()
