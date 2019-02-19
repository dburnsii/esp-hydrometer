import network
import usocket as socket
import gc

gc.collect()

try:
    f = open('wifi.txt')
    credentials = f.read().split(',')
    f.close()

    ssid = credentials[0]
    psk = credentials[1]

    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    sta_if.connect(ssid, psk)

if( sta_if.isconnected() ):
  ap_if.active(False)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
