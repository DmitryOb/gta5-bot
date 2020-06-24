import subprocess
import pathlib

path_to_clicker = str(pathlib.Path(__file__).parent.absolute()) + '/clickermann/Clickermann.exe'

def clicker_script_run(script_path):
    subprocess.run(
        f'{path_to_clicker} {script_path}',
        check=True,
        shell=True
    )
