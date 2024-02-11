from django.shortcuts import render, redirect
import pyrebase

# config = {
#     "apiKey": "AIzaSyDbAn-fvmY7MDxmbwQNrJkKn175WWxrh30",
#     "authDomain": "carbon-guard-52ed1.firebaseapp.com",
#     "databaseURL": "https://carbon-guard-52ed1-default-rtdb.firebaseio.com/",
#     "projectId": "carbon-guard-52ed1",
#     "storageBucket": "carbon-guard-52ed1.appspot.com",
#     "messagingSenderId": "565640798929",
#     "appId": "1:565640798929:web:db11d89014c922f191dbf0",
#     "measurementId": "G-4GGDBDWZDM"
# }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# database = firebase.database()

# def home(request):
#     return render(request, 'home.html', {})

# def login(request):
#     return render(request, 'login.html', {})

# def signup(request):
#     return render(request, 'signup.html', {})

# def calculator(request):
#     return render(request, 'calculator.html', {})
def calculate_carbon_footprint(request):
    if request.method == 'POST':
        # Extract data from the form
        petrol = float(request.POST.get('petrol', 0))
        diesel = float(request.POST.get('diesel', 0))
        electricity = float(request.POST.get('electricity', 0))
        natural_gas = float(request.POST.get('natural_gas', 0))
        cng = float(request.POST.get('cng', 0))
        cng_scm = float(request.POST.get('cng_scm', 0))
        flight = float(request.POST.get('flight', 0))
        lpg = float(request.POST.get('lpg', 0))
        coal = float(request.POST.get('coal', 0))

        # Conversion factors for each activity (carbon footprint per unit)
        conversion_factors = {
            'petrol': 2.31,  # kg CO2 per litre
            'diesel': 2.68,  # kg CO2 per litre
            'electricity': 0.537,  # kg CO2 per kWh
            'natural_gas': 0.184,  # kg CO2 per kWh
            'cng': 2.15,  # kg CO2 per kg
            'flight': 0.214,  # kg CO2 per passenger-km
            'lpg': 1.51,  # kg CO2 per litre
            'coal': 2.93  # kg CO2 per kg
        }

        # Additional factors
        cng_factor = 1.0  # Example: If you have a specific factor for CNG, define it here

        # Calculate total carbon footprint
        total_carbon_footprint = (petrol * conversion_factors['petrol']) + \
                                 (diesel * conversion_factors['diesel']) + \
                                 (electricity * conversion_factors['electricity']) + \
                                 (natural_gas * conversion_factors['natural_gas']) + \
                                 (cng * conversion_factors['cng']) + \
                                 (cng_scm * cng_factor) + \
                                 (flight * conversion_factors['flight']) + \
                                 (lpg * conversion_factors['lpg']) + \
                                 (coal * conversion_factors['coal'])

        return render(request, 'carbon_footprint_result.html', {'total_carbon_footprint': total_carbon_footprint})

    # Handle GET request or invalid form submission
    return render(request, 'calculator.html', {})

# def about(request):
#     return render(request, 'about.html', {})

# def postsign(request):
#     email = request.POST.get('email')
#     passw = request.POST.get('password')

#     try:
#         user = auth.sign_in_with_email_and_password(email, passw)
#         request.session['firebase_uid'] = user['localId']  # Store Firebase UID in session
#         return redirect('welcome', firebase_uid=user['localId'])  # Redirect to welcome page with UID
#     except:
#         message = "Invalid Credentials"
#         return render(request, "login.html", {"messg": message})

# def presign(request):
#     email = request.POST.get('email')
#     passw = request.POST.get('password')

#     user = auth.create_user_with_email_and_password(email, passw)
#     return render(request, 'login.html', {'e': email})

# def welcome(request, firebase_uid):
#     if firebase_uid:
#         # Retrieve user data from Firebase Realtime Database using the Firebase UID
#         user_data = database.child('users').child(firebase_uid).get().val()
       
#         return render(request, 'welcome.html', {'user_data': user_data})
#     else:
#         # Handle case when user is not logged in or UID is not provided
#         return redirect('login')

# if __name__ == "__main__":
#     ob = calculate_carbon_footprint():
        
    