from random import choice
absurd_object = ["кот","чай","чайник","огурец","автобус"]
subjects = [{"words": ["кот ","чай ","чайник ","огурец ","автобус "],
									"type": "absurd" 
									},
									{"words": ["правительство "],
									"type": "neuter" 
									},
									{"words": ["эксперты ","депутаты ","ученые "],
									"type": "plural" 
									},
									{"words": ["полиция "],
									"type": "female" 
									}
								]
actions_mnch = ["придумали","сделали","изобрели","подписали","поставили на пост президента","отправили на луну","посадили в тюрьму"]
actions_credniy = ["придумало","сделало","изобрело","подписало","поставило на пост президента","отправило на луну","посадило в тюрьму"]
actions_woman = ["придумала","сделала","изобрела","подписала","поставила на пост президента","отправила на луну","посадила в тюрьму"]
actions_man = ["придумал","сделал","изобрел","подписал","поставил на пост президента","отправил на луну","посадил в тюрьму"]

def get_subject():
	category = choice(subjects)
	subject = choice(category["words"])
	return { "word": subject,
				"type": category["type"]}

def get_action(subject):
	if subject["type"] == "absurd":
		action = choice(actions_man)
	elif subject["type"] == "female":
		action = choice(actions_woman)
	elif subject["type"] == "neuter":
		action = choice(actions_credniy)
	elif subject["type"] == "plural":
		action = choice(actions_mnch)
	return action
def get_object():
	object=choice(absurd_object)
	return object

def get_twist(context):
	obj = context["object"]
	action = context["action"]
	twist_types = ["результат","отказ","переворот","причина","масштаб","признано"]
	twist_type = choice(twist_types)
	result_types = [f", в результате {obj} сбежал",f", после этого {obj} заговорил"]
	otkas_types = [f", но {obj} отказался это коментировать", ", но ООН признали это неправильным", f", но {obj} взбунтовался"]
	reverse_types = [f", из-за этого {obj} начал принимать решения сам", f", после этого {obj} начал управлять сам", f", {obj} потребовал объяснить происходящее"]
	reason_types= [f", потому что {obj} так решил", f", потому что {obj} попросил", f", потому что {obj}у это показалось логичным"] 
	mashtab_types =[", в эту ситуацию оказался втянут весь интернет", f", {obj} передал, что это распространится на весь мир",", этот инцедент навсегда зекрепится в учебниках истории по всему миру"]
	prisnano_types =[f", из-за этого инцедента {obj} признали нелегальным", f", принят закон о запрете {obj}", f", эксперты из Лондона подтвердили {obj} теперь личность"]
	if twist_type == "результат":
		twist = choice(result_types)
	elif twist_type == "отказ":
		twist = choice(otkas_types)
	elif twist_type == "переворот":
		twist = choice(reverse_types)	
	elif twist_type == "причина":
		twist = choice(reason_types)
	elif twist_type == "масштаб":
		twist = choice(mashtab_types)
	elif twist_type == "признано":
		twist = choice(prisnano_types)
	return twist
def build_news():
	subject=get_subject()
	sub = subject["word"]
	act=get_action(subject)
	obj=get_object()
	context = {
				"subject": subject,
				"object":obj,
				"action": act
	}
	twist=get_twist(context)
	if obj == "кот":
		obj = "кота"
	news = f"{sub}{act} {obj}{twist}"
	return news
if __name__ == "__main__":
	build_news()
