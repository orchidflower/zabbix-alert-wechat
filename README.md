# zabbix-alert-wechat
With this script, Zabbix can send alert message via WeChat API.


# 1. 概述
Zabbix支持多种报警方式，例如邮件、短信等等。但是这些方式或多或少有一些限制，例如邮件经常被当成垃圾邮件；短信一方面有费用，另一方面受字数的限制，报警信息很难说清楚。随着微信发展，基于微信企业号的报警消息发送显得越来越有价值。

微信提供了公众号的功能。其中的企业号功能是针对公司、政府或者事业单位的。企业号可以无限的群发消息，它没有限制，因为，它针对的是它自己的用户。通过企业号，可以方便而且不受限的发送报警信息，非常有价值。

从网上经常能够搜索到的脚本都是基于bash shell的。但是这些脚本大多没有很好的处理Zabbix这种里面有特殊字符（例如%）和空格的报警信息。导致在微信上收到的信息格式总是有些错乱。所以才有了这一个Python版本的脚本。

# 2. 使用
首先修改脚本中`Corpid`,`Secret`,`AgentID`等几个参数为正确的值。然后在Zabbix中创建一个新的`Media Types`，选定`Type`为`Script`，选择本脚本即可。

# 3. 已知限制
本脚本接受至少两个参数：

第一个参数是报警消息接收人。如果该参数为数字，则假定其为企业号中的用户组，对应api参数中的`toparty`参数；如果不是数字，则认为是用户ID，对应api参数中的`touser`。具体请看微信api定义及代码。

第二个以及之后的所有参数都将被拼接成`content`参数，作为消息内容发送给接受者。

# 4. 参考资料
* [微信接口：消息类型及数据格式](http://qydev.weixin.qq.com/wiki/index.php?title=%E6%B6%88%E6%81%AF%E7%B1%BB%E5%9E%8B%E5%8F%8A%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F#text.E6.B6.88.E6.81.AF)
* [Zabbix Custom alertscripts](https://www.zabbix.com/documentation/3.2/manual/config/notifications/media/script)
