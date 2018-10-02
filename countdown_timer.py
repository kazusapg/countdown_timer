# TODO:Pause機能
# TODO:残り時間の表示

import argparse
import pygame
import time
import sys

class CountDownTimer:

    def __init__(self, minutes, mp3_filepath):
        self.minutes = minutes
        self.mp3_file_path = mp3_filepath

    def count_down(self):
        seconds = self.minutes * 60
        while seconds >= 0:
            seconds -= 1
            time.sleep(1)
        pygame.mixer.init()
        pygame.mixer.music.load(self.mp3_file_path)
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
    parser.add_argument('mp3_file_path', type=str, help='mp3ファイルのパス')

    args = parser.parse_args()
    countdown_timer = CountDownTimer(args.minutes, args.mp3_file_path)
    countdown_timer.count_down()
