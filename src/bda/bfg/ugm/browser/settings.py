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
        # XXX
        return 'OK'
        #return 'Failed'

@tile('editform', interface=ISettings, permission="view")
class LDAPSettingsForm(EditForm):
    
    @property
    def form(self):
        form = factory(u'form',
                       name='editform',
                       props={'action': '%s/edit' % self.nodeurl})
        form['server'] = factory(
            'field:label:error:text',
            value = self.model.attrs.server,
            props = {
                'required': 'No server defined',
                'label': 'LDAP Server',
            })
        form['port'] = factory(
            'field:label:error:text',
            value = self.model.attrs.port,
            props = {
                'required': 'No port defined',
                'label': 'LDAP Port',
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
        form['groups_dn'] = factory(
            'field:label:error:text',
            value = self.model.attrs.groups_dn,
            props = {
                'required': 'No Groups DN defined',
                'label': 'Groups Base DN',
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
        self.model.attrs.server = data.fetch('editform.server').extracted
        self.model.attrs.port = data.fetch('editform.port').extracted
        self.model.attrs.user = data.fetch('editform.user').extracted
        self.model.attrs.password = data.fetch('editform.password').extracted
        self.model.attrs.users_dn = data.fetch('editform.users_dn').extracted
        self.model.attrs.groups_dn = data.fetch('editform.groups_dn').extracted
        self.model()