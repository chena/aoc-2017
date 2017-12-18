paid_items = [
	# robin
	239.11, 132.5, 25.08, 15.11, 22.8, 17.25, 72.0, 
	# timmy
	10.0,
	# jack
	23.0, 81.0, 43.24, 31.18, 10.25, 49.47
]

people_paid = {
	'robin': sum(paid_items[:7]),
	'timmy': paid_items[7],
	'jack': sum(paid_items[8:]),
	'amy': 0,
	'alice': 0,
	'xiaohe': 0
}

split_count = [len(people_paid)] * len(paid_items)
split_count[1] = 5
split_count[10] = 5
split_count[12] = 2
divided_amounts = [paid_items[n] / split_count[n] for n in range(len(paid_items))]

people_exclude = {
	'robin': divided_amounts[12],
	'timmy': divided_amounts[12],
	'jack': divided_amounts[1],
	'amy': 0,
	'alice': divided_amounts[12],
	'xiaohe': sum([divided_amounts[10], divided_amounts[12]])
}

for person in people_paid:
	if (person in ['robin', 'jack']): continue
	need_to_pay = sum(divided_amounts) - (people_paid[person] + people_exclude[person])
	print('{} needs to pay robin {}'.format(person, str(need_to_pay)))

jack_owed = (people_paid['jack'] + people_exclude['jack']) - sum(divided_amounts)
print('robin needs to pay jack {}'.format(str(jack_owed)))
print(total + jack_owed)

