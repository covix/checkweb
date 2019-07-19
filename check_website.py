import requests
import click
import time
from slack import WebClient

import settings


def send_message(to, text, icon_emoji=':alarm_clock:', username='@CheckWeb'):
    sc = WebClient(token=settings.TOKEN)

    sc.chat_postMessage(
        channel=to,  # or '@to_user'
        text=text,
        icon_emoji=icon_emoji,
        username=username  # username is the "sender" name
    )


@click.command()
@click.argument('url')
@click.argument('monitoring_name')
@click.argument('to')
@click.option('--seconds', default=5, help='Seconds to wait between each call.')
def main(url, monitoring_name, to, seconds):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'
    }

    username = f'{monitoring_name}@CheckWeb'

    text = f'Captain, I started monitoring {url} with the name `{monitoring_name}`'
    send_message(to, text, username=username)

    response = requests.get(url, headers=headers)
    last_response_text = response.text

    while True:
        time.sleep(seconds)
        response = requests.get(url, headers=headers)

        if last_response_text != response.text:
            last_response_text == response.text

            text = f"While on guard, I found that `{monitoring_name}` changed "\
                f"@ {url}, captain!"

            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(current_time, ':', text)

            send_message(to, text, username=username)


if __name__ == '__main__':
    main()
