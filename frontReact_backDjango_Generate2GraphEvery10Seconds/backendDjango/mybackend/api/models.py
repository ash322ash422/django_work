from django.db import models

class DataPoint(models.Model):
    x_value = models.FloatField(help_text="X-axis value for both graphs")
    y_value = models.FloatField(help_text="Y-axis value for scatter plot")
    line_value = models.FloatField(help_text="Y-axis value for line graph")
    category = models.CharField(max_length=100, null=True, blank=True, 
                              help_text="Optional category for data grouping")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['x_value']  # Default ordering by x_value

    def __str__(self):
        return f"DataPoint (x={self.x_value}, scatter_y={self.y_value}, line_y={self.line_value})"
