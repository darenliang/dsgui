import platform
from pathlib import Path

dsgui_version = "1.8.1"
dscli_version = "1.13.1"

dscli_bin = f"{Path.home().as_posix()}/.dsgui/bin/dscli{'.exe' if platform.system() == 'Windows' else ''}"
