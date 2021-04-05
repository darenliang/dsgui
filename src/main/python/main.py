from fbs_runtime.application_context.PyQt5 import ApplicationContext

from utils import dscli
from widgets.tray import SystemTray

from assets import resources  # noqa

if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext

    dscli.setup()

    appctxt.app.setQuitOnLastWindowClosed(False)
    #
    # Prevent system tray to be GC'd away
    #
    system_tray = SystemTray(appctxt.app)
