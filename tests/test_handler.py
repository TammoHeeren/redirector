import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_with_empty_path(self):
        result = index.handler(None, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'text/html')

    def test_linkedin(self):
        result = index.handler({
            'pathParameters': {'short': 'linkedin'}
        }, None)
        self.assertEqual(result['statusCode'], 303)

    def test_with_incorrect(self):
        result = index.handler({
            'pathParameters': {'short': '_____'}
        }, None)
        self.assertEqual(result['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
