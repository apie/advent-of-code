Add cronjobs for alerter.py <year> and redirect the output to a file.

    *    *  *   *   *    cd /home/telegram/aoc/ && /usr/bin/env python3 alerter.py 2022 > 2022/log.txt && send_last_log.bash 2022

`send_last_log.bash` sends the changes to telegram.
