/*-------------------------------------------------------------------------
 * RENDIFY - Custom jQuery Scripts
 * ------------------------------------------------------------------------

	1.	Plugins Init
	2.	Site Specific Functions
	3.	Shortcodes
	4.      Other Need Scripts (Plugins config, themes and etc)
	
-------------------------------------------------------------------------*/


jQuery(document).ready(function($){
	
	
/*------------------------------------------------------------------------*/
/*	1.	Plugins Init
/*------------------------------------------------------------------------*/


/************** ToolTip *********************/

	function toolTipInit() {
	
		$('.social-icons li a').tooltip({
			placement: 'top'
		});
	}
	
	toolTipInit();


/************** Tabs *********************/

	$('#tabs').tab();


/************** SuperFish Menu *********************/

	function initSuperFish(){
		
		$(".sf-menu").superfish({
			 delay:  50,
			 autoArrows: true,
			 animation:   {opacity:'show'}
			 //cssArrows: true
		});
		
		// Replace SuperFish CSS Arrows to Font Awesome Icons
		$('nav > ul.sf-menu > li').each(function(){
			$(this).find('.sf-with-ul').append('<i class="fa fa-angle-down"></i>');
		});
	}
	
	initSuperFish();



/************** FlexSlider *********************/

	$(window).load(function() {
	    $('.flexslider').flexslider({
	    	animation: "fade",
	    	touch: true,
	    	controlNav: false,
	    	prevText: "&nbsp;",  
			nextText: "&nbsp;" 
	    });
	});

	$('.carousel').carousel({
	  interval: 300
	})



/************** FancyBox *********************/
	$(".fancybox").fancybox({
		padding: 5,
		titlePosition: 'over'
	});



/************** pSlider *********************/

	$('#slider-testimonials').pSlider({
        slider: $('#slider-testimonials ul li'),
        visible: 1,
        button: {
            next: $('#slider-testimonials .next'),
            prev: $('#slider-testimonials .prev')
        }
    });



/************** mixitup *********************/
    $('#Grid').mixitup({
        effects: ['fade','grayscale'],
        easing: 'snap',
        transitionSpeed: 400
    });
	



/*------------------------------------------------------------------------*/
/*	2.	Site Specific Functions
/*------------------------------------------------------------------------*/


	$('.sub-menu').addClass('animated fadeInRight');




/************** Responsive Navigation *********************/

	$('.menu-toggle-btn').click(function(){
        $('.responsive_menu').stop(true,true).slideToggle();
    });

	
	$('.thumb-small-gallery').addClass('closed');
	
    $('.thumb-small-gallery').hover(function(){
        var elem = $(this);
        elem.removeClass('closed');
        elem.css({opacity: 1});
        $('.gallery-small-thumbs .closed').css({opacity: 0.7});
    }, function(){
        var elem = $(this);
        elem.addClass('closed');
        $('.gallery-small-thumbs .closed').css({opacity: 1});
    });


});