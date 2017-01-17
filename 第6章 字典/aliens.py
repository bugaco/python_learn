aliens = []
for alien_num in range(30):
	new_alien = {'color':'green', 'speed': 'slow', 'point': 5}
	aliens.append(new_alien)
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yello'
		alien['speed'] = 'medium'
		alien['point'] = 10
	print(alien)