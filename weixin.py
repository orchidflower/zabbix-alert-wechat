#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from urllib import urlencode
import json
import sys
import re

class WeChat:
	PATTERN_GROUPID = re.compile(r'\d+')
	
	def __init__(self,url,Corpid,Secret): 
		url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url,Corpid,Secret)
		res = self.doRequest(url)
		self.token = res['access_token']
#		print self.token
		
	def doRequest(self,url,method='get',data={}):
		if method == 'get':
			req = urllib2.Request(url)
			res = json.loads(urllib2.urlopen(req).read())
		elif method == 'post':
			req = urllib2.Request(url,data,{'Content-Type': 'text/xml; charset=utf-8'})
			res = json.loads(urllib2.urlopen(req).read(), 'utf-8')
		else:
			print 'error request method...exit'
			sys.exit()  
		return res

	def sendMessage(self,userlist,content,agentid=0):
		self.userlist = userlist
		self.content = content
		url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % self.token
		data = {
					"touser": "",
					"toparty": "",
#					"totag": "",
					"msgtype": "text",
					"agentid": "0",
					"text": {
						"content": ""
					},
					"safe":"0"
				}
		# if the userlist is all digits, consider it as a group id
		if self.PATTERN_GROUPID.match(userlist):
			data['toparty'] = userlist
		else:
			data['touser'] = userlist
		data['agentid'] = agentid
		data['text']['content'] = content
		data = json.dumps(data,ensure_ascii=False,encoding='utf-8')
		res = self.doRequest(url,method='post',data=data)
		if res['errmsg'] == 'ok':
			print 'send sucessed!!!'
		else:
			print 'send failed!!'
			print res


if __name__ == '__main__':  
	reload(sys)
	sys.setdefaultencoding( "utf-8" )
	userlist = sys.argv[1]
	content = sys.argv[2:]
	content = '\n'.join(content)
	
#    output = open('/tmp/log.log', 'a')
#    output.write(userlist)
#    output.write('\n')
#    output.write(content)
#    output.write('\n')
#    output.write('\n')
#    output.close()

	# TODO: Replace with your own settings
	Corpid = '------------'
	Secret = '++++++++++++'
	AgentID = 1
	url = 'https://qyapi.weixin.qq.com'

	WeChat = WeChat(url,Corpid,Secret)
	WeChat.sendMessage(userlist,content,AgentID)