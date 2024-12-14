from django.shortcuts import render
from django.shortcuts import render
from .ml_model import PostQualityPredictor

def predict_post_quality(request):
    prediction = None
    if request.method == 'POST':
        try:
            reputation = float(request.POST.get('reputation'))
            interaction = float(request.POST.get('interaction'))
            
            predictor = PostQualityPredictor()
            prediction = predictor.predict(reputation, interaction)
        except (ValueError, TypeError) as e:
            prediction = "Invalid input"
            #print the error
            print(e)

    
    return render(request, 'predict.html', {'prediction': prediction})

# Create your views here.
