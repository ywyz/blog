Title: 编译安装ubuntu智能拼音输入法
Date: 2026-06-19 21:22
Category: 技术
Tags: 无影云电脑, Ubuntu，编译，输入法


# 缘起

Windows中习惯了微软拼音，实在习惯不了还可以搜狗、QQ、百度 and so on。可是Ubuntu系统不行。很多输入法不提供Linux版本，提供的看样子也都在deepin里面。搜狗提供的，但是版本太旧，还需要安装fcitx4 ，可是现在Ubuntu24.04 已经到了fcitx5了，我就得大改系统，还不一定能成功。

这不就类似于为了路上的韭菜买了一套房子吗？不乐意了。翻一翻系统自带智能拼音，还带有云输入，挺好挺好。

不过一翻软件关于，点击github仓库一看，居然不是最新版本的，可是ubuntu自带软件仓库里面并没有呀。滞后了怎么办，开启了我这辈子第一次还是第二次编译安装的路

# 做好安装准备

首先得做好安装环境的准备。

## 卸载旧版

```bash
#卸载旧版
sudo apt remove 'libpinyin*'
sudo apt remove 'ibus-libpinyin'
```

## 安装环境

```bash
# 安装环境
sudo apt install libibus-1.0-dev
sudo apt install libdb-dev
sudo apt install libsqlite3-dev
sudo apt install sqlite3
# 根据我的安装过程还需要安装
sudo apt install libsoup-3.0-dev
sudo apt install libjson-glib-dev
sudo apt install libnotify-dev
sudo apt install gnome-common 
```

## 下载软件

```bash
wget <https://github.com/libpinyin/libpinyin/releases/download/2.10.3/libpinyin-2.10.3.tar.gz>
wget <https://github.com/libpinyin/ibus-libpinyin/releases/download/1.16.5/ibus-libpinyin-1.16.5.tar.gz>

tar zxvf libpinyin-2.10.3.tar.gz
tar zxvf ibus-libpinyin-1.16.5.tar.gz

# 可以根据github上面最新的链接修改
```

# 编译安装

```bash
cd libpinyin-2.10.3/
./configure --prefix=/usr
make
sudo make install-strip
cd ..

cd ibus-libpibtyin-1.16.5
./autogen.sh --prefix=/usr --enable-cloud-input-mode # 开启云输入
make
sudo make-install

```

接下来重启电脑，就能享受最新版的ibus智能拼音了。
