import unittest
from biz import Track
from biz import TrackPoint

import sys

sys.path.append('/Users/Wim/GpxProject')

class Test_Track(unittest.TestCase):
    def test_init(self):
        pass
        
    def test_without_file(self):
        t = Track()
        self.assertEqual(t.getAmount(), 0)
        
    def test_file_3_tp(self):
        t = Track()
        t.getTrackFromFile("gpx/3tp.gpx")
        self.assertEqual(t.getAmount(), 3)

    def test_max_lat_1(self):
        t = Track()
        t.addTrackPoint(TrackPoint(1, 1, 1))
        t.addTrackPoint(TrackPoint(100, 1, 1))
        t.addTrackPoint(TrackPoint(95, 1, 1))
        t.addTrackPoint(TrackPoint(-4, 1, 1))
        t.addTrackPoint(TrackPoint(101, 1, 1))
        self.assertEqual(t.getMaximumLat(), 101)
        
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