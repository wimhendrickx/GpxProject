import unittest
from biz import Track
import sys

sys.path.append('/Users/Wim/GpxProject')

class Test_Track(unittest.TestCase):
    def test_init(self):
        pass
        
    def test_no_file_loading(self):
        t = Track()
        self.assertEqual(t.getAmount(), 0)
        
    def test_3_tp(self):
        t = Track()
        t.getTrackFromFile("gpx/3tp.gpx")
        self.assertEqual(t.getAmount(), 3)
        
    