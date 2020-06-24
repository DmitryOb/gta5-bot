from bot import *

restart_oil = script_dir + 'restart_oil.cms'

def oil_bot():
    subprocess.run(
        f'{path_to_clicker} {init}',
        check=True,
        shell=True
    )
    i = 0
    while True:
        i += 1
        clicker_script_run(oil)
        if i % 7 == 0:
            clicker_script_run(restart_oil)

oil_bot()
