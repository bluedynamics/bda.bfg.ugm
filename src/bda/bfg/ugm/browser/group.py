from yafowil.base import factory
from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import (
    make_url,
    make_query,
)
from bda.bfg.app.browser.form import EditForm
from bda.bfg.ugm.model.interfaces import IGroup
from.bda.bfg.ugm.browser.columns import Column
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', interface=IGroup, permission='view')
class GroupLeftColumn(Column):
    
    add_label = u"Add Group"
    
    def render(self):
        self.request['_curr_listing_id'] = self.model.__name__
        return self._render(self.model.__parent__, 'leftcolumn')

@tile('rightcolumn', 'templates/right_column.pt',
      interface=IGroup, permission='view')
class GroupRightColumn(Tile):
    pass

@tile('columnbatch', interface=IGroup, permission='view')
class GroupColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=IGroup, permission='view')
class GroupColumnListing(ColumnListing):
    
    slot = 'rightlisting'
    
    @property
    def items(self):
        ret = list()
        return ret
#        for i in range(10):
#            item_target = make_url(self.request,
#                                   node=self.model.root['users'],
#                                   resource=u'user%i' % i)
#            action_query = make_query(id=u'user%i' % i)
#            action_target = make_url(self.request,
#                                     node=self.model.root['groups'],
#                                     resource=self.model.__name__,
#                                     query=action_query)
#            
#            ret.append({
#                'target': item_target,
#                'head': 'Group Member - User %i' % i,
#                'current': False,
#                'actions': [
#                    {
#                        'id': 'add_item',
#                        'enabled': False,
#                        'title': 'Add User to selected Group',
#                        'target': action_target,
#                    },
#                    {
#                        'id': 'remove_item',
#                        'enabled': True,
#                        'title': 'Remove User from selected Group',
#                        'target': action_target,
#                    },
#                ],
#            })
#            
#        return ret

@tile('allcolumnlisting', 'templates/column_listing.pt',
      interface=IGroup, permission='view')
class AllGroupColumnListing(ColumnListing):
    
    slot = 'rightlisting'
    
    @property
    def items(self):
        ret = list()
        for i in range(10):
            item_target = make_url(self.request,
                                   node=self.model.root['users'],
                                   resource=u'user%i' % i)
            action_query = make_query(id=u'user%i' % i)
            action_target = make_url(self.request,
                                     node=self.model.root['groups'],
                                     resource=self.model.__name__,
                                     query=action_query)
            
            ret.append({
                'target': item_target,
                'head': 'Group Member - User %i' % i,
                'current': False,
                'actions': [
                    {
                        'id': 'add_item',
                        'enabled': False,
                        'title': 'Add User to selected Group',
                        'target': action_target,
                    },
                    {
                        'id': 'remove_item',
                        'enabled': True,
                        'title': 'Remove User from selected Group',
                        'target': action_target,
                    },
                ],
            })
            
        return ret

@tile('editform', interface=IGroup, permission="edit")
class GroupEditForm(EditForm):
    
    @property
    def form(self):
        form = factory(u'form',
                       name='editform',
                       props={'action': self.nodeurl})
        form['name'] = factory(
            'field:error:label:text',
            value = self.model.__name__,
            props = {
                'label': 'Name',
            })
        form['save'] = factory(
            'submit',
            props = {
                'action': 'save',
                'expression': True,
                'handler': self.save,
                'next': self.next,
                'label': 'Save',
            })
        return form
    
    def save(self, widget, data):
        pass