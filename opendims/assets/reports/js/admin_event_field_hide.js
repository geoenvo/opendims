(function($) {
    $(function() {
        var selectedField = $('#id_disaster');

        // select the outer most div for magnitude's field and depth's field
        var magnitude = $('#id_magnitude').closest('.field-magnitude');
        var depth = $('#id_depth').closest('.field-depth');

        // select the outer most div for height's field and height_min's field
        var height = $('#id_height').closest('.field-height');
        var height_min = $('#id_height_min').closest('.field-height_min');

        function toggleHideShow(value) {
            if(value == 'GMP'){
                magnitude.show();
                depth.show();
                height.hide();
                height_min.hide();
            }
            else if(value == 'BJR' || value == 'ROB'){
                height.show();
                height_min.show();
                magnitude.hide();
                depth.hide();
            }
            else{
                height.hide();
                height_min.hide();
                magnitude.hide();
                depth.hide();
            }
        }

        // show/hide on load based on pervious value of selectField
        toggleHideShow(selectedField.val());

        // show/hide on change
        selectedField.change(function() {
            toggleHideShow($(this).val());
        });
    });
})(django.jQuery);
