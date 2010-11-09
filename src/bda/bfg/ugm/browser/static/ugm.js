(function($) {
    
    $(document).ready(function() {
        ugm.left_listing_nav_binder();
        ugm.right_listing_nav_binder();
        ugm.listing_filter_binder();
        ugm.listing_actions_binder();
		ugm.listing_related_binder();
        bdajax.binders.left_listing_nav_binder = ugm.left_listing_nav_binder;
        bdajax.binders.right_listing_nav_binder = ugm.right_listing_nav_binder;
        bdajax.binders.listing_filter_binder = ugm.listing_filter_binder;
        bdajax.binders.listing_actions_binder = ugm.listing_actions_binder;
		bdajax.binders.listing_related_binder = ugm.listing_related_binder;
    });
    
    ugm = {
        
        // bind left listing trigger
        left_listing_nav_binder: function(context) {
            var sel = $('div.left_column div.li_trigger', context);
            sel.unbind();
            sel.bind('click', ugm.left_listing_nav_cb);
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
        
        // bind right listing trigger
        right_listing_nav_binder: function(context) {
            var sel = $('div.right_column div.li_trigger', context);
            sel.unbind();
            sel.bind('click', ugm.right_listing_nav_cb);
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
        
        // bind listing item actions
        listing_actions_binder: function(context) {
            
			// bind delete actions
			var delete_actions = $('div.actions a.delete_item', context);
            delete_actions.unbind();
            delete_actions.bind('click', ugm.actions.delete_item);
			
			// bind disabled delete actions
			var delete_disabled = $('div.actions a.delete_item_disabled',
			                        context);
			delete_disabled.unbind();
			delete_disabled.bind('click', function(event) {
				event.preventDefault();
			});
            
			// bind add actions
			var add_actions = $('div.actions a.add_item', context);
            add_actions.unbind();
            add_actions.bind('click', ugm.actions.add_item);
			
			// bind disabled add actions
			var add_disabled = $('div.actions a.add_item_disabled', context);
			add_disabled.unbind();
			add_disabled.bind('click', function(event) {
                event.preventDefault();
            });
            
			// bind remove actions
			var remove_actions = $('div.actions a.remove_item', context);
            remove_actions.unbind();
            remove_actions.bind('click', ugm.actions.remove_item);
			
			// bind disabled remove actions
			var remove_disabled = $('div.actions a.remove_item_disabled',
			                        context);
			remove_disabled.unbind();
			remove_disabled.bind('click', function(event) {
                event.preventDefault();
            });
        },
        
        // object containing ugm action callbacks
        actions: {
            
            // delete item from database
            delete_item: function(event) {
                event.preventDefault();
                var options = {
                    message: 'Do you really want to delete this item?',
                    action_id: 'delete_item'
                };
                var elem = $(event.currentTarget);
                var target = elem.attr('ajax:target');
                $.extend(options, bdajax.parsetarget(target));
                $.extend(options, {
                    success: function(data) {
                        if (!data) {
                            bdajax.error('Empty response');
							return;
                        }
                        if (!data.success) {
                            bdajax.error(data.message);
							return;
                        }
                        var li = elem.parent().parent();
                        if (li.hasClass('selected')) {
                            var col = $('div.right_column');
                            col.removeClass('box');
                            col.empty();
                        }
                        li.remove();
                    }
                });
                bdajax.dialog(options, function(options) {
                    ugm.actions.perform(options);
                });
            },
            
            // add item as member
            add_item: function(event) {
                event.preventDefault();
				var elem = $(event.currentTarget);
                var target = elem.attr('ajax:target');
				var options = bdajax.parsetarget(target);
				$.extend(options, {
					action_id: 'add_item',
                    success: function(data) {
                        if (!data) {
                            bdajax.error('Empty response');
                            return;
                        }
                        if (!data.success) {
                            bdajax.error(data.message);
                            return;
                        }
						elem.unbind();
	                    elem.removeClass('add_item');
	                    elem.addClass('add_item_disabled');
						elem.bind('click', function(event) {
			                event.preventDefault();
			            });
						var remove = $('.remove_item_disabled', elem.parent());
						remove.unbind();
						remove.removeClass('remove_item_disabled');
						remove.addClass('remove_item');
						remove.bind('click', ugm.actions.remove_item);
                    }
                });
				ugm.actions.perform(options);
            },
            
            // remove item from member
            remove_item: function(event) {
                event.preventDefault();
				var elem = $(event.currentTarget);
                var target = elem.attr('ajax:target');
				var options = bdajax.parsetarget(target);
				$.extend(options, {
					action_id: 'remove_item',
                    success: function(data) {
                        if (!data) {
                            bdajax.error('Empty response');
                            return;
                        }
                        if (!data.success) {
                            bdajax.error(data.message);
                            return;
                        }
						elem.unbind();
                        elem.removeClass('remove_item');
                        elem.addClass('remove_item_disabled');
						elem.bind('click', function(event) {
                            event.preventDefault();
                        });
                        var add = $('.add_item_disabled', elem.parent());
                        add.unbind();
                        add.removeClass('add_item_disabled');
                        add.addClass('add_item');
                        add.bind('click', ugm.actions.add_item);
                    }
                });
				ugm.actions.perform(options);
            },
            
            // perform listing item action
            perform: function(config) {
                bdajax.request({
                    url: bdajax.parseurl(config.url) + '/' + config.action_id,
                    type: 'json',
                    params: config.params,
                    success: config.success
                });
            }
        },
        
        // bind listing filter
        listing_filter_binder: function(context) {
            
            // reset filter input field
            $('div.column_filter input', context).bind('focus', function() {
                this.value = '';
                $(this).css('color', '#000');
            });
            
            // refresh focused column with filtered listing
            $('div.column_filter input', context).bind('keyup', function() {
                var current_filter = this.value.toLowerCase();
                $('div.columnlisting li', $(this).parent().parent())
                    .each(function() {
                        var li = $(this);
                        var val = $('div.head', li).html().toLowerCase();
                        if (val.indexOf(current_filter) != -1) {
                            li.removeClass('hidden');
                        } else {
                            li.addClass('hidden');    
                        }
                    });
            });
        },
        
        // reset selcted item in listing
        reset_listing_selected: function(li) {
            $('li', li.parent()).removeClass('selected');
            li.addClass('selected');
        },
		
		// bind related items filter
		listing_related_binder: function(context) {
			var sel = $('#related_filter', context);
            sel.unbind();
            sel.bind('click', ugm.listing_related_cb);
		},
		
		// callback when related filter gets toggled
		listing_related_cb: function(event) {
			var elem = $(this);
			var action;
			if (elem.attr('checked')) {
				action = 'columnlisting';
			} else {
				action = 'allcolumnlisting';
			}
			var target = bdajax.parsetarget(elem.attr('ajax:target'));
            bdajax.action({
                name: action,
                selector: 'div.right_column .columnlisting',
                mode: 'replace',
                url: target.url,
                params: target.params
            });
		}
    };
    
})(jQuery);