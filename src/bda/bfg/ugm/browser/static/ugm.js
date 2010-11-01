(function($) {
	
	$(document).ready(function() {
		ugm.left_listing_nav_binder();
		ugm.right_listing_nav_binder();
		bdajax.binders.left_listing_nav_binder = ugm.left_listing_nav_binder;
		bdajax.binders.right_listing_nav_binder = ugm.right_listing_nav_binder;
    });
	
	ugm = {
		
		// bind left listing trigger
		left_listing_nav_binder: function(context) {
			var sel = $('div.left_column div.li_trigger', context);
			sel.unbind();
			sel.bind('click', ugm.left_listing_nav_cb);
		},
		
		// bind right listing trigger
        right_listing_nav_binder: function(context) {
            var sel = $('div.right_column div.li_trigger', context);
            sel.unbind();
            sel.bind('click', ugm.right_listing_nav_cb);
        },
		
		// left listing trigger callback
		left_listing_nav_cb: function(event) {
			var li = $(this).parent();
            ugm.reset_listing_selected(li);
			
			// perform action manually
			var target = bdajax.parsetarget(li.attr('ajax:target'));
			bdajax.action({
			    name: 'rightcolumn',
			    selector: '.right_column',
			    mode: 'replace',
			    url: target.url,
			    params: target.params
			});
			return false;
		},
		
		// right listing trigger callback
        right_listing_nav_cb: function(event) {
			var li = $(this).parent();
			ugm.reset_listing_selected(li);
			
			// reload context sensitiv tiles and context with new target
			var target = li.attr('ajax:target');
			bdajax.trigger('contextchanged', '.contextsensitiv', target);
			bdajax.trigger('contextchanged', '#content', target);
			return false;
		},
		
		// reset selcted item in listing
		reset_listing_selected: function(li) {
            $('li', li.parent()).removeClass('selected');
            li.addClass('selected');
		}
	};
	
})(jQuery);