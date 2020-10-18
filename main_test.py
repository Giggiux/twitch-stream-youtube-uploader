from actors.twitch_coordinator import TwitchCoordinator
import math
import time
import logging

logging.basicConfig(level=logging.INFO)


coordinator = TwitchCoordinator.start().proxy()

channelsFile = 'channels.txt'

with open(channelsFile) as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
channels = [x.strip() for x in content]

logging.debug("adding channels")
for channel in channels:
    coordinator.add_channel(channel)

while True:
    time.sleep(60*60*24*365)