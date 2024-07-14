# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
oxygenFloat = 25.22
pressure1 = 0.25

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/<meter>/<value>')
# ‘/’ URL is bound with valuePass() function.
def valuePass(meter, value):
   global oxygenFloat
   global pressure1
   if type(meter) != str:
        meter = str(meter)
   if type(value) != str:
        value = str(value)
   if meter == 'oxygen':
       if value != 'read':
            oxygenFloat = float(value)
       ##return 'Oxygen value set to: %s' % str(oxygenFloat)
   if meter == 'pressure1':
       if value != 'read':
           pressure1 = float(value)
       ##return 'Pressure1 value set to: %s' % str(pressure1)    
   ##return 'Non valid meter: %s' % meter
   return dash()        

@app.route('/dash')

def dash():
    global oxygenFloat
    global pressure1
    returning = 'Oxygen meter: %s' % str(oxygenFloat)
    returning += ' Pressure1: %s' % str(pressure1)
    return returning

@app.route('/highPressure')

def highPressure():
    global oxygenFloat
    global pressure1
    pressure1 = 125.02
    return dash()

@app.route('/lowOxygen')

def lowOxygen():
    global oxygenFloat
    global pressure1
    oxygenFloat = 85.3
    return dash()

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
