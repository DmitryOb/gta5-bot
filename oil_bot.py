from bot import *
from cutter import full_cut
from matcher import task_render_calc

def oil_bot():
    subprocess.run(
        f'{path_to_clicker} {init}',
        check=True,
        shell=True
    )

    while True:
        clicker_script_run(oil)
        time.sleep(1)
        if task_is_open():
            full_cut("base_screen.png")
            true_answer = task_render_calc('cutted/0.png')
            try_match_true_answer(true_answer)
            time.sleep(2)
            restart_oil = '"D:/_Distr_Programs/Clickermann v4.13 x64/restart_oil.cms"'
            clicker_script_run(restart_oil)
