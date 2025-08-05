from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
import os


class Command(BaseCommand):
    help = 'Download and save hero image for the home page'

    def handle(self, *args, **options):
        self.stdout.write('Downloading hero image...')

        # Technical electrical drawing image URL
        image_url = 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop'
        
        # Local path for the image
        static_dir = 'static/images'
        image_filename = 'hero-electrical-drawing.jpg'
        image_path = os.path.join(static_dir, image_filename)
        
        try:
            # Create directory if it doesn't exist
            os.makedirs(static_dir, exist_ok=True)
            
            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                # Save the image locally
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully downloaded hero image to {image_path}')
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download image: HTTP {response.status_code}')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error downloading hero image: {e}')
            ) 