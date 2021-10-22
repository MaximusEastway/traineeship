from flask import Flask
app = Flask(__name__)

@app.route("/")
def hallo_wereld():  
	return '''
   <html><body>
     <h1>Hallo wereld</h1>
     <p>Dit is een webpagina waar we nog heel veel plezier van gaan hebben
     in het vervolg van deze training!</p>
     </body>
   </html>
  '''