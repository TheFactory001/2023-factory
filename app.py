from flask import Flask,render_template,request
import requests, datetime as dt
app = Flask(__name__)
  
@app.route('/')
def home():
    return render_template("shoppr_form.html")

@app.route('/form-result',methods=["POST"])
def get_form():
    if request.method=="POST":
        print(request.form) 
        dictionary=request.form.to_dict()
        print(dictionary)
        email=dictionary['email']
        first_name=dictionary['first_name']
        last_name=dictionary['last_name']
        print("form::::::::::::::::::::",first_name,email,last_name)
    return render_template("success.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login',methods=["POST"])
def get_login_form():
    if request.method=="POST":
        print(request.form)
        dictionary=request.form.to_dict()
        print(dictionary)
        phone=dictionary['phone']
        password=dictionary['password']
        country=dictionary['country']
        range=dictionary['range']
        membership=dictionary['membership']
        print("login:::::::::::::::::::::", phone,password,country,range,membership)
        return render_template("login_successful.html")
    
@app.route('/get-api',methods=["GET","POST"])
def get_api():
    if request.method=="GET":
        print(request.args.get("get"))
    return render_template("get.html")

@app.route('/get-twitter', methods=["GET"])
def get_twitter():
    if request.method=="GET":
        print(request.args.get("get"))
    return render_template("twitter.html")

@app.route('/get-netflix', methods=["GET"])
def get_netflix():
    if request.method=="GET":
        print(request.args.get("get"))
    return render_template("netflix.html")

@app.route('/amazon-search', methods=["GET"])
def amazon_search():
    if request.method=="GET":
        print(request.args.get("get"))
        return render_template("amazon.html")
    
def get_url(city):
    base_url="https://api.openweathermap.org/data/2.5/weather?appid=b6afc5e65b72cb94fdb747d02b449eb1&q="
    complete_url=base_url+city
    return complete_url

def get_sunrise_readable_time():
    sunrise = dt.datetime.fromtimestamp()
    return sunrise

print(get_sunrise_readable_time())

    
@app.route('/weather',methods=["GET","POST"])
def weather():
    if request.method=="POST":
        user_city=request.form["city"]
        city_url=get_url(user_city)
        response= requests.get(city_url)
        city_data=response.json()
        print(city_data)
        country=city_data["sys"]["country"]
        sunrise=city_data ["sys"]["sunrise"]
        temp=city_data["main"]["temp"]
        lon=city_data["coord"]["lon"]
        lat=city_data["coord"]["lat"]
        pressure=city_data["main"]["pressure"]
        humidity=city_data["main"]["humidity"]
        sunset=city_data["sys"]["sunset"]
        name=city_data["name"]
        timezone= dt.datetime.fromtimestamp(city_data["timezone"])
        description=city_data["weather"][0]["description"]
        return render_template("weather.html",city_data=city_data,country=country,sunrise=sunrise,
                               temp=temp,lon=lon,lat=lat,pressure=pressure,humidity=humidity,sunset=sunset,
                               name=name,timezone=timezone,description=description)
        
    return render_template("weather.html")

weather="https://api.openweathermap.org/data/2.5/weather?appid=b6afc5e65b72cb94fdb747d02b449eb1&q="


# @app.route('/dict',methods=["GET","POST"])
# def dict():
#     if request.method=="POST":
#         print(request.args.get("get"))
#     return   render_template("dict.html")








  

    
        
    
    # form_dictionary={}
    #     my_form_data=request.form
    #     form_dictionary['first_name']=my_form_data["first_name"]
    #     form_dictionary['email']=my_form_data["email"]
    #     form_dictionary["last_name"]=my_form_data["last_name"]
    #     form_dictionary["password"]=my_form_data["password"]

    #     print(request.form) 
    #     dictionary=request.form.to_dict()
    #     print(dictionary)
    #     email=dictionary['email']
    #     first_name=dictionary['first_name']
    #     last_name=dictionary['last_name']
    #     print("form::::::::::::::::::::",first_name,email,last_name)