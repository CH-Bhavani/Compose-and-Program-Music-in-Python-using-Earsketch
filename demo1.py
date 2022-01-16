#		python code
#		script_name:demo1
#
#		author:zoe
#		description:composition practice
#
from earsketch import *
init()
setTempo(120)
#secondarybeat=HIPHOP_BASSSUB_001
fitMedia(ZOE9_BEAUTIFUL, 2,1, 12)
setEffect(1,VOLUME,GAIN,-60,1,5,12)
setEffect(1,VOLUME,GAIN,5,12,-60,16)
fitMedia(ZOE9_STAY_WITH_ME_OST,1,1,16)
setEffect(3,DELAY,DELAY_TIME,500)
fitMedia(ZOE9_STAY_WITH_ME_OST,3,1,8)
setEffect(3,REVERB,REVERB_TIME,200)
finish()