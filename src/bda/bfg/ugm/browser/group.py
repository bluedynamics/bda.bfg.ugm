from yafowil.base import factory
from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import make_url
from bda.bfg.app.browser.form import EditForm
from bda.bfg.ugm.model.group import Group
from.bda.bfg.ugm.browser.columns import Column
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', interface=Group, permission='view')
class GroupLeftColumn(Column):
    
    add_label = u"Add Group"
    
    def render(self):
        return self._render(self.model.__parent__, 'leftcolumn')

@tile('rightcolumn', 'templates/right_column.pt',
      interface=Group, permission='view')
class GroupRightColumn(Tile):
    pass

@tile('columnbatch', interface=Group, permission='view')
class GroupColumnBatch(ColumnBatch):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=Group, permission='view')
class GroupColumnListing(ColumnListing):
    
    @property
    def items(self):
        ret = list()
        for i in range(10):
            ret.append({
                'target': make_url(self.request,
                                   node=self.model.root['users'],
                                   resource=u'user%i' % i),
                'left': 'Group Member',
                'right': 'User %i' % i,
            })
        return ret

@tile('editform', interface=Group, permission="view")
class GroupEditForm(EditForm):
    
    @property
    def form(self):
        form = factory(u'form',
                       name='editform',
                       props={'action': self.nodeurl})
        form['name'] = factory(
            'field:error:label:text',
            value = 'Gruppe 1',
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