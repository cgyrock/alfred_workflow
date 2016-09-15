#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__='Drol'

import sys
from workflow import Workflow, ICON_WEB, web

URL_BILI_SUGGEST = 'http://s.search.bilibili.com/main/suggest'

params = {'jsoncallback':''
	,'func':'suggest'
	,'suggest_type':'accurate'
	,'sub_type':'tag'
	,'main_ver':'v1'
	#,'highlight':''
	#,'userid':'1357442'
	,'bangumi_acc_num':'1'
	,'special_acc_num':'1'
	,'topic_acc_num':'1'
	,'upuser_acc_num':'3'
	,'tag_num':'10'
	,'special_num':'10'
	,'bangumi_num':'10'
	,'upuser_num':'3'
	,'term':''
	#,'rnd':'0.8777030278949041'
	#,'_':'1473911858269'
}

def main(wf):	
	if len(wf.args) > 0:
		kw = wf.args[0]
		wf.add_item(u'搜索bilibili.com', arg=kw, valid=True, icon='icon.png')
		get_suggest(kw)

	wf.send_feedback()

def get_suggest(keyword):
	params['term'] = keyword
	r = web.get(URL_BILI_SUGGEST, params)
	r.raise_for_status()
	rs = r.json()
	if(rs['code'] != 0 or not rs.has_key('result') or len(rs['result']) == 0):
		return

	for v in r.json()['result']['tag'] :
		name = v['name']
		wf.add_item(name, arg=name, valid=True, icon='rs_icon.png') 

if __name__ == '__main__':
	wf = Workflow()
	sys.exit(wf.run(main)) 

