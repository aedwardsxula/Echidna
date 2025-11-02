import unittest
import requests
from xula_driver import get_centennial_campaign_impact

class TestCentennialScraper(unittest.TestCase):

    def test_valid_url_response(self):
        """
        Test 1: Ensure the URL returns a successful (200 OK) response.
        """
        url = "https://www.xula.edu/about/centennial.html"
        response = requests.get(url, timeout=10)
        
        self.assertEqual(response.status_code, 200, "URL did not return 200 OK")


if __name__ == "__main__":
    unittest.main()

