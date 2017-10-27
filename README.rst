media.ccc.de (relive) downloader
--------------------------------

For one reason or another, you might want to download all Relive videos from
streaming.media.ccc.de. This script helps you to do so.

Installation
============

Installation is a bit tricky since you'll need youtube-dl with streaming.media.ccc.de
support, which is a not-yet-merged feature.

1. Start a virtualenv for this script.
2. Install the required dependencies: `pip install requests`
3. Install the required youtube-dl branch: `pip install -U git+https://github.com/rixx/youtube-dl@ccc-de-relive`
4. Find your (case insensitive) event slug by looking up your event on https://streaming.media.ccc.de
5. Execute this script: `./download_relives.py pw17`
