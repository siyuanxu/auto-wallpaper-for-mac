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

### fake code

```
判断 python 版本 引入库
如果当前路径中已有超过 5 张图片
	删除所有图片
获取 collection random img 下载链接
对下载链接的参数进行设定
命名下载文件为 unsplash + time tag.jpg
设为桌面背景
```

### 使用说明

1. download release
2. 如果希望修改图源为自己的 collection 或者需要更高分辨率的图片，可以在 macosplash.py 的 user configuration 部分进行相应修改
3. ​

