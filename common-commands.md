```
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```

```
sudo passwd
```

```
raspi-config
```

config.txt
---
`hdmi_cvt=<width> <height> <framerate> <aspect> <margins> <interlace> <rb>`
| Value  | Default	| Description |
| ---    | ---      | --- |
| width	|(required)	|width in pixels|
| height	|(required)	|height in pixels|
| framerate	|(required)	|framerate in Hz|
| aspect	|3	|aspect ratio 1=4:3, 2=14:9, 3=16:9, 4=5:4, 5=16:10, 6=15:9|
| margins	|0	|0=margins disabled, 1=margins enabled|
| interlace	|0	|0=progressive, 1=interlaced|
| rb	|0	|0=normal, 1=reduced blanking|