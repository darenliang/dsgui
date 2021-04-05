import glob
import subprocess
from pathlib import Path

if __name__ == "__main__":
    for file in glob.iglob("gui/*.ui"):
        subprocess.run(
            ["pyuic5", file, "-o",
             f"gui/{Path(file).stem}.py"
             ]
        )
