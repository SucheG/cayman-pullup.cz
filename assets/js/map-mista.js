mapboxgl.accessToken = 'pk.eyJ1IjoicHVsbHVwY3oiLCJhIjoiY2ptMmUzaHBkMmVndzNwcXVheXIwdGJrciJ9._aVCFvQX7445VKEoNqC-9g';

var centerCZ = [15.47,49.83];
var zoomCZ = 6.4;

var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/pullupcz/cjmpbn331fibo2rnyxvrdmvc9',

  center: centerCZ,
  zoom: zoomCZ,
  scrollZoom: false
});
map.addControl(new mapboxgl.NavigationControl());
map.addControl(new mapboxgl.FullscreenControl());

map.on('click', function (e) {
  var features = map.queryRenderedFeatures(e.point, {
    layers: ['mista'] // name of layer
  });

  if (!features.length) { return; }

  var feature = features[0];//

  var popup = new mapboxgl.Popup({ offset: [0, -15] })
    .setLngLat(feature.geometry.coordinates)
    .setHTML('<h3>' + feature.properties.nazev + '</h3><p>' + feature.properties.popis + '</p>')
    .setLngLat(feature.geometry.coordinates)
    .addTo(map);
});

// Add geolocate control to the map.
map.addControl(new mapboxgl.GeolocateControl({
  positionOptions: {
    enableHighAccuracy: true
  },
  trackUserLocation: true
}));

var zoomValues = [
  // west, south, east, north
  // sw, ne
  {name: "CZ", bb: [[12, 48], [19, 51.3]]},
  {name: "SK", bb: [[16.6, 47.4], [23, 50.2]]},
  {name: "Svět", bb: [[-131, -52], [159, 77]]}
];

var zoomDiv = document.getElementById('zoomDiv');

// TODO: místo zoom a center použít BBox
// TODO: tlačítka přidat přímo do mapy ?
// TODO: formulář pro zadání nového bodu / nového bboxu (oblasti pro zoom)

//// TODO: největší otázka: jak bude provázaná mapa a stránky ?

function createElement(tag, attrs, text, parent) {
  var el = document.createElement(tag);
  el.innerText = text;
  attrs.forEach(function (attr_value) {
    attr_value = attr_value.split('=');
    el.setAttribute(attr_value[0], attr_value[1]);
  });
  parent.appendChild(el);
  return el;
}

if (zoomDiv) {
  zoomValues.forEach(function (value) {
    var btn = createElement('span', ['class= btn btn-088'], value.name, zoomDiv);

    btn.addEventListener('click', function() {
      map.fitBounds(value.bb);
    });
  });

  var addBtn = createElement('span', ['class= btn btn-088 right'], '+ přidat', zoomDiv);
  addBtn.addEventListener('click', function () {
    console.log('Show Form to add new Place');
  })
}