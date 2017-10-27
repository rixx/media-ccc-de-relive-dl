#!/usr/bin/env python3
import json
import sys

import requests
import youtube_dl


def _check_youtube_dl(ydl):
    try:
        ydl.get_info_extractor(ie_key='StreamingCCC')
    except KeyError:
        print('Please install a version of youtube-dl that can download relives.')
        print('  pip install -U git+https://github.com/rixx/youtube-dl@ccc-de-relive')
        sys.exit(1)


def main():

    if len(sys.argv) != 2:
        print('Please provide an event slug!')
        return

    event_slug = sys.argv[-1]
    print('Using "{slug}" as event slug.'.format(slug=event_slug))

    response = requests.get('http://live.dus.c3voc.de/relive/{slug}/index.json'.format(slug=event_slug))
    if not response or response.status_code != 200:
        print('Could not read API response, sorry.')
        print(response.status_code)
        print(response.content)
        return

    try:
        recordings = json.loads(response.content.decode())
    except Exception as e:
        print('Could not decode API response: {exception}'.format(str(e)))
        return

    total = len(recordings)
    with youtube_dl.YoutubeDL() as ydl:
        _check_youtube_dl(ydl)

        for index, recording in enumerate(recordings):
            talk_id = recording['id']
            url = 'https://streaming.media.ccc.de/{event}/relive/{talk_id}'.format(event=event_slug, talk_id=talk_id)

            if not recording.get('mp4'):
                try:
                    print('ERROR: No mp4 linked for talk: {title}'.format(title=recording.get('title', '')))
                except:
                    print('ERROR: No mp4 linked for a talk that must not be named. Its URL is {url}.'.format(url=url))
                continue

            try:
                print('Downloading {current}/{total}: {title}'.format(current=index, total=total, title=recording['title']))
                ydl.download([url])
            except Exception as e:
                print('DEBUG: {}'.format([url]))
                print('ERROR: Failed to download: {err}'.format(err=str(e)))


if __name__ == '__main__':
    main()
