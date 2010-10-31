from repoze.bfg.view import static
from bda.bfg.app import browser
browser.MAIN_TEMPLATE = 'bda.bfg.ugm.browser:templates/main.pt'
browser.ADDITIONAL_CSS.append('bda.bfg.ugm.static/styles.css')

static_view = static('static')