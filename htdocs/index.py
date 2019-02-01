#!python
print("Content-Type: text/html")
print()
import cgi,cgitb
cgitb.enable() #for debegygging
form = cgi.FieldStorage()
print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
    <title>Panorama test</title>
    <script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=76frmrzttl&submodules=panorama"></script>
</head>
<body>
<div id="pano1" style="width:49%;height:300px;float:left;"></div>
<div id="pano2" style="width:49%;height:300px;float:left;"></div>
<div id="pano3" style="width:49%;height:300px;float:left;"></div>
<div id="pano4" style="width:49%;height:300px;float:left;"></div>
<script>
var panoramaOptions1 = {
    position: new naver.maps.LatLng(37.3599605, 127.1058814),
    pov: {
        pan: -180,
        tilt: 0,
        fov: 90
    },
    visible: true,
    minScale: 0,
    maxScale: 0,
    minZoom: 0,
    maxZoom: 0,
    aroundControl: false
};
var panoramaOptions2 = {
    position: new naver.maps.LatLng(37.3599605, 127.1058814),
    pov: {
        pan: -90,
        tilt: 0,
        fov: 90
    },
    visible: true,
    minScale: 0,
    maxScale: 0,
    minZoom: 0,
    maxZoom: 0,
    aroundControl: false
};
var panoramaOptions3 = {
    position: new naver.maps.LatLng(37.3599605, 127.1058814),
    pov: {
        pan: 0,
        tilt: 0,
        fov: 90
    },
    visible: true,
    minScale: 0,
    maxScale: 0,
    minZoom: 0,
    maxZoom: 0,
    aroundControl: false
};
var panoramaOptions4 = {
    position: new naver.maps.LatLng(37.3599605, 127.1058814),
    pov: {
        pan: 90,
        tilt: 0,
        fov: 90
    },
    visible: true,
    minScale: 0,
    maxScale: 0,
    minZoom: 0,
    maxZoom: 0,
    aroundControl: false
};

var panorama1 = new naver.maps.Panorama("pano1",panoramaOptions1);
var panorama2 = new naver.maps.Panorama("pano2",panoramaOptions2);
var panorama3 = new naver.maps.Panorama("pano3",panoramaOptions3);
var panorama4 = new naver.maps.Panorama("pano4",panoramaOptions4);


</script>
</body>
</html>
''')