import unittest
from biz import Track
from biz import TrackPoint

import sys

sys.path.append('/Users/Wim/GpxProject')

class Test_Track(unittest.TestCase):
    def test_init(self):
        pass
        
    def test_no_file_loading(self):
        tt = Track()
        tt.printTrack()
        self.assertEqual(tt.getAmount(), 0)
        
    def test_3_tp(self):
        t = Track()
        t.getTrackFromFile("gpx/3tp.gpx")
        self.assertEqual(t.getAmount(), 3)

class Test_TrackPoint(unittest.TestCase):
    def test_init(self):
        pass
    
    def test_lat(self):
        t = TrackPoint(1,2,3)
        self.assertEqual(t.getLat(), 1)
        
    def test_lon(self):
        t = TrackPoint(1,2,3)
        self.assertEqual(t.getLon(), 2)
        
    def test_ele(self):
        t = TrackPoint(1,2,3)
        self.assertEqual(t.getEle(), 3)