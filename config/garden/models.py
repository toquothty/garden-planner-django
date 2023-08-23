from django.db import models

# Create your models here.
class Garden_DB(models.Model):
    __tablename__ = "garden_DB"

    # id = Column(Integer, primary_key=True)
    vegetable = models.CharField(max_length=200)
    sow_type = models.CharField(max_length=20)  # Direct, Indoors, key used to filter later
    harvest_days = models.IntegerField()  # How many days to harvest
    plant_spacing = models.IntegerField()  # Inches between plants
    seed_depth = models.DecimalField(decimal_places=1, max_digits=5)  # Inches for seed depth
    sow_window_start = models.DateField(blank=True, null=True)  # Window to sow, regardless of sow type
    sow_window_end = models.DateField(blank=True, null=True)  # Window to sow, regardless of sow type
    transplant_window_start = models.DateField(blank=True, null=True)  # Window to transplant if applicable
    transplant_window_end = models.DateField(blank=True, null=True)  # Window to transplant if applicable
    harvest_window_start = models.DateField(blank=True, null=True)  # Window to harvest
    harvest_window_end = models.DateField(blank=True, null=True)  # Window to harvest
    vegetable_picture_url = models.CharField(max_length=500)  # Public URL for vegetable picture

    def __str__(self):
            return self.vegetable
