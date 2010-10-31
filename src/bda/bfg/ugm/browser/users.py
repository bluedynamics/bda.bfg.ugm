from yafowil.base import factory
from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.form import EditForm
from bda.bfg.ugm.model.users import Users

@tile('leftcolumn', 'templates/left_column.pt', interface=Users,
      permission='login')
class UsersLeftColumn(Tile):
    
    add_label = u"Add User"

@tile('rightcolumn', 'templates/right_column.pt', interface=Users,
      permission='login')
class UsersRightColumn(Tile):
    pass

@tile('editform', interface=Users, permission="view")
class UserEditForm(EditForm):
    """XXX: bind to user.
    """
    
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