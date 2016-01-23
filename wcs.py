# DATA COLLECTION AND ANALYSIS

# imports and reading data

import scipy.misc

import numpy as np

import glob

txt = Table.read_table("foci­exp.txt")

def find_min_distance(col, c_set):

"""

Finds the minimum RGB 'distance' between the color passed in

and the color set given to the system.

"""

d = {}

for color in c_set:

dist = ((col[0]­color[0])**2 + (col[1]­color[1])**2 + (col[2]­color[2])**2)**0.5

d[dist] = color

return d[min(d)]

def munsell2rgb(munsell):

"""

Converts a chip value into an RGB value.

Input as a pair [letter, number]

>>> munsell2rgb([A, 0])

[239, 239, 239]

"""

munsell_path = 'munsell.png'

assert len(munsell) == 2

assert ord(munsell[0])>= 65 and ord(munsell[0])<= 74

assert munsell[1] <= 40

munsell_image = scipy.misc.imread(munsell_path)

return munsell_image[(ord(munsell[0]) ­ 64) ­ 1][munsell[1]]

def avg_rgb(ls):

"""

Returns the average color value by averaging R,

G and B values for colors passed in on a list.

"""

red_tot, grn_tot, blu_tot, count = 0, 0, 0, 0

for col in ls:

red_tot += col[0]

grn_tot += col[1]

blu_tot += col[2]

count += 1

if count==0:

return [0, 0, 0]

return [red_tot/count, grn_tot/count, blu_tot/count]

def to_chip(str):

"""

Converts a string chip value into a pair that

can be used in calculations later in the program.

"""

assert len(str) == 2 or len(str) == 3

return [str[0], int(str[1:])]

def analyze_image(foci, image_path):

"""

Takes in an image, spits out frequencies

of colors near foci in the list foci.

Note: this method was used to analyze the

full image (i.e. all pixels); this method

was abandoned when it was discovered how

much processing power it took to analyze a

full folder of images.

"""

image = scipy.misc.imread(image_path)

# get counts array

arr_dist = []

for i in range(len(image)):

for j in range(len(image[i])):

# make into dict of color, count

counts_dict = {}

for col in foci.keys():

counts_dict[col] = arr_dist.count(foci[col]) / (len(image) * len(image[0]))

return counts_dict

def analyze_image_sample(foci, image_path, n=500):

"""

Takes in an image, takes a random sample

of size n pixels and spits out proportional

frequencies of colors near foci on the list

foci. (appendix reference 2)

"""

image = scipy.misc.imread(image_path)

arr_dist = []

for i in range(n):

px = image[np.random.randint(0, len(image))][np.random.randint(0, len(image[0]))]

ch = find_min_distance(px, c_set=list(foci.values()))

arr_dist.append(ch)

counts_dict = {}

for col in foci.keys():

counts_dict[col] = arr_dist.count(foci[col]) / (n)

return counts_dict

def avg_of_dict_vals(ls):

"""

Takes in a list of dictionaries with like

keys; returns a dictionary with the same

keys that stores the average value of all

dictionaries for each of its keys.

"""

avg_d, count_d = {}, 0

for d in ls:

count_d += 1

for k in d.keys():

arr_dist.append(find_min_distance(image[i][j], c_set=list(foci.values())))

if not k in avg_d.keys():

avg_d[k] = d[k]

else:

avg_d[k] += d[k]

for k in avg_d.keys():

avg_d[k] = avg_d[k]/count_d

return avg_d

######################################

# setting up countries to analyze

langs_analyzed = Table()

langs_analyzed['Language'] = ['Abidji']

langs_analyzed['LID'] = [1]

langs_analyzed['Location'] = ['Ivory Coast']

langs_analyzed['# Terms'] = [9]

langs_analyzed.append(['Chacobo', 23, 'Bolivia', 5])

langs_analyzed.append(['Nafaanra', 77, 'Ghana', 4])

langs_analyzed.append(['Karaja', 53, 'Central Brazil', 3])

langs_analyzed.append(['Shipibo', 86, 'Peru', 12])

for i in range(langs_analyzed.num_rows): # prints are for formatting purposes

print('==================== ', langs_analyzed['Language'][i], ' ===================== (',

langs_analyzed['LID'][i], ')')

# get language data for specific language

lang_data = txt.where(txt['Lang'] == langs_analyzed['LID'][i])

# determine foci for language (appendix reference 1)

focus_colors_lang = {}

for f in set(lang_data['Term']):

focus_values = lang_data.where(lang_data['Term'] == f)['Chip']

munsell_rgb_values = [munsell2rgb(to_chip(x)) for x in focus_values]

focus_colors_lang[f] = (avg_rgb(munsell_rgb_values))

# show the foci and their color values

Table([focus_colors_lang.keys(), focus_colors_lang.values()],

# read in pictures and analyze them

prop_dicts = []

for directory in glob.glob('./Pictures/' + langs_analyzed['Location'][i] + '/*.png'):

prop_dicts.append(analyze_image_sample(focus_colors_lang, directory))

# make into a dictionary with total proportions for language

new_dict = avg_of_dict_vals(prop_dicts)

print()

# display table of proportions

Table([new_dict.keys(), new_dict.values()], ['term', 'freq']).sort('term').show()

dict_keys = new_dict.keys()

dict_values = [new_dict[x] for x in dict_keys]

lang_table = Table([dict_keys, dict_values], ['term', 'frequencies'])

lang_table.sort('term').barh('term')

print()

print()

['term', 'color']).sort('term').show()

/////////////////////////////////////////////////////////////////////////////////////////

# HYPOTHESIS TESTING

# imports and data reading

import numpy as np

from scipy import *

t = Table.read_table('term.txt')

t1 = t.where('Lang',1)

# making counts dictionary (appendix reference 3)

lst = {}

for i in t1.columns[3]:

if i not in lst.keys():

else:

# converting to proportions

sum1 = sum(list(lst.values()))

for i in lst.keys():

lst[i] = lst[i]/sum1

table = Table([lst.keys(),lst.values()],['color terms','frequencies'])

table.barh('color terms')

# specific data to each language

table1 =

Table([['F','FU','G','GB','LB','LE','LF','S','WK'],[0.06,0.1588,0.0216,0.0158,0.3496,0.0312,0.

077,0.27,0.016]],\

table = table.sort('color terms')

def tvd(col1,col2):

return 0.5*(sum(abs(col1­col2)))

def sampling(table,arg1):

# (appendix reference 5)

reps = 1000

tvds = []

for i in np.arange(reps):

lst[i] = 1

lst[i]+=1

['term','frequencies'])

sample= np.random.multinomial(1000, table['frequencies'])

table['multi_results'] = sample/1000

tvds.append(tvd(table['multi_results'], arg1['frequencies']))

p_value = np.count_nonzero(tvds >= observed_tvd)/len(tvds)

table2 = Table([tvds],['tvds'])

table2.hist(bins = 20)

return p_value

######################################

# actually doing analysis (appendix reference 4)

observed_tvd = tvd(table['frequencies'], table1['frequencies'])