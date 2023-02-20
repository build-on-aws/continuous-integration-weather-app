import app
# from app import weather
import unittest

# Unit test for the weather function
class WeatherTestCase(unittest.TestCase):
    def test_weather(self):
        # Simulate a request to the weather function
        with app.app.test_request_context(method="POST", data={"city": "London"}):
            weather_data = app.weather()

            # Check if the response is a valid HTML page
            self.assertTrue("<!DOCTYPE html>" in weather_data)
            print("test passed\n\n",weather_data)

if __name__ == '__main__':
    unittest.main()