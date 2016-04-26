$(document).ready(function() {
  // On selecting a geolevel, populate the id text field
  $('select').on("select2:selecting", function(e) {
    var data = e.params.args.data;
    if (data.id) {
      $('#id_id').val('');
      $('#id_id').val(data.id);
    }
  });
});
