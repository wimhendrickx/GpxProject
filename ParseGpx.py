from xml.dom.minidom import parse
dom = parse("gpx/example.gpx")
for node in dom.getElementsByTagName('trkpt'):  # visit every node <bar />
    print node.toxml()