import platform
from pathlib import Path

dsgui_version = "1.7.0"
dscli_version = "1.12.3"

dscli_bin = f"{Path.home().as_posix()}/.dsgui/bin/dscli{'.exe' if platform.system() == 'Windows' else ''}"
