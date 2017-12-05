# Macosplash

Macosplash 可以通过 unsplash 的开放 API 来获取图片并定时设定为 macOS 的桌面背景。

## Requirements

- macOS
- Python 2.X 3.X
- appscript
    - pip install appscript

*Tested under macOS High Sierra python 2.7 python 3.5 python 3.6*

## 思路

1. unsplash 可以很方便的自己制作或者使用他人的 collection。
2. source.unsplash.com 可以很方便的随机抽取特定 collection 中的照片，而且还支持指定尺寸或者作者等等特性。
3. Python 的 appscript 库可以很好的与 macOS 平台的 AppleScript 相连接。


## 实现和使用

