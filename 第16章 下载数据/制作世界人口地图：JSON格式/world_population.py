import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

# 将数据加载到列表中
filename = 'world_population.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2014年的人口数量

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2014':
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        # country_code = pop_dict['Country Code']
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            pass
cc_pops_1, cc_pops_2, cc_pops_3, = {}, {}, {}
for cc, pop in cc_populations.items():
    pop = int(float(pop))
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
# 自定义颜色
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)



wm.render_to_file('world_population.svg')