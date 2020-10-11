from nose.tools import *
import sys
sys.path.append('gothonweb')
from planisphere import Room
#from ex47.game02 import *
def setup():
	print('开始')
def teardown():
	print('拆除')
def test_basic():
	print("正在运行")
def test_room():
	gold = Room("GoldRoom",
			"""This room has gold in it you can grab. There's a
			door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	center.add_paths({'north': north, 'south':south})
	assert_equal(center.go('north').name, north.name)
	assert_equal(center.go('north').description,north.description)
	assert_equal(center.go('south'), south)
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
def test_map02():
#	a_map = Map('central_corridor')
#	assert_equal(a_map.start_scene, "central_corridor")
#	assert_equal(a_map.next_scene('the_bridge'),TheBridge())
#	death=Death()
	sent='hello world'
	assert_equal(len(sent),11)
	assert_equal(sent[0],'h')
	assert_equal(ord('A'),65)
def test_hello():
	sent='你好 世界'
	a=sent.split(' ')
	a0='你好'
	a1='世界'
	assert_equal(sent.split(' ')[0],a0)
	assert_equal(sent.split(' ')[1],a1)

