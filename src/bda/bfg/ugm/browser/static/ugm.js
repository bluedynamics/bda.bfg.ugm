(function($) {
    
    $(document).ready(function() {
        ugm.left_listing_nav_binder();
        ugm.right_listing_nav_binder();
        ugm.listing_filter_binder();
        ugm.listing_actions_binder();
        bdajax.binders.left_listing_nav_binder = ugm.left_listing_nav_binder;
        bdajax.binders.right_listing_nav_binder = ugm.right_listing_nav_binder;
        bdajax.binders.listing_filter_binder = ugm.listing_filter_binder;
        bdajax.binders.listing_actions_binder = ugm.listing_actions_binder;
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
            var delete_actions = $('div.actions a.delete_item', context);
            delete_actions.unbind();
            delete_actions.bind('click', ugm.actions.delete_item);
            var add_actions = $('div.actions a.add_item', context);
            add_actions.unbind();
            add_actions.bind('click', ugm.actions.add_item);
            var remove_actions = $('div.actions a.remove_item', context);
            remove_actions.unbind();
            remove_actions.bind('click', ugm.actions.remove_item);
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
                        }
                        if (!data.success) {
                            bdajax.error(data.message);
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
            },
            
            // remove item from member
            remove_item: function(event) {
                event.preventDefault();
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
        }
    };
    
})(jQuery);