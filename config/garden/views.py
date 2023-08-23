from django.shortcuts import render, HttpResponse
from .models import Garden_DB

# Create your views here.

def home(request):
    return render(request, "home.html")

def list(request):
    vegetables = Garden_DB.objects.order_by("vegetable").all()
    context = {'vegetables': vegetables}
    return render(request, "list.html", context)

def get_vegetable(request, get_vegetable):
    
    # Uppercase the vegetable entry from the URL call to match case in DB
    vegetable = get_vegetable.title()

    # Query the database to return the database row data based on vegetable
    transform_vegetable = Garden_DB.objects.filter(vegetable = vegetable).values()
    veg_dict = transform_vegetable[0]
    print(veg_dict)
    print(veg_dict['sow_type'])

    
    # Grab the appropriate column data for the row called
    vegetable = transform_vegetable.vegetable
    sow_type = transform_vegetable.sow_type
    harvest_days = transform_vegetable.harvest_days
    plant_spacing = transform_vegetable.plant_spacing
    seed_depth = transform_vegetable.seed_depth
    # If direct sow type, we'll feed the sow window dates
    if sow_type == "Direct":
        window_start = transform_vegetable.sow_window_start
        window_end = transform_vegetable.sow_window_end
    # If transplant type, we'll feed the transplant window dates
    else:
        window_start = transform_vegetable.transplant_window_start
        window_end = transform_vegetable.transplant_window_end
    harvest_window_start = transform_vegetable.harvest_window_start
    harvest_window_end = transform_vegetable.harvest_window_end

    context = {'vegetable': vegetable,
        'sow_type': sow_type,
        'harvest_days': harvest_days,
        'plant_spacing': plant_spacing,
        'seed_depth': seed_depth,
        'window_start': window_start,
        'window_end': window_end,
        'harvest_window_start': harvest_window_start,
        'harvest_window_end': harvest_window_end}

    return render(request, "vegetable.html", context
    )

def forecast(request):
    return render(request, "forecast.html")

# def todays_tasks(request):
#     return render(request, "todays-tasks")