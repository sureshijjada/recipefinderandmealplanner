from flask import Flask, render_template, request

app = Flask(__name__)

# Sample list of recipes with titles, ingredients, and descriptions
recipes = [
    {"id": 1, "title": "Tamarind", "ingredients": ["rice", "ground nuts", "tamarind", "green chillies", "cashew", "oil", "curry leaves","turmeric powder","mustard seeds","cumin seeds","urad dal","chana dal","asafoetida"], "description": "Tamarind rice, or Pulihora, is a tangy and spicy South Indian dish made by mixing cooked rice with tamarind paste, spices, and seasonings.", "image": "https://tse1.mm.bing.net/th?id=OIP.TguPoHSltm5sjUSo2BWMUAHaE0&pid=Api&P=0&h=180"},
    {"id": 2, "title": "Chicken Salad", "ingredients": ["chicken", "lettuce", "tomato", "cucumber", "olive oil", "lemon", "feta cheese"], "description": "A light and healthy salad with grilled chicken breast, fresh lettuce, cucumber, and tomato. Tossed in olive oil and lemon dressing, topped with crumbled feta cheese.", "image": "https://img.freepik.com/premium-photo/chicken-salad-hd-8k-wallpaper-stock-photographic-image_890746-104026.jpg"},
    {"id": 3, "title": "Vegetable Stir Fry", "ingredients": ["bell peppers", "carrot", "broccoli", "soy sauce", "ginger", "garlic"], "description": "A colorful mix of stir-fried vegetables, including bell peppers, carrots, and broccoli, seasoned with soy sauce, garlic, and ginger.", "image": "https://tse3.mm.bing.net/th?id=OIP.aHBwle0DxRcK5q3ZmK5zzwHaEJ&pid=Api&P=0&h=180"},
    {"id": 4, "title": "Egg masala", "ingredients": ["boiled eggs", "curry leaves", "onion", "tomato", "garlic past", "green chillies","oil","garam masala","chilli powder","turmeric powder","salt","water","coriander leaves"], "description": "Egg Masala is a flavorful and hearty Indian dish made with hard-boiled eggs cooked in a rich, spiced tomato-based gravy.", "image":"https://tse4.mm.bing.net/th?id=OIP.SiqeK3DYr-CVIJOe70BCWwHaLH&pid=Api&P=0&h=180"},
    {"id": 5, "title": "Mutton dum biryani", "ingredients": ["rice", "oil", "curd", "mutton", "chilli powder", "turmeric powder","salt","biryani masalas","mutton masala"], "description":"Mutton Dum Biryani is a fragrant, flavorful rice dish made with tender mutton, aromatic spices, and basmati rice, cooked together on low heat to perfection.", "image": "https://tse4.mm.bing.net/th?id=OIP.qTzBIim8Nyc4KQofktP11AHaE8&pid=Api&P=0&h=180"}, 
    {"id": 6, "title": "Toor dal tomato", "ingredients": ["toor dal", "cumin seed", "mustard seeds", "urdal dal", "tomatos", "curry leaves","red chillies","salt","turmeric powder"], "description": "Toor dal tomato curry is a flavorful, tangy dish made with split pigeon peas, tomatoes, and aromatic spices, often served with rice or flatbreads.", "image": "https://tse3.mm.bing.net/th?id=OIP.JtZDcJ3LojkA9GMcjQ3l-wHaEK&pid=Api&P=0&h=180"},
    {"id": 7, "title": "crab curry", "ingredients": ["crabs", "onions", "tomatos", "ginger-garlic paste","green chillies", "curry leaves", "tamarind","chilli powder","salt","masalas"],"description": "Crab curry is a flavorful, spicy dish made with tender crab pieces simmered in a rich, aromatic gravy of spices, coconut milk, and fresh herbs.", "image": "https://tse3.mm.bing.net/th?id=OIP.M-sOi0cEwlz1gggnn5e0jQHaFj&pid=Api&P=0&h=180"},
    {"id": 8, "title": "garlic butter prawn", "ingredients": ["prawns", "garlic cloves", "butter", "lemon juice", "salt", "pepper","parsley"], "description":"Garlic Butter Prawns are succulent prawns cooked in a rich, aromatic garlic butter sauce with a hint of lemon, creating a deliciously savory dish.", "image": "https://tse3.mm.bing.net/th?id=OIP.EZNvDta2LyNGr48zJjH70gHaJQ&pid=Api&P=0&h=180"},
    {"id": 9, "title": "cumin rice", "ingredients": ["rice", "water", "onion", "garlic", "cloves", "cumin seeds", "cinnamon","salt","cilantro"], "description": "Cumin rice is a fragrant, simple dish made by cooking basmati rice with aromatic cumin seeds, a touch of ghee or oil, and optional spices, creating a flavorful and aromatic side dish.", "image": "https://tse1.mm.bing.net/th?id=OIP.ELTYHuwJWM3L7_7x1Wc8cwHaEO&pid=Api&P=0&h=180"},
    {"id": 10, "title": "paneer tikka masala", "ingredients": ["paneer", "yogurt", "ginger garlic paste", "onions", "red chilli powder", "turmeric powder","lemon juice","salt","butter","green chillies","ghee","kasurimethi"], "description": "Paneer Tikka Masala is a rich and flavorful dish featuring grilled or roasted paneer cubes in a creamy, spiced tomato-based gravy.", "image": "https://tse2.mm.bing.net/th?id=OIP.xJEmfCipx32hXBHQ_l60tAHaEs&pid=Api&P=0&h=180"},
    {"id": 11, "title": "stuffed brinjal curry", "ingredients": ["green chillies", "salt", "coriander leaves", "tomato", "cumin seeds", "garlic cloves", "tamarind extract","musted seeds"], "description": "Stuffed Brinjal Curry is a flavorful dish made with small eggplants filled with a spicy, tangy peanut-coconut stuffing, simmered in a rich onion-tomato gravy.", "image": "https://tse4.mm.bing.net/th?id=OIP.PLtXOZXWvybrheI0EcLQ0QHaE8&pid=Api&P=0&h=180"},
    {"id": 12, "title": "mushroom stir-fry", "ingredients": ["mushrooms", "garlic", "onions", "bell papper", "carrot","green beans","soya sauce","sesame oil","chilli flakes","salt"], "description": "Mushroom Stir-fry is a quick and flavorful dish made by sautéing mushrooms with garlic, vegetables, and soy sauce, seasoned with spices for a savory, healthy treat.", "image": "https://tse3.mm.bing.net/th?id=OIP.n2MrqvF1ZSBUyrAnkh_VqwHaFj&pid=Api&P=0&h=180"},
    {"id": 13, "title": "Sambar", "ingredients": ["dal", "oil", "garlic", "tamarind extract", "red chillies", "salt", "vegetables","water","curry leaves","onions","sambar powder","cumin seeds","musted seeds"], "description": "Sambar is a hearty South Indian lentil stew made with vegetables, tamarind, and a blend of spices.", "image": "https://tse3.mm.bing.net/th?id=OIP.O6LB8LHw88U9scAQGwrFfgHaE3&pid=Api&P=0&h=180"},
    {"id": 14, "title": "vegetable pulao", "ingredients": ["rice", "onion", "garlic", "mixed vegetables", "green chillies", "whole spices", "turmeric powder","coriander","garam masala","salt","mint leafs","cilantro","water"], "description": "Vegetable Pulao is a fragrant rice dish cooked with mixed vegetables, aromatic spices, and herbs, offering a flavorful, comforting meal.", "image": "https://tse3.mm.bing.net/th?id=OIP.MpINH8kdeFfA8o-eiyQbKQHaDt&pid=Api&P=0&h=180"},
    {"id": 15, "title": "fish fry", "ingredients": ["fish pieces","oil","sali", "onion", "corn flour", "cumin powder", "chili powder", "yogurt","curry leaves","ginger garlic paste","fish masala","turmeric powder"], "description": "Fish fry is a flavorful dish made by marinating fish in spices and frying it until crispy and golden brown.", "image": "https://tse1.mm.bing.net/th?id=OIP.9fnyp-AhaU1oonOPV2v_8AAAAA&pid=Api&P=0&h=180"},
    {"id": 16, "title": "potato kurma","ingredients":["potatos","onions","chillies","garam masala","ginger garlic paste","oil","salt","water","curry leaves","turmeric powder"],"description":"Potato Kurma is a flavorful South Indian curry made with potatoes and a rich, aromatic, spiced gravy. It's usually served with rice, paratha, or roti. Here's how to make it.", "image":"https://tse3.mm.bing.net/th?id=OIP._7NmpyrnV3WjKHArgEKq1QHaE8&pid=Api&P=0&h=180"},
    {"id": 17, "title": "chicken curry","ingredients":["chicken","onions","chillies","garam masala","ginger garlic paste","oil","salt","water","curry leaves","turmeric powder","chicken masala","corianderpowder","cashew"],"description":"Chicken curry is a rich and flavorful dish made with tender chicken cooked in a spiced gravy of onions, tomatoes, and aromatic spices. It’s often served with rice or naan for a comforting, hearty meal.", "image":"https://tse3.mm.bing.net/th?id=OIP.PnJkAkEoUZ5XdkxTMEGNDgHaE8&pid=Api&P=0&h=180"},
    {"id": 18, "title": "Spicy Macaroni","ingredients":["macaroni","onions","chillies","garam masala","ginger garlic paste","oil","salt","water","curry leaves","tomatos","pepper","ground meat","cheese","fresh herbs","lemon juice","cream"],"description":"A flavorful and zesty macaroni dish with a spicy kick from chili, peppers, and seasonings, often enriched with cheese or meat.", "image":"https://tse2.mm.bing.net/th?id=OIP.XMCUa9KJ3e5EAO9BnEncOwHaE8&pid=Api&P=0&h=180"},
    {"id": 19, "title": "Mixed Non-Veg Fried Rice","ingredients":["cooked rice","onions","chillies","garam masala","ginger garlic paste","oil","salt","green beens","curry leafs","carrots","pepper","boneless chicken breast","chilli flakes","shrimp","eggs","frozen peas","Soy sauce","prawns"],"description":"Mixed Non-Veg Fried Rice is a savory, stir-fried dish packed with chicken, shrimp, eggs, vegetables, and aromatic seasonings, creating a delicious and hearty meal.", "image":"https://tse3.mm.bing.net/th?id=OIP.hUXb-900KtnkLGZkUkcUQwHaEK&pid=Api&P=0&h=180"},
    {"id": 20, "title": "shark fish curry","ingredients":["smashed shark fish","onions","chillies","tomatos","ginger garlic paste","oil","salt","cumin seeds","curry leaves","coriander","musted seeds","water"],"description":"Shark Fish Curry is a spicy, tangy dish made with shark fish simmered in a flavorful curry of tamarind, coconut milk, and a blend of aromatic spices.", "image":"https://tse1.mm.bing.net/th?id=OIP.q0vPIzYEcJ6rtL1duUYK8QHaEK&pid=Api&P=0&h=180"}




]

# Placeholder for the user's meal plan (could be expanded to a database)
# meal_plan = []

# Store meals for each day of the week
meal_plan = {
    'monday': [],
    'tuesday': [],
    'wednesday': [],
    'thursday': [],
    'friday': [],
    'saturday': [],
    'sunday': []
}

@app.route("/", methods=["GET", "POST"])
def index():
    search_query = request.form.get("search_query", "")
    matching_recipes = []

    if search_query:
        # Convert the search query to lowercase for case-insensitive matching
        search_query_lower = search_query.lower()
        
        # Search through recipes based on title or ingredients (case-insensitive)
        matching_recipes = [recipe for recipe in recipes if search_query_lower in recipe["title"].lower() or 
                            any(search_query_lower in ingredient.lower() for ingredient in recipe["ingredients"])]
    
    return render_template("index.html", recipes=matching_recipes, search_query=search_query)

@app.route("/recipe/<int:recipe_id>")
def recipe_detail(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if recipe is None:
        return "Recipe not found", 404
    return render_template("recipe_detail.html", recipe=recipe)

@app.route('/meal-planner', methods=['GET', 'POST'])
def meal_planner():
    if request.method == 'POST':
        meal = request.form['meal']
        day = request.form['day']
        if meal and day:
            meal_plan[day].append(meal)  # Add the meal to the corresponding day
    return render_template('meal_planner.html', meal_plan=meal_plan)

if __name__ == "__main__":
    app.run(debug=True)
