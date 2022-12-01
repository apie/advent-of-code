Add cronjobs for alerter.py <year> and redirect the output to a file.

    *    *  *   *   *    cd /home/telegram/aoc/ && /usr/bin/env python3 alerter.py 2022 > 2022/log.txt && send_last_log.bash 2022

Use start.bash to watch the file and send differences to telegram.
