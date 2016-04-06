var map;

$(window).on('map:init', function(e) {
    // Get the map object
    map = e.originalEvent.detail.map;
  }
);

$(document).ready(function() {
  // On selecting a geolevel, show the geolevel polygon on the leaflet map
  $('select').on("select2:selecting", function(e) {
    var selectField = $(this).attr('name');
    var data = e.params.args.data;
    if (data.id) {
      // Clear existing GeoJSON layers
      map.eachLayer(function(layer) {
        if (layer instanceof L.GeoJSON) {
          map.removeLayer(layer);
        }
      });
      var apiEndpoint = '/geolevels/selectField/api/'.replace('selectField', selectField);
      $.getJSON(apiEndpoint, {id: data.id}, function(data) {
        var layer = L.geoJson(data).addTo(map);
        map.fitBounds(layer.getBounds());
      });
    }
  });
});
