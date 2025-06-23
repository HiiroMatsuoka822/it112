from django.db import models

class MyItem(models.Model):
    """
    A simple model to demonstrate API functionality.
    It has a title (character field) and a description (text field).
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set when created

    def __str__(self):
        """String representation for a MyItem instance."""
        return self.title

    class Meta:
        # Define the default ordering for query results
        ordering = ['-created_at']
