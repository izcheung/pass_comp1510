"""
Irene Cheung
A01349998
"""

import io
from unittest import TestCase
from unittest.mock import patch
from game import welcome_message


class TestWelcomeMessage(TestCase):
    @patch('builtins.input', side_effect=["Irene"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_message_all_alphabetical_letters(self, mock_output, _):
        welcome_message()
        printed_output = mock_output.getvalue()
        expected_output = ("\nWelcome to 'Chocopass' Irene! You are a hopeless student with an average of 49.9% in"
                           " COMP1510. Out of desperation, you make a devious plan to bribe your instructor with his favourite "
                           "chocolates to pass his course. Your task is to collect 10 Reese's chocolates and then "
                           "deliver it to him.\n")
        self.assertEqual(expected_output, printed_output)

    @patch('builtins.input', side_effect=["123"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_message_all_numbers(self, mock_output, _):
        welcome_message()
        printed_output = mock_output.getvalue()
        expected_output = ("\nWelcome to 'Chocopass' 123! You are a hopeless student with an average of 49.9% in "
                           "COMP1510. Out of desperation, you make a devious plan to bribe your instructor with his "
                           "favourite chocolates to pass his course. Your task is to collect 10 Reese's chocolates and"
                           " then deliver it to him.\n")
        self.assertEqual(expected_output, printed_output)

    @patch('builtins.input', side_effect=["#@!$%^><"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_message_all_symbols(self, mock_output, _):
        welcome_message()
        printed_output = mock_output.getvalue()
        expected_output = ("\nWelcome to 'Chocopass' #@!$%^><! You are a hopeless student with an average of 49.9% "
                           "in COMP1510. Out of desperation, you make a devious plan to bribe your instructor with his "
                           "favourite chocolates to pass his course. Your task is to collect 10 Reese's chocolates and "
                           "then deliver it to him.\n")
        self.assertEqual(expected_output, printed_output)

    @patch('builtins.input', side_effect=["#@#HI%*.27"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_message_mix_symbols_letters_numbers(self, mock_output, _):
        welcome_message()
        printed_output = mock_output.getvalue()
        expected_output = ("\nWelcome to 'Chocopass' #@#HI%*.27! You are a hopeless student with an average of 49.9% "
                           "in COMP1510. Out of desperation, you make a devious plan to bribe your instructor with his "
                           "favourite chocolates to pass his course. Your task is to collect 10 Reese's chocolates "
                           "and then deliver it to him.\n")
        self.assertEqual(expected_output, printed_output)
