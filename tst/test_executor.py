import unittest
import mock
import ExecuteCommand
from subprocess import CalledProcessError

class TestExecutor(unittest.TestCase):

     def setUp(self):
        self.patcher1 = mock.patch('ExecuteCommand.subprocess.Popen')
        self.mock_popen = self.patcher1.start()

     def tearDown(self):
        self.patcher1.stop()
        self.mock_popen.stop()

     def test_read_success_percent(self):
        command = ['git', 'commit', '-m', 'whatever']

        side_effect = "----whatever----"

        self.mock_popen.return_value.poll.return_value = 3
        self.mock_popen.return_value.stdout.readline.side_effect = side_effect

        with self.assertRaises(CalledProcessError):
            ExecuteCommand.call_popen(command, live_logging= False)

        self.mock_popen.return_value.poll.return_value = 0
        self.mock_popen.return_value.stdout.readline.side_effect = side_effect
        ExecuteCommand.call_popen(command, live_logging=False)

        calls = [
            mock.call(['git', 'commit', '-m', 'whatever'], stdout=-1)
        ]
        self.mock_popen.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
