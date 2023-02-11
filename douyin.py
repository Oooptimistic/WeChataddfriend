import uiautomator2 as u2
import pandas as pd
import random
import time

# 通过USB连接
d = u2.connect_usb('a0029b1a')
def focus(tel, i):
    # 填入手机号
    time.sleep(random.randint(1,3))
    d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/fgy"]').set_text(tel)
    # 点击搜索
    d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/p6+"]/android.widget.LinearLayout[1]').click()
    # 点击关注
    d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/fx8"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()
    null = i
    return null


def main():
    data = pd.read_csv('f_name.csv',encoding='utf-8',)
    # 以company列 删除重复行
    data.drop_duplicates('company', inplace=True)
    data.reset_index()
    # 自定义添加好友语句
    for i in range(len(data['tel'])):
        tel = str(data['tel'][i])
        result = focus(tel, i)
        try:
            data.drop(result, inplace=True)
        except:
            pass
        data.to_csv('f_name.csv', index=False)
main()