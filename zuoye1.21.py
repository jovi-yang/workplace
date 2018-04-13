# coding=utf-8
'''
twitter文本附件的排序格式如下
fields=bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url
bid    消息ID
uid     用户ID
username 用户名
ugrade 用户等级字段
content(text) 微博内容
img(message包含图片链接)
created_at 微博发布时间
source(来源)
rt_num, 转发数
cm_num, 评论数
rt_uid, 转发UID
rt_username, 转发用户名
rt_v_class, 转发者等级
rt_content, 转发内容
rt_img, 转发内容所涉及图片
src_rt_num, 源微博回复数
src_cm_num, 源微博评论数
gender,(用户性别)
rt_mid（转发mid）
geo 地区
lat() 经度
lon 纬度
place 地点
hashtags
ats  @谁
rt_hashtags, 回复标签
rt_ats, 回复@谁
v_url, 源微博URL
rt_v_url 转发URL
'''
import time
with open('t21.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
t_ID = []
name = []
for x in text:
    l = x.split('","')[1]
    m = x.split('","')[2]
    t_ID.append(l)
    name.append(m.strip())
n = len(list(set(t_ID)))

# 1.该文本里，有多少个用户。（要求：输出为一个整数。）
#print('1.该文本里，有%s个用户。' % n)

# 2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
name1 = list(set(name))
# print('2.该文本里，每一个用户的名字: %s' % name1[:])

#3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）
issue = []
for x in text:
	t = x.split('","')[6]
	issue.append(t)
b = []
n = len(issue)
for x in range(n):
	if len(issue[x]) != 19:
		pass
	else:
		a = time.strptime(issue[x],'%Y-%m-%d %H:%M:%S')
		b.append(list(a))

t3 = [str(b[x][0])+str(b[x][1]) for x in range(n)]
#print('3.该文本里，有 %s 个2012年11月发布的tweets。' % t3.count('201211'))

#4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
tmp4 = [str(b[x][0])+'-'+str(b[x][1])+'-'+str(b[x][2]) for x in range(n)]
t4 = list(set(tmp4))
#print('4.该文本里，有哪几天的数据: %s' % t4)

#5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
t5 = [str(b[x][3]) for x in range(n)]
keys = list(set(t))
l = [[x,t.count(x)] for x in keys]
m = sorted(l, key=lambda x:x[1], reverse=True)
#print('5.该文本里，在哪个小时发布的数据最多:{0}'.format(m[0][0]))

#6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）












