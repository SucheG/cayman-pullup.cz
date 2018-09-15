mapboxgl.accessToken = 'pk.eyJ1IjoicHVsbHVwY3oiLCJhIjoiY2ptMmUzaHBkMmVndzNwcXVheXIwdGJrciJ9._aVCFvQX7445VKEoNqC-9g';

var centerCZ = [15.47,49.83];
var zoomCZ = 6.4;

var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v10',
  center: centerCZ,
  zoom: zoomCZ,
  scrollZoom: false
});
map.addControl(new mapboxgl.NavigationControl());
map.addControl(new mapboxgl.FullscreenControl());

// map.on('click', function (e) {
//   var features = map.queryRenderedFeatures(e.point, {
//     layers: ['name-of-layer'] // name of layer
//   });
//
//   if (!features.length) { return; }
//
//   var feature = features[0];//
//
//   var popup = new mapboxgl.Popup({ offset: [0, -15] })
//     .setLngLat(feature.geometry.coordinates)
//     .setHTML('<h3>' + feature.properties.index + '</h3><p>' + feature.properties.name + '</p>')
//     .setLngLat(feature.geometry.coordinates)
//     .addTo(map);
// });

// Add geolocate control to the map.
map.addControl(new mapboxgl.GeolocateControl({
  positionOptions: {
    enableHighAccuracy: true
  },
  trackUserLocation: true
}));

var zoomValues = [
  {name: "CZ", center: centerCZ, zoom: zoomCZ},
  {name: "SK", center: [19.76,48.68], zoom: 6.5},
  {name: "Svět", center: [0,30], zoom: 1}
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
      map.flyTo({
        center: value.center,
        zoom: value.zoom,
        duration: 1000,
        speed: 1,
        curve: 0.5,
      });
    });
  });

  var addBtn = createElement('span', ['class= btn btn-088 right'], '+ přidat', zoomDiv);
  addBtn.addEventListener('click', function () {
    console.log('Show Form to add new Place');
  })
}