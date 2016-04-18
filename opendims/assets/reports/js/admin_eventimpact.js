$(document).ready(function() {
  var map;
  var mapArr = [];
  var inlineMapRegex = new RegExp('^id_eventimpacts_[0-9]+_evac_point_map$', 'i');

  $(window).on('map:init', function(e) {
      // Get the map object
      var leafletMap = e.originalEvent.detail.map;
      var leaftletMapContainer = leafletMap.getContainer();
      var leaftletMapContainerId = $(leaftletMapContainer).attr('id');

      if (leaftletMapContainerId == 'id_evac_point_map') { // For stand alone event impact form
        map = leafletMap;
      } else if (inlineMapRegex.test(leaftletMapContainerId)) { // For inline event impact form
        mapArr.push(leafletMap);
      }
    }
  );

  var isInline = false;
  var autocompleteSelector = '.autocomplete-light-eventimpact select';

  // Check if event impact form is inline
  if ($('.dynamic-eventimpacts').length > 0) {
    isInline = true;
    autocompleteSelector = '.dynamic-eventimpacts select.select2-hidden-accessible';
  }

  // On selecting a geolevel, show the geolevel polygon on the leaflet map
  $(autocompleteSelector).on("select2:selecting", function(e) {
    var apiEndpoint = $(this).data('autocomplete-light-url');
    var data = e.params.args.data;

    if (isInline) {
      var selectName = $(this).attr('name');
      var mapIndex = selectName.match(/eventimpacts-([0-9]+)/i)[1];
      map = mapArr[parseInt(mapIndex)];
    }

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
