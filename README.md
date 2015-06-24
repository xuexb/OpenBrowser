# openbrowser
在sublime里打开浏览器，可以自定义配置打开的`uri`

感谢[@ququ](https://www.imququ.com)

## 安装
1. `git clone https://github.com/xuexb/OpenBrowser.git`
2. `mv ./OpenBrowser ${packages}`

## 路径配置
打开方式：

1. 包配置->OpenBrowser->Settings – User
2. `${packages}/User/OpenBrowser.sublime-settings`

```json
{
    "path": {
        "/Users/xxoo/work/tests/": "http://192.168.199.2/",
        "C:\\web\\html5\\" : "http://192.168.199.2/"
    }
}
```

## 快捷键配置

`command : open_browser` 