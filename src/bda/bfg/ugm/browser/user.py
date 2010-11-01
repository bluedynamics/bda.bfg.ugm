from yafowil.base import factory
from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.form import EditForm
from bda.bfg.ugm.model.user import User
from.bda.bfg.ugm.browser.columns import Column
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', 'templates/left_column.pt',
      interface=User, permission='view')
class UserLeftColumn(Column):
    
    add_label = u"Add User"
    
    def render(self):
        return self._render(self.model.__parent__, 'leftcolumn')

@tile('rightcolumn', 'templates/right_column.pt',
      interface=User, permission='view')
class UserRightColumn(Tile):
    pass

@tile('columnbatch', interface=User, permission='view')
class UserColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=User, permission='view')
class UserColumnListing(ColumnListing):
    pass

@tile('editform', interface=User, permission="view")
class UserEditForm(EditForm):
    
    @property
    def form(self):
        form = factory(u'form',
                       name='editform',
                       props={'action': self.nodeurl})
        form['name'] = factory(
            'field:error:label:text',
            value = 'Max Mustermann',
            props = {
                'label': 'Name',
            })
        form['email'] = factory(
            'field:error:label:text',
            value = 'foo@my-domain.com',
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
        form['cancel'] = factory(
            'submit',
            props = {
                'action': 'cancel',
                'expression': True,
                'handler': None,
                'next': self.next,
                'label': 'Cancel',
                'skip': True,
            })
        return form
    
    def save(self, widget, data):
        pass