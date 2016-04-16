$(document).ready(function() {
  var map;

  $(window).on('map:init', function(e) {
      // Get the map object
      var leafletMap = e.originalEvent.detail.map;
      var leaftletMapContainer = leafletMap.getContainer();
      if ($(leaftletMapContainer).attr('id') == 'id_evac_point_map') {
        map = leafletMap;
      } else if ($(leaftletMapContainer).attr('id') == 'id_eventimpacts_0_evac_point_map') {
        // for inline event impact form
        map = leafletMap;
      }
    }
  );

  var autocompleteSelector = '.autocomplete-light-eventimpact select';

  if ($('#eventimpacts-0').length > 0) {
    autocompleteSelector = '#eventimpacts-0 select.select2-hidden-accessible';
  }

  // On selecting a geolevel, show the geolevel polygon on the leaflet map
  $(autocompleteSelector).on("select2:selecting", function(e) {
    var apiEndpoint = $(this).data('autocomplete-light-url');
    var data = e.params.args.data;
    if (data.id) {
      // Clear existing GeoJSON layers
      map.eachLayer(function(layer) {
        if (layer instanceof L.GeoJSON) {
          map.removeLayer(layer);
        }
      });
      apiEndpoint = apiEndpoint.replace('autocomplete-', '') + 'api/';
      $.getJSON(apiEndpoint, {id: data.id}, function(data) {
        var layer = L.geoJson(data).addTo(map);
        map.fitBounds(layer.getBounds());
      });
    }
  });
});
