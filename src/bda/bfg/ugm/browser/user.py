from odict import odict
from paste.httpexceptions import HTTPFound
from zodict import AttributedNode
from yafowil.base import (
    factory,
    UNSET,
)
from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.app.browser.utils import (
    make_url,
    make_query,
)
from bda.bfg.app.browser.form import (
    AddForm,
    EditForm,
)
from bda.bfg.ugm.model.interfaces import IUser
from bda.bfg.ugm.browser.columns import Column
from bda.bfg.ugm.browser.batch import ColumnBatch
from bda.bfg.ugm.browser.listing import ColumnListing

@tile('leftcolumn', interface=IUser, permission='view')
class UserLeftColumn(Column):
    
    add_label = u"Add User"
    
    def render(self):
        print self.model
        self.request['_curr_listing_id'] = self.model.__name__
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
    
    slot = 'rightlisting'
    
    @property
    def items(self):
        ret = list()
        return ret
#        for i in range(10):
#            item_target = make_url(self.request,
#                                   node=self.model.root['groups'],
#                                   resource=u'group%i' % i)
#            action_query = make_query(id=u'group%i' % i)
#            action_target = make_url(self.request,
#                                     node=self.model.root['users'],
#                                     resource=self.model.__name__,
#                                     query=action_query)
#            ret.append({
#                'target': item_target,
#                'head': 'User in Group - Group %i' % i,
#                'current': False,
#                'actions': [
#                    {
#                        'id': 'add_item',
#                        'enabled': False,
#                        'title': 'Add selected User to Group',
#                        'target': action_target,
#                    },
#                    {
#                        'id': 'remove_item',
#                        'enabled': True,
#                        'title': 'Remove selected User from Group',
#                        'target': action_target,
#                    },
#                ],
#            })
#        return ret

@tile('allcolumnlisting', 'templates/column_listing.pt',
      interface=IUser, permission='view')
class AllUserColumnListing(ColumnListing):
    
    slot = 'rightlisting'
    
    @property
    def items(self):
        ret = list()
        for i in range(10):
            item_target = make_url(self.request,
                                   node=self.model.root['groups'],
                                   resource=u'group%i' % i)
            action_query = make_query(id=u'group%i' % i)
            action_target = make_url(self.request,
                                     node=self.model.root['users'],
                                     resource=self.model.__name__,
                                     query=action_query)
            ret.append({
                'target': item_target,
                'head': 'User in Group - Group %i' % i,
                'current': False,
                'actions': [
                    {
                        'id': 'add_item',
                        'enabled': False,
                        'title': 'Add selected User to Group',
                        'target': action_target,
                    },
                    {
                        'id': 'remove_item',
                        'enabled': True,
                        'title': 'Remove selected User from Group',
                        'target': action_target,
                    },
                ],
            })
        return ret

class UserForm(object):
    
    @property
    def form(self):
        resource = 'add'
        if self.model.__name__ is not None:
            resource = 'edit'
        action = make_url(self.request, node=self.model, resource=resource)
        form = factory(u'form',
                       name='userform',
                       props={'action': action})
        settings = self.model.root['settings']
        attrmap = settings.attrs.users_form_attrmap
        if not attrmap:
            return form
        for key, val in attrmap.items():
            chain = 'field:error:label:mode:text'
            if key == 'userPassword':
                chain = 'field:error:label:password'
            props = {
                'label': val,
            }
            if key in ['userPassword']:
                props['required'] = 'No %s defined' % val
            if key in ['id', 'login'] and resource == 'edit':
                props['mode'] = 'display'
            value = UNSET
            if resource == 'edit':
                value = self.model.attrs.get(key, '')
            form[key] = factory(
                chain,
                value = value,
                props = props
            )
        form['save'] = factory(
            'submit',
            props = {
                'action': 'save',
                'expression': True,
                'handler': self.save,
                'next': self.next,
                'label': 'Save',
            })
        if resource =='add':
            form['cancel'] = factory(
                'submit',
                props = {
                    'action': 'cancel',
                    'expression': True,
                    'next': self.next,
                    'label': 'Cancel',
                    'skip': True,
                })
        return form

@tile('addform', interface=IUser, permission="view")
class UserAddForm(UserForm, AddForm):
    
     def save(self, widget, data):
        settings = self.model.root['settings']
        attrmap = settings.attrs.users_form_attrmap
        user = AttributedNode()
        for key, val in attrmap.items():
            user.attrs[key] = data.fetch('userform.%s' % key).extracted
        users = self.model.__parent__.ldap_users
        users[user.attrs['id']] = user
        users.context()
    
     def next(self, request):
        return HTTPFound(make_url(request.request, node=self.model))

@tile('editform', interface=IUser, permission="view")
class UserEditForm(UserForm, EditForm):
    
    def save(self, widget, data):
        pass
    
    def next(self, request):
        return HTTPFound(make_url(request.request, node=self.model))