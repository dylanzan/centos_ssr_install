带有vps测速脚本(请使用CentOS 7.2)
```
cd /opt && wget -N --no-check-certificate https://raw.githubusercontent.com/zanshichun/centos_ssr_install/master/vps_speedtest.py && chmod +x /opt/vps_speedtest.py && python /opt/vps_speedtest.py
```
&nbsp;

# SSR的几个默认设置：
- ssr代码安装在`/home/ssr/`下。
- 默认的加密方式是：`chacha20-ietf`
- 默认的协议是：`auth_sha1_v4_compatible`
- 默认的混淆是：`tls1.2_ticket_auth_compatible`

# SSR的一键安装命令：
```
wget -N --no-check-certificate https://raw.githubusercontent.com/zanshichun/centos_ss_install/master/ssr-install.sh && bash ssr-install.sh
```

# SSR一键包的几个命令：

- 添加用户：`ssr adduser`
- 删除用户：`ssr deluser`
- 启动SSR：`ssr start`
- 停止SSR：`ssr stop`
- 重启SSR：`ssr restart`
- 卸载SSR：`ssr uninstall`
- 更新SSR：`ssr update`

# 如果你想自己修改用户和的加密，混淆和协议的话：
修改`vi /home/ssr/mudb.json`文件
```
[
{
"d": 0,
"enable": 1,
"method": "chacha20-ietf",
"obfs": "tls1.2_ticket_auth_compatible",
"passwd": "password",
"port": port,
"protocol": "auth_sha1_v4_compatible",
"transfer_enable": 9007199254740992,
"u": 0,
"user": "username"
}
]
```
几个参数的说明：
- method：加密方法
- passwd：ssr密码
- port：ssr端口
- protocol：协议
- obfs：混淆
- transfer_enable：流量

大家可以自己视情况修改。

## 一键安装最新内核并开启BBR方法（感谢@秋水逸冰）：

使用 root 用户登录，运行以下命令：
```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh
```

安装完成后，脚本会提示需要重启 VPS ，输入 y 并回车后重启。
重启完成后，进入 VPS ，验证一下是否成功安装最新内核并开启 TCP BBR ，输入以下命令：

```
uname -r
```
查看内核版本，含有 4.13 就表示 OK 了

```
sysctl net.ipv4.tcp_available_congestion_control
```
返回值一般为：
net.ipv4.tcp_available_congestion_control = bbr cubic reno

```
sysctl net.ipv4.tcp_congestion_control
```
返回值一般为：
net.ipv4.tcp_congestion_control = bbr

```
sysctl net.core.default_qdisc
```
返回值一般为：
net.core.default_qdisc = fq

```
lsmod | grep bbr
```
返回值有 tcp_bbr 模块即说明 bbr 已启动。


本仓库仅是个人兴趣爱好、为学习科研开发技术，方便，而设计，不可投入商用！遵守法律，人人有责！