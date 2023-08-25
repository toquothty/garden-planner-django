from django.shortcuts import render, HttpResponse
from datetime import datetime, date
from .models import Garden_DB
from .core.weather import weather

# Create your views here.


def home(request):
    return render(request, "home.html")


def list(request):
    # Grabs all table data ordered by vegetable column
    vegetables = Garden_DB.objects.order_by("vegetable").all()
    context = {"vegetables": vegetables}
    return render(request, "list.html", context)


def get_vegetable(request, get_vegetable):
    # Uppercase the vegetable entry from the URL call to match case in DB
    vegetable = get_vegetable.title()

    # Query the database to return the database row data based on vegetable
    # Transform query set into dictionary for easier python parsing
    transform_vegetable = Garden_DB.objects.filter(vegetable=vegetable).values()
    veg_dict = transform_vegetable[0]

    # Grab the appropriate column data for the row called
    vegetable = veg_dict["vegetable"]
    sow_type = veg_dict["sow_type"]
    harvest_days = veg_dict["harvest_days"]
    plant_spacing = veg_dict["plant_spacing"]
    seed_depth = veg_dict["seed_depth"]
    # If direct sow type, we'll feed the sow window dates
    if sow_type == "Direct":
        window_start = veg_dict["sow_window_start"]
        window_end = veg_dict["sow_window_end"]
    # If transplant type, we'll feed the transplant window dates
    else:
        window_start = veg_dict["transplant_window_start"]
        window_end = veg_dict["transplant_window_end"]
    harvest_window_start = veg_dict["harvest_window_start"]
    harvest_window_end = veg_dict["harvest_window_end"]

    context = {
        "vegetable": vegetable,
        "sow_type": sow_type,
        "harvest_days": harvest_days,
        "plant_spacing": plant_spacing,
        "seed_depth": seed_depth,
        "window_start": window_start,
        "window_end": window_end,
        "harvest_window_start": harvest_window_start,
        "harvest_window_end": harvest_window_end,
    }

    return render(request, "vegetable.html", context)


def forecast(request):
    # Utilize weather.py to grab the forecast for the next three time periods as defined by NWS
    weather_dict = weather()
    context = {"weather_dict": weather_dict}

    print(weather_dict)
    return render(request, "forecast.html", context)


def todays_tasks(request):
    today = date.today()

    vegetable_list = Garden_DB.objects.order_by("vegetable").all()

    render_task_dict = {}

    for item in vegetable_list:
        # Determine if sow type is Direct or Transplant
        # Set variables to values from dictionary
        sow_type = item.sow_type
        if sow_type == "Direct":
            window_start = item.sow_window_start
            window_end = item.sow_window_end

        else:
            window_start = item.transplant_window_start
            window_end = item.transplant_window_end

        harvest_start = item.harvest_window_start
        harvest_end = item.harvest_window_end

        # Append to dictionary the sow type if in window
        if window_start <= today <= window_end:
            render_task_dict[item.vegetable] = sow_type

        # Append to dictionary if in harvest window
        elif harvest_start <= today <= harvest_end:
            render_task_dict[item.vegetable] = "Harvest"

    context = {"render_task_dict": render_task_dict}

    return render(request, "todays-tasks.html", context)
