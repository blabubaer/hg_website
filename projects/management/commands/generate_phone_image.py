from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont
import os


class Command(BaseCommand):
    help = 'Generate phone number image for anti-scraping protection'

    def handle(self, *args, **options):
        self.stdout.write('Generating phone number image...')

        # Phone number to display
        phone_number = "+49 361 75193660"
        
        # Create static directory if it doesn't exist
        static_dir = 'static/images'
        os.makedirs(static_dir, exist_ok=True)
        
        # Image settings
        width = 300
        height = 60
        background_color = (0, 123, 255)  # Bootstrap primary blue
        text_color = (255, 255, 255)      # White text
        
        try:
            # Create image with gradient background
            image = Image.new('RGB', (width, height), background_color)
            draw = ImageDraw.Draw(image)
            
            # Try to use a system font, fallback to default
            try:
                # Try different font options
                font_paths = [
                    'arial.ttf',
                    'Arial.ttf',
                    '/System/Library/Fonts/Arial.ttf',  # macOS
                    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',  # Linux
                    'C:/Windows/Fonts/arial.ttf'  # Windows
                ]
                
                font = None
                for font_path in font_paths:
                    try:
                        font = ImageFont.truetype(font_path, 24)
                        break
                    except:
                        continue
                
                if font is None:
                    font = ImageFont.load_default()
                    
            except Exception as e:
                self.stdout.write(f'Using default font: {e}')
                font = ImageFont.load_default()
            
            # Calculate text position for center alignment
            bbox = draw.textbbox((0, 0), phone_number, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (width - text_width) // 2
            y = (height - text_height) // 2
            
            # Draw text with shadow effect
            shadow_offset = 2
            draw.text((x + shadow_offset, y + shadow_offset), phone_number, 
                     fill=(0, 0, 0, 128), font=font)  # Shadow
            draw.text((x, y), phone_number, fill=text_color, font=font)
            
            # Add subtle border
            draw.rectangle([0, 0, width-1, height-1], outline=(255, 255, 255, 100), width=2)
            
            # Save the image
            image_path = os.path.join(static_dir, 'phone-number.png')
            image.save(image_path, 'PNG', optimize=True)
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully generated phone image: {image_path}')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error generating phone image: {e}')
            ) 