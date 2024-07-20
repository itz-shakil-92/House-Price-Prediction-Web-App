from django.shortcuts import render
import numpy as np
import joblib

# Load model
model = joblib.load('scripts/health_model.pkl')

def home(request):
    return render(request, "home.html")

def predict(request):
    if request.method == 'POST':
        var1 = float(request.POST['n1'])
        var2 = float(request.POST['n2'])
        var3 = float(request.POST['n3'])
        var4 = float(request.POST['n4'])
        var5 = float(request.POST['n5'])

        prediction = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1))
        prediction = round(prediction[0])
        price = "The predicted price of the house is: $" + str(prediction)
        return render(request, "predict.html", {'result_for_current_query': price})

    return render(request, "predict.html")
