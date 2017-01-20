import pygal

wm = pygal.Worldmap()
wm.title = '北美国家人口'
wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})
wm.render_to_file('北美人口.svg')