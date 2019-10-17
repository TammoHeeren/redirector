import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_with_empty_path(self):
        result = index.handler(None, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/html')

    def test_linkedin(self):
        result = index.handler({
            'pathParameters': {'short': 'linkedin'}
        }, None)
        self.assertEqual(result['statusCode'], 301)
        self.assertEqual(result['headers']['Location'], 'https://www.linkedin.com/in/tammoheeren/')


if __name__ == '__main__':
    unittest.main()
