#### 开发思路：

在实现微信抖音 自动加好友，并不是用的微信官方提供的api接口，是模拟点击手机屏幕操作。需要准备好：一部安卓手机、python环境、UIAutomator2、weditor 。

1. 安卓手机：(小米平板五) 无特殊要求，能正常使用的安卓手机即可进入设置，打开开发者模式。
2. python环境：python3
3. UIAutomator2：是一个可以使用Python对Android设备进行UI自动化的库
4. weditor： weditor 工具来进行手机元素识别，将对应的元素传给UIAutomator2。

### **1.环境准备**

**1.1 UIAutomator2安装和初始化**
	UIAutomator2安装

```
pip3 install --pre -U uiautomator2
```

​	UIAutomator2初始化

```
python -m uiautomator2 init
```

****
**1.2 运行python代码的pc连接手机**			

手机连接pc，adb命令保证能正确读取到设备。有两种方法：

​			1.通过WIFI，WiFi连接更方便一点，需要保持PC和手机使用的一个WIFI，查看手机连接WIFI的IP地址手机的IP可以在设置-WIFI设置里面获取到。

```
import uiautomator2 as u2
c = u2.connect('192.168.168.108')
```

​			2.通过USB数据线将手机链接电脑。手机的设备编号可以通过adb devices命令获取到

【**获取手机设备编号**】下载一个adb开发工具包，配置下环境变量。连接到电脑之后，进行cmd窗口，输入如下命令，便可以查看设备的手机设备编号

```
adb devices
```

【**uiautomator2 连接设备**】
  通过python代码，使用uiautomator2 模块连接手机。

```
import uiautomator2 as u2
c = u2.connect_usb('abcdef')
```

**1.3 weditor安装**

```
pip install -U weditor
```

1. pc终端输入

   ```
   webditor
   ```

   浏览器自动打开网页 [http://atx.open.netease.com](http://atx.open.netease.com/)	

2. 网页对应位置输入手机设备ip，点击connect连接手机设备，最后根据需要获取手机/app对应元素。连接顺序如下：
     step1：设备id输入
     step2：Connect连接
     step3：reload刷新页面

### **2.微信代码展示**

```
import uiautomator2 as u2
import pandas as pd
import time
import weditor

# 通过wifi连接
d = u2.connect_usb('a0029b1a')

# 添加好友
def addfriend(tel, company, text, i):
    # 点击添加好友
    d.xpath('//*[@resource-id="com.tencent.mm:id/j69"]').click()
    # 填入手机号
    d(resourceId="com.tencent.mm:id/cd7").set_text(tel)
    time.sleep(2)
    # 点击搜索
    d.xpath('//*[@resource-id="com.tencent.mm:id/j6x"]/android.widget.RelativeLayout[1]').click()
    time.sleep(2)
    # 判断用户是否存在
    if (d.exists(text="该用户不存在")):
        d(resourceId="com.tencent.mm:id/apy").click()
        null = i
        return null
    elif (d.exists(text="被搜帐号状态异常，无法显示")):
        print(tel, "被搜帐号状态异常，无法显示")
        d.press("back")
        null = i
        return null
    elif (d.exists(text="添加到通讯录")):
        d(resourceId="com.tencent.mm:id/khj").click()
        # 发生好友申请说明
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0w"]').set_text(text)
        # 设置备注
        time.sleep(1)
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0z"]').set_text(company)
        d(resourceId="com.tencent.mm:id/e9q").click()
        print(tel, "发送加好友请求成功")
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.press("back")
        null = i
        return null
    elif (d.exists(text="申请添加朋友")):
        # 发生好友申请说明
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0w"]').set_text(text)
        # 设置备注
        time.sleep(1)
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0z"]').set_text(company)
        d(resourceId="com.tencent.mm:id/e9q").click()
        print(tel, "发送加好友请求成功")
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.press("back")
        null = i
        return null
    elif (d.exists(text="发消息")):
        print(tel, "已经是您的好友")
        d.xpath('//*[@resource-id="com.tencent.mm:id/g1"]').click()
        d.xpath('//*[@resource-id="com.tencent.mm:id/apy"]').click()
        null = i
        return null

# 读取文件中的微信账号
def main():
    data = pd.read_csv('name.csv',encoding='utf-8',)
    # 以company列 删除重复行
    data.drop_duplicates('company', inplace=True)
    data.reset_index()
    # 自定义添加好友语句
    text = '老板你好,我是专业做各种自动门、防火门、卷帘门的'
    for i in range(len(data['tel'])):
        tel = str(data['tel'][i])
        company = str(data['company'][i])
        result = addfriend(tel, company, text, i)
        try:
            data.drop(result, inplace=True)
        except:
            pass
        data.to_csv('name.csv', index=False)
main()
```

### 3.抖音代码展示

```

```

