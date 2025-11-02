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



    def test_impact_text_format(self):
        """
        Test 2: Check that the scraped campaign impact text is formatted correctly.
        """
        url = "https://www.xula.edu/about/centennial.html"
        result = get_centennial_campaign_impact(url)

        self.assertIsInstance(result["impact_text"], list, "impact_text should be a list")
        self.assertGreater(len(result["impact_text"]), 0, "impact_text list should not be empty")
        self.assertTrue(all(isinstance(p, str) and p.strip() for p in result["impact_text"]),
                        "All impact_text items should be non-empty strings")
        
    
   


        

if __name__ == "__main__":
    unittest.main()
