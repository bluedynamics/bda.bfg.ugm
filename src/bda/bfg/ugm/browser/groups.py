from yafowil.base import factory
from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.form import EditForm
from bda.bfg.ugm.model.groups import Groups

@tile('leftcolumn', 'templates/left_column.pt', interface=Groups,
      permission='login')
class GroupsLeftColumn(Tile):
    
    add_label = u"Add Group"

@tile('rightcolumn', 'templates/right_column.pt', interface=Groups,
      permission='login')
class GroupsRightColumn(Tile):
    pass

@tile('editform', interface=Groups, permission="view")
class GroupEditForm(EditForm):
    """XXX: bind to group.
    """
    
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