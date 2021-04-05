import platform
from pathlib import Path

dsgui_version = "1.0.0"
dscli_version = "1.8.0"

dscli_bin = f"{Path.home().as_posix()}/.dsgui/bin/dscli{'.exe' if platform.system() == 'Windows' else ''}"