On the RPi with BMP180 sensor connected run
```
./server.py --addr fe80::bcef:ff:fe00:1111%lowpan0
```

On the other RPi
```
./client.py --addr [fe80::bcef:ff:fe00:1111%lowpan0]
```