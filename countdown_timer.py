import argparse
import pygame
import time
import sys


def count_down(minutes, mp3file_path):
    seconds = minutes * 60
    while seconds >= 0:
        seconds -= 1
        time.sleep(1)
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file_path)
    print('時間になりました')
    try:
        while True:
            pygame.mixer.music.play(100)
            if pygame.mixer.music.get_busy():
                time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='引数で指定した時間（分単位）後にmp3ファイルを鳴らす')
    parser.add_argument('minutes', type=int, help='指定時間（分単位）')
    parser.add_argument('mp3file_path', type=str, help='mp3ファイルのパス')

    args = parser.parse_args()
    count_down(args.minutes, args.mp3file_path)
