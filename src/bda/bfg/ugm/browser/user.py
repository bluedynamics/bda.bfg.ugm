from yafowil.base import factory
from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import make_url
from bda.bfg.app.browser.form import EditForm
from bda.bfg.ugm.model.interfaces import IUser
from.bda.bfg.ugm.browser.columns import Column
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', interface=IUser, permission='view')
class UserLeftColumn(Column):
    
    add_label = u"Add User"
    
    def render(self):
        self.request['_listing_current_id'] = self.model.__name__
        return self._render(self.model.__parent__, 'leftcolumn')

@tile('rightcolumn', 'templates/right_column.pt',
      interface=IUser, permission='view')
class UserRightColumn(Tile):
    pass

@tile('columnbatch', interface=IUser, permission='view')
class UserColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=IUser, permission='view')
class UserColumnListing(ColumnListing):
    
    @property
    def items(self):
        ret = list()
        for i in range(10):
            ret.append({
                'target': make_url(self.request,
                                   node=self.model.root['groups'],
                                   resource=u'group%i' % i),
                'head': 'User in Group - Group %i' % i,
                'current': False,
                'actions': [
                    {
                        'id': 'add_item',
                        'enabled': True,
                        'title': 'Add selected User to Group',
                    },
                    {
                        'id': 'remove_item',
                        'enabled': True,
                        'title': 'Remove selected User from Group',
                    },
                ],
            })
        return ret

@tile('editform', interface=IUser, permission="edit")
class UserEditForm(EditForm):
    
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
        form['email'] = factory(
            'field:error:label:text',
            value = '%s@my-domain.com' % self.model.__name__,
            props = {
                'label': 'E-Mail',
            })
        form['phone'] = factory(
            'field:error:label:text',
            value = '0815',
            props = {
                'label': 'Phone',
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