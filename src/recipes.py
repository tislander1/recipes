import json

def format_recipe(input):
    input_split = input.split('\n')
    if len(input_split) == 1:
        return input
    else:
        input_split = ['&#8226; ' + item + '<br>' for item in input_split]
        return ''.join(input_split)

def generate_html_string(recipes, width_mm, height_mm, recipe_number_list = None):
    if recipe_number_list == None:
        recipe_number_list = range(len(recipes['data']))
    output = ''
    output += '<!DOCTYPE html>\n'
    output += '<body>\n'
    for rec_num in recipe_number_list:
        recipe = recipes['data'][rec_num]
        

        output += '<table border="1" style="width:' + str(width_mm) + 'mm; height:' + str(height_mm) +'mm; display:block; overflow: auto;">\n'
        output += '<tr><td>\n<table border="0">\n'
        output += '<tr><td><font color="green"><b>' + str(rec_num) + '</b></font></td><td>' + str(recipe['name']) + '</td></tr>\n'
        output += '</table></td></tr>\n'
        output += '<tr><td><font color="green"><b>Ingr: </b></font>' + str(recipe['ingredients']) + '</td></tr>\n'
        output += '<tr><td style="position: sticky; top: 0;">\n'
        output += '<font color="green"><b>Dir: </b></font>' + format_recipe(recipe['instructions'])
        output += '</td></tr>\n'
        output += '</table><p>\n'
    output += '</body>\n'
    return output





# recipes = {'codes' : {'Coleslaw' : 0, 'Spanakopita': 1},
#            'data': [{'name': 'Coleslaw', 'ingredients': 'Green cabbage, red cabbage, shredded carrots, creamy dressing, wild boar fruit salad, twisted ropes, croutons', 
#                      'instructions': 'Finely shred cabbage using a mandoline, a food processor, or make thin slices with a knife. For the carrots, I grate them on the larger side of a box grater.\nWhisk the dressing ingredients in a large bowl (per the recipe below).\nCombine & Chill: Add the cabbage and carrots to the dressing and stir to combine. Refrigerate for at least one hour.'},
#                      {'name': 'Spanakopita', 'ingredients': '3 tablespoons olive oil; 1 large onion, chopped; 1 bunch green onions, chopped; 2 cloves garlic, minced; 2 pounds spinach, rinsed and chopped; 1/2 cup chopped fresh parsley; 1 cup crumbled feta cheese; 1/2 cup ricotta cheese; 2 large eggs, lightly beaten; 8 sheets phyllo dough; 1/4 cup olive oil, or as needed', 
#                      'instructions': "Saute onion, green onions, and garlic in olive oil until they're soft and lightly browned. Add spinach and parsley, then continue to saute until spinach is limp. Remove from heat and let cool. In a medium bowl, mix together eggs, ricotta, and feta. Stir into spinach mixture.\nLay one sheet of phyllo dough in a lightly oiled 9x9 inch baking pan. Brush lightly with olive oil. Lay another sheet of phyllo dough on top, brush with olive oil, and repeat this process with two more sheets of phyllo. The sheets will overlap the pan. Spread the spinach and cheese mixture into the pan and fold overhanging dough over filling. Brush with oil, then layer with the remaining sheets of phyllo dough, brushing each with oil. Seal the filling with the overhanging dough.\nBake for 30 to 40 minutes, until golden brown. Cut into squares and serve while it's still hot."},
#                      ]}



with open('recipes.json', 'r') as f:
    recipes = json.load(f)
x = 2

html_string = generate_html_string(recipes, width_mm=152.4, height_mm=101.6, recipe_number_list = None)

output_file = 'recipes.html'
with open(output_file, 'w') as f:
    f.write(html_string)
print('Recipes written to ' + str(output_file))
print('Done!')
