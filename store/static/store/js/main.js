$(document).ready(function() {

	// Activar item de menu
	$('.nav li a').each(function(index) {
		if (this.href.trim() == window.location) {
			$(this).parent().addClass("active");
		} else {
			$(this).removeClass('active');
		}
	});

});