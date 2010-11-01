(function($) {
	
	$(document).ready(function() {
		ugm.listing_nav_binder();
		bdajax.binders.listing_nav_binder = ugm.listing_nav_binder;
    });
	
	ugm = {
		
		// bind listing trigger
		listing_nav_binder: function(context) {
			var sel = $('.columnlisting div.trigger', context);
			sel.unbind();
			sel.bind('click', ugm.listing_nav_action);
		},
		
		// perform listing nav action
		listing_nav_action: function(event) {
			// prevent default event from performing
			event.preventDefault();
			
			// set selected class
			var li = $(this).parent();
			$('li', li.parent()).removeClass('selected');
			li.addClass('selected');
			
			// perform action manually
			var target = bdajax.parsetarget(li.attr('ajax:target'));
			bdajax.action({
			    name: 'rightcolumn',
			    selector: '.right_column',
			    mode: 'replace',
			    url: target.url,
			    params: target.params
			});
		}
	};
	
})(jQuery);