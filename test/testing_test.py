import unittest
from click.testing import CliRunner
import test

class TestTest(unittest.TestCase):
    def test_main(self):
        runner = CliRunner()
        result = runner.invoke(test.main, ['hi'])
        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,'hi\n')

        result = runner.invoke(test.main, ['hi', '-n', 'ram'])
        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,'hi ram\n')

 
if __name__ == '__main__':
    unittest.main()
