import urllib.parse

print('此脚本默认未出行，如需填写相关信息，请前往网页签到')
name = input('输入姓名：')
sex = input('输入性别(男/女)：')
studentid = input('请输入学号：')
college_id = input('请输入学院代码，参照college_id.json（金融学院请输入404）：')
address = input('请输入家庭住址：')
contact = input('请输入个人联系电话：')
phone = input('请输入父母（家人）电话：')
province_id = input('请输入目前所在省份代码，参照province_id.json（山东省内请输入16）：')
city_id = input('请输入目前所在城市代码，参照city_id.json（济南市请输入170）：')
now_address = input('请目前所在输入详细地址：')
now_status = input('请输入目前状态，参照now_status.json（健康请输入1）：')
now_status_msg = input('请输入状态补充（可直接回车跳过）：')
print('为方便期间，其他信息均设置为默认值')


if sex == '男':
    sexcode = '1'
else:
    sexcode = '0'

f = {'name': name, 'sex': sexcode, 'study_id': studentid, 'college_id': college_id, 'address':address, 'contact':contact, 'phone':phone, 'province_id':province_id,'city_id':city_id,'now_address':now_address,'now_status':now_status,'now_status_msg':now_status_msg}

custom = urllib.parse.urlencode(f)
defualt = '&partition_time=&behavior=1&travel_address=&back_address=&travel_start=&travel_back=&travel_type=0&travel_number=&is_public=0&country_travel=0&travel_msg=&other_msg=&'
basicinfo = custom + defualt
with open('basicinfo.txt', 'w') as f:
    f.write(basicinfo)
print('basicinfo已保存至该文件下的basicinfo.txt中')