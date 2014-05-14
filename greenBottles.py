##10 GREEN BOTTLES - MATTHEW HEAVENS##

import time
bottles = 10
sNeeded = "s"
for x in range(10):
    print("{0} green bottle{1}, hanging on the wall".format(bottles,sNeeded))
    time.sleep(1)
    print("{0} green bottle{1}, hanging on the wall".format(bottles,sNeeded))
    time.sleep(1)
    print("And if 1 green bottle should acidentally fall,")
    time.sleep(1)
    bottles = bottles-1
    if bottles == 1:
        sNeeded = ""
    else:
        sNeeded = "s"
    print("They'll be {0} green bottle{1} hanging on the wall.".format(bottles,sNeeded))
    time.sleep(1)
