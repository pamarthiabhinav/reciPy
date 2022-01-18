from flask import Flask, render_template, request, redirect
from edamam import recipe_search

# create an instance of the Flask class
# name is the place holder for current module, here is app.py
app = Flask(__name__)


# use the route decorator to tell Flask what URL should trigger our function.
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recipe', methods=['POST', 'GET'])
def show_recipe():
    if request.method == 'POST':
        data = request.form
        # print(data)
        ingrediant = data['ingrediant'] or None
        health = data['health'] or None
        preference = data['preference'] or None
        # print(ingrediant, health, preference)
        if ingrediant and health and preference:
            hits = recipe_search(ingrediant, health, preference)
            # set second argument to pass the data
            return render_template('recipe.html', hits=hits)
    return redirect('/')


@app.route('/about')
def about():
    return render_template('about.html')


# it checks if a module is being imported or not
if __name__ == '__main__':
    # set debug=True so it's auto updated and we don't have to restart the server every time
    app.run(debug=True)
