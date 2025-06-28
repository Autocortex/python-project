import unittest
import python_repos as pr

class TestPythonRepos(unittest.TestCase):

    def test_equal_statuscode(self):
        self.assertEqual(pr.status_code, 200)

    def test_equal_responsedata(self):
        self.assertEqual(len(pr.repo_dicts), 30)

    def test_equal_lists(self):
        self.assertEqual(len(pr.repo_links), len(pr.stars), len(pr.labels))

if __name__ == '__main__':
    unittest.main()