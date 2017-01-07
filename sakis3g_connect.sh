# Activate 3G DGCOM Viettel
# 
# With Raspberry Pi, you can easily put it in /etc/rc.local for 
# auto starting after booting

printf "INFO: Auto connecting to 3G dongle\n"
sakis3g --console connect APN='e-connect' APN_USER='0' APN_PASS='0'
