import unittest
from unittest.mock import patch, MagicMock
import main
import os
import datetime

class TestMainScript(unittest.TestCase):
    def setUp(self):
        self.german = "Guten Morgen"
        self.russian = "Доброе утро"
        self.expected_ssml = f'{self.german}. <break time="1s" /> {self.russian}. <break time="2s" /> {self.german}. <break time="2s" /> {self.german}.<break time="2s" /> {self.german}. <break time="2s" /> {self.german}.'
        self.datecode = datetime.datetime.now().strftime('%Y-%m-%d')
        self.csv_source = 'german-russian_01'
        self.expected_filename = f"{self.csv_source}_{self.datecode}_guten_morgen.mp3"

    def test_build_ssml(self):
        ssml = main.build_ssml(self.german, self.russian)
        self.assertEqual(ssml, self.expected_ssml)

    @patch('main.generate_audio')
    def test_audio_generation_and_naming(self, mock_generate_audio):
        mock_generate_audio.return_value = b"fake audio data"
        output_path = os.path.join(main.OUTPUT_DIR, self.expected_filename)
        # Simulate one row
        ssml_text = main.build_ssml(self.german, self.russian)
        audio_content = main.generate_audio(ssml_text, output_path, self.german)
        self.assertEqual(audio_content, b"fake audio data")
        self.assertTrue(self.expected_filename.endswith("guten_morgen.mp3"))

if __name__ == '__main__':
    unittest.main() 