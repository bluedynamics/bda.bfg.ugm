from yafowil.base import factory
from bda.bfg.tile import tile
from bda.bfg.app.browser.layout import ProtectedContentTile
from bda.bfg.app.browser.form import EditForm
from bda.bfg.ugm.model.interfaces import ISettings

@tile('content', 'templates/settings.pt', interface=ISettings,
      permission='login', strict=False)
class Settings(ProtectedContentTile):
    
    @property
    def ldap_status(self):
        if self.model.ldap_connectivity == 'success':
            return 'OK'
        return 'Down'
    
    @property
    def ldap_users(self):
        if self.model.ldap_users_container_valid:
            return 'OK'
        return 'Inexistent'
        
    @property
    def ldap_groups(self):
        if self.model.ldap_groups_container_valid:
            return 'OK'
        return 'Inexistent'

@tile('editform', interface=ISettings, permission="edit")
class LDAPSettingsForm(EditForm):
    
    @property
    def form(self):
        form = factory(u'form',
                       name='editform',
                       props={'action': '%s/edit' % self.nodeurl})
        form['uri'] = factory(
            'field:label:error:text',
            value = self.model.attrs.uri,
            props = {
                'required': 'No URI defined',
                'label': 'LDAP URI',
            })
        form['user'] = factory(
            'field:label:error:text',
            value = self.model.attrs.user,
            props = {
                'required': 'No user defined',
                'label': 'LDAP Manager User',
            })
        form['password'] = factory(
            'field:label:error:password',
            value = self.model.attrs.password,
            props = {
                'required': 'No password defined',
                'label': 'LDAP Manager Password',
            })
        form['users_dn'] = factory(
            'field:label:error:text',
            value = self.model.attrs.users_dn,
            props = {
                'required': 'No Users DN defined',
                'label': 'Users Base DN',
            })
        form['users_scope'] = factory(
            'field:label:error:text',
            value = self.model.attrs.users_scope,
            props = {
                'required': 'No users scope defined',
                'label': 'Users scope',
            })
        form['users_query'] = factory(
            'field:label:error:text',
            value = self.model.attrs.users_query,
            props = {
                'required': 'No users query defined',
                'label': 'Users query',
            })
        form['groups_dn'] = factory(
            'field:label:error:text',
            value = self.model.attrs.groups_dn,
            props = {
                'required': 'No Groups DN defined',
                'label': 'Groups Base DN',
            })
        form['groups_scope'] = factory(
            'field:label:error:text',
            value = self.model.attrs.groups_scope,
            props = {
                'required': 'No groups scope defined',
                'label': 'Groups scope',
            })
        form['groups_query'] = factory(
            'field:label:error:text',
            value = self.model.attrs.groups_query,
            props = {
                'required': 'No groups query defined',
                'label': 'Groups query',
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
        self.model.attrs.uri = data.fetch('editform.uri').extracted
        self.model.attrs.user = data.fetch('editform.user').extracted
        self.model.attrs.password = data.fetch('editform.password').extracted
        self.model.attrs.users_dn = data.fetch('editform.users_dn').extracted
        self.model.attrs.users_scope = data.fetch('editform.users_scope').extracted
        self.model.attrs.users_query = data.fetch('editform.users_query').extracted
        self.model.attrs.groups_dn = data.fetch('editform.groups_dn').extracted
        self.model.attrs.groups_scope = data.fetch('editform.groups_scope').extracted
        self.model.attrs.groups_query = data.fetch('editform.groups_query').extracted
        self.model()
        self.model.invalidate()