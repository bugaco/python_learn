import pygal

wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('Central America', ['ar', 'bo', 'br', 'cl', 'cu', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've',])

wm.render_to_file('americas.svg')