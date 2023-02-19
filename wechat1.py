import uiautomator2 as u2
import pandas as pd
import time
# 爸

# 通过USB连接
d = u2.connect_usb('a0029b1a')

# 添加好友
def addfriend(tel, company, text, i):
    # 点击添加好友
    d.xpath('//*[@resource-id="com.tencent.mm:id/j69"]').click()
    # 填入手机号
    time.sleep(1)
    d(resourceId="com.tencent.mm:id/cd7").set_text(tel)
    time.sleep(4)
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
        time.sleep(3)
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0w"]').set_text(text)
        # 设置备注
        time.sleep(3)
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0z"]').set_text(company)
        time.sleep(2)
        d(resourceId="com.tencent.mm:id/e9q").click()
        print(tel, "发送加好友请求成功")
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.press("back")
        null = i
        return null
    elif (d.exists(text="申请添加朋友")):
        time.sleep(2)
        # 发生好友申请说明
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0w"]').set_text(text)
        # 设置备注
        time.sleep(3)
        d.xpath('//*[@resource-id="com.tencent.mm:id/j0z"]').set_text(company)
        time.sleep(3)
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
    data = pd.read_csv('name1.csv',encoding='utf-8',)
    # 以company列 删除重复行
    data.drop_duplicates('company', inplace=True)
    data.reset_index()
    # 自定义添加好友语句
    text = '老板您好,我是专业做各种自动门、防火门、卷帘门的希望能有机会与您合作'
    for i in range(len(data['tel'])):
        tel = str(data['tel'][i])
        company = str(data['company'][i])+'-**'
        result = addfriend(tel, company, text, i)
        try:
            data.drop(result, inplace=True)
        except:
            pass
        data.to_csv('name1.csv', index=False)
main()
