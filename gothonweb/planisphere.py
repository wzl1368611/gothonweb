from textwrap import dedent
import random 

class Room(object):

	def __init__(self, name, description): #设置房间的名称 和描述
		self.name = name
		self.description = description
		self.paths = {}    #为字典类型，房间名 ： 房间对象

	def go(self, direction): #进入任意下一个房间，获取这个房间对象
		return self.paths.get(direction, None)
	def add_paths(self, paths):# 设置房间的路径 
		self.paths.update(paths)
	def enter(self):
		pass       #完成房间内的挑战 有惊喜 闯关成功 恭喜
# 闯关房间 挑战  challenge ready go 百事百科 十万个为什么
# 答题选择 建立家庭 维护和谐 挑选女朋友 奖励 金钱 创立基业
# 建造房屋 领取金币 认领宠物 取得美女芳心 英雄救美 见义勇为
# 购置豪宅 辛勤工作 学会职业 制造产品 保护家人 生儿育女 赶走恶犬
# 打跑强盗 欣赏风景 好好的睡一觉 辉煌人生 失败的话 工作 挣钱 
# 天仙美女 10选一 一个充满金钱的房间 大闯关（）
des='''power is knowledge!
	in this room ,you will answer any of five problems,if you are right ,you 		will go into next room,or again once!'''
#challenge=Room(knowledge,des)
des02='''in this room ,you will meet some beauty,you have chance to marry one of them,maybe you have a best beautiful wife,Everything depends on your luck!
'''
#beauty=Room('beauty',des02)
#path1={'north':beauty}
#challenge.add_paths(path1)
#challenge.enter()
class Beauty(Room):
	def __init__(self):
		self.name='knowledge'
		self.description='知识问答，答对了有奖励，答错了有惩罚，请在规定时间内作答，超过时间判零'
		self.paths={}
	def enter(self):
		print(dedent('''
					欢迎来到知识殿堂！！！'''))
		n1='1冬瓜、黄瓜、西瓜、南瓜都能吃，什么瓜不能吃？'
		n2='2 盆里有6只馒头，6个小朋友每人分到1只，但盆里还留着1只，为什么？'
		n3='3 你能以最快速度，把冰变成水吗？'
		p1='傻瓜'
		p2='最后一个小朋友把盆子一起拿走了'
		p3='把“冰”字去掉两点，就成了“水”'
		score=0
		for i in range(3):
			if i==0:
				print('请看题：'+n1)
				a=input('请输入你的答案：')
				if a==p1:
					score+=1
					print('答案正确，加一分',score)	
				else:
					print('很抱歉，您答错了，答案是'+p1)
			if i==1:
				print('请看提：'+n2)
				a=input('请输入你的答案：')
				if a==p2:
					score+=1
					print('答案正确，加一分',score)
				else:
					print('很抱歉，您答错了，答案是'+p2)
			if i==2:
				print('请看题：'+n3)
				a=input('请输入你的答案：')
				if a==p3:
					score+=1
					print('答案正确加一分',score)
				else:
					print('很抱歉，您答错了，答案是'+p3)
		print('恭喜您获得的总分是：'+str(score)+'分')
		if score==3:
			print('三题答对，获得金币总额10000，提前晋级下一轮！美滋滋')
		if score==2:
			print('二题答对，获得金币总额1000，进入闯关2！有点伤')
			return 'north'
		if score==1:
			print('一题答对，获得金币总额10000，进入闯关1！运气有点不好哦')
			return 'south'
class Gold():
	def __init__(self):
		self.name='gold'
		self.description='金币房间'
		self.paths={}
	def enter(self):
		print('你有1次机会抽取最高奖励，一等奖：10000金币，二等奖：1000金币，三等奖：100金币')
		a=random.randint(1,10)
		b=random.choice(['一等奖','二等奖','三等奖'])
		print('抽奖开始','随机显示的数为',a)
		if a<4:
			print('恭喜获奖了')
			if a==1:
				print('喜提一等奖')
				return 'beauty'
			elif a==2:
				print('喜提二等奖一枚')
				return 'farm'
			else :
				print('喜提三等奖一枚')
				return 'job'
		else :
			print('很遗憾，未获奖，欢迎下次再来，再接再厉')
			return 'again'
			

a=Beauty()
b=Gold()
print(a.name,a.description)
print(b.name,b.description)
res=a.enter()
print(res)
if res=='south':
	fin=b.enter()
	print(fin)


		





		
			
		

	
