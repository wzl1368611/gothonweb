a='hello world'
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
		pass   
lexicon={'direct':['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],'verb':['go', 'stop', 'kill', 'eat','shoot','dodge','tell','throw','place'],'prep':['the', 'in', 'of', 'from', 'at','a','the','slowly'],'noun': ['door', 'bear', 'princess', 'cabinet','bomb','joke','!'],'num':[0,1,2,3,4,5,6,7,8,9]}
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(ss):
	
	word=ss.split()

	s=[]
	for i in range(len(word)):
		a=word[i]
		if a in lexicon['direct']:
			s.append('direct')
			s.append(word[i])
		elif a in lexicon['verb']:
			s.append('verb')
			s.append(a)
		elif a in lexicon['prep']:
			s.append('prep')
			s.append(a)
		elif a in lexicon['noun']:
			s.append('noun')
			s.append(a)
		elif convert_number(a)!=None:
			s.append('num')
			s.append(int(a))
		else :
			s.append('error')
			s.append(a)
	print('拆分的单词类型为：',s)
	sentence=[]
	if len(s)/2==1:
		first_word=(s[0],s[1])	
		sentence = [ first_word ]
	if len(s)/2==2:
		first_word=(s[0],s[1])
		second_word=(s[2],s[3])
		sentence = [ first_word , second_word]
	if len(s)/2==3:
		first_word=(s[0],s[1])
		second_word=(s[2],s[3])
		third_word=(s[4],s[5])
		sentence = [ first_word , second_word , third_word ]
	if len(s)/2>3:
		for i in range(int(len(s)/2)):
			j=i*2
			first_word=(s[j],s[j+1])
			sentence.append(first_word)

#first_word = ( 'verb ' , 'go ' )
#second_word = ( ' direction ' , ' north ' )
#third_word = ( ' direct ion ' , ' west ' )

	print(sentence,'+++++++++++++++++++++++')
	return sentence
'''
stuff=input('>')
print(stuff)
scan(stuff)
'''




