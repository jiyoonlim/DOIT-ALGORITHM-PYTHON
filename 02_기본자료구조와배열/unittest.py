import unittest

def price(q):
  if q<10:
    return 100
  elif q<20:
    return 95
  else:
    return 90


class TestPriceFunction(unittest.TestCase):
  def test_price_1(self):
    self.assertEqual(price(1), 100)
    self.assertEqual(price(2), 200)
    self.assertEqual(price(3), 300)

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)