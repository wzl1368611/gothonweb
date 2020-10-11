import sys
#sys.path.append('ex48/')
from lexicon import scan
class ParserError(Exception):
	def __init__(self,ss):
		self.errorinfo=ss
	def __str__(self):
		return self.errorinfo
class Sentence(object):
	def __init__(self,subject,verb,obj):
		self.subject=subject[1]
		self.verb=verb[1]
		self.obj=obj[1]
def peek(word_list):
	if word_list:
		word=word_list[0]
		return word[0]
	else:
		return None
def match(word_list,excepting):
	if word_list:
		word=word_list.pop(0)
		if word[0]==excepting:
			return word
		else:
			return None
	else:
		return None
def skip(word_list,word_type):
	while peek(word_list)==word_type:
		match(word_list,word_type)
'''def parse_verb(word_list):
	skip(word_list,'prep')
	next_word=peek(word_list)
	if next_word=='noun':
		return match(word_list,'noun')
	elif next_word=='direct':
		return match(word_list,'direct')
	else:
		raise ParserError('expectd a noun or direct next.')
'''
def parse_verb(word_list):
	skip(word_list, 'prep') 

	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		
		raise ParserError("Expected a verb next.")
		
def parse_subject(word_list):
	skip(word_list, 'prep')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("Expected a verb next.")
def parse_object(word_list):
	skip(word_list, 'prep')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direct':
		return match(word_list, 'direct')
	else:
			

		raise ParserError("Expected a noun or direction next.")
		
def  parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list) 

	return Sentence(subj, verb, obj)
#hh=[('verb', 'go'), ('prep', 'the'), ('verb', 'go')]
#ss=parse_sentence(hh)
#print(ss.subject,ss.verb,ss.obj)
'''x = parse_sentence([('noun', 'bear'), ('verb', 'eat'),('prep','the'),('noun','honey')])
print(x.subject,x.verb,x.obj)
aa=ParserError("Expected a noun or direction next.")
	
print(aa,'==============')
print(type(aa),'======================')
if str(aa)=="Expected a noun or direction next.":
	print('ok','是正确的')
else :
	print('不相等')
'''
# 测试输入转换代码是否成功
# chin=input('请输入内容')
# chan=scan(chin)
# result=parse_sentence(chan)
# print(result.subject,result.verb,result.obj)
def convert_word(words):
	chan=scan(words)
	result=parse_sentence(chan)
	hh=result.subject+' '+result.verb+' '+result.obj
	return hh

		
