import qdarkstyle
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from assets import resources  # noqa
from utils import dscli
from widgets.tray import SystemTray

if __name__ == '__main__':
    appctxt = ApplicationContext()

    #
    # Setup dscli
    #
    dscli.setup()

    #
    # Setup stylesheets
    #
    appctxt.app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    appctxt.app.setQuitOnLastWindowClosed(False)

    #
    # Prevent system tray to be GC'd away
    #
    system_tray = SystemTray(appctxt.app)
