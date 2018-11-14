import unittest
import tempfile
from countdown_timer import CountDownTimer


class TestValidateArgMinutes(unittest.TestCase):
    
    def test_validate_arg_minutes_negative(self):
        c = CountDownTimer(-1, 'test.mp3')
        self.assertFalse(c.validate_arg_minutes())


class TestValidateValidateArgMp3Filepath(unittest.TestCase):

    def test_validate_arg_mp3_filepath(self):
        with tempfile.TemporaryFile(suffix='.mp3') as f:
            c = CountDownTimer(1, f.name)
            self.assertTrue(c.validate_arg_mp3_filepath())

    def test_validate_arg_mp3_filepath_blank(self):
        c = CountDownTimer(1, '')
        self.assertFalse(c.validate_arg_mp3_filepath())

    def test_validate_arg_mp3_filepath_not_existence(self):
        c = CountDownTimer(1, 'not_existence.mp3')
        self.assertFalse(c.validate_arg_mp3_filepath())

    def test_validate_arg_mp3_filepath_wrong_extension(self):
        with tempfile.TemporaryFile(suffix='.txt') as f:
            c = CountDownTimer(1, f.name)
            self.assertFalse(c.validate_arg_mp3_filepath())


if __name__ == '__main__':
    unittest.main()
