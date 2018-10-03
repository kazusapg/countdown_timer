# TODO:Pause機能
# TODO:残り時間の表示

import argparse
import time
import sys
import os
import pygame


class CountDownTimer:

    def __init__(self, minutes, mp3_filepath):
        self.minutes = minutes
        self.mp3_file_path = mp3_filepath

    def validate_arg_minutes(self):
        """引数の時間をチェック"""
        if self.minutes < 0:
            print('時間には0以上の整数を入力してください。')
            return False
        return True

    def validate_arg_mp3_filepath(self):
        """引数のmp3ファイルをチェック"""
        if self.mp3_file_path == '':
            print('mp3ファイルのパスを入力してください')
            return False
        if not os.path.exists(self.mp3_file_path):
            print('ファイルが見つかりませんでした。')
            return False
        _, ext = os.path.splitext(self.mp3_file_path)
        if ext != '.mp3':
            print('拡張子が{}です。mp3ファイルを指定してください。'.format(ext))
            return False
        return True

    def count_down(self):
        if not self.validate_arg_minutes():
            return
        if not self.validate_arg_mp3_filepath():
            return

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
