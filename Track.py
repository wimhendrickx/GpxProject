from xml.dom.minidom import parse

class TrackPoint:
    lat = 0
    lon = 0
    ele = 0
    
    def __init__(self, x, y, z):
        self.lat = x
        self.lon = y
        self.ele = z
        
    def __str__(self):
        return 'lat: ' + self.lat + ' lon: ' + self.lon
        
    def __repr__(self):
        return 'lat: ' + self.lat + ' lon: ' + self.lon
        
class Track:
    tracks = []
    
    def __init__(self):
        pass
    
    def addTrackPoint(self, t):
        self.tracks.append(t)
        
    def getAmount(self):
        return len(self.tracks)
        
    def getTrackFromFile(self, filename):
        dom = parse(filename)
        for node in dom.getElementsByTagName('trkpt'):
            self.addTrackPoint(TrackPoint(node.getAttribute('lat'), node.getAttribute('len'), 0))
    
    def printTrack(self):
        print self.tracks
    
onzetrack = Track() 
onzetrack.getTrackFromFile("gpx/example.gpx")  
onzetrack.printTrack()
    
    
    