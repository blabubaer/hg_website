from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from projects.models import Project, ProjectImage
import requests
from io import BytesIO
import os


class Command(BaseCommand):
    help = 'Add sample stock images for projects'

    def handle(self, *args, **options):
        self.stdout.write('Adding sample images to projects...')

        # Stock image URLs that resemble electrical engineering and building themes
        # Using Unsplash images that are free to use
        stock_images = {
            'historische-altstadt-schmalkalden': [
                'https://images.unsplash.com/photo-1541961017774-22349e4a1262?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1511818966892-d7d671e672a2?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop'
            ],
            'landesgartenschau-2015-gruenguertel-schmalkalden': [
                'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop'
            ],
            'viba-nougatworld-aussenanlagen': [
                'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop'
            ],
            'rathaus-schmalkalden-modernisierung': [
                'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&h=600&fit=crop'
            ],
            'produktionshalle-metallbau-schmalkalden': [
                'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop'
            ],
            'seniorenheim-haus-am-park-erweiterung': [
                'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&h=600&fit=crop',
                'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&h=600&fit=crop'
            ]
        }

        # Image captions for each project
        image_captions = {
            'historische-altstadt-schmalkalden': [
                'Historische Gebäude mit moderner Elektroinstallation',
                'Denkmalgeschützte Fassade mit integrierter Beleuchtung',
                'Moderne Sicherheitstechnik in historischem Ambiente'
            ],
            'landesgartenschau-2015-gruenguertel-schmalkalden': [
                'Gartenausstellung mit LED-Beleuchtung',
                'Veranstaltungsfläche mit Sicherheitstechnik',
                'Außenanlagen mit energieeffizienter Beleuchtung'
            ],
            'viba-nougatworld-aussenanlagen': [
                'Produktionsbereich mit moderner Elektrotechnik',
                'Besucherbereich mit integrierter Beleuchtung',
                'Außenanlagen mit Sicherheitstechnik'
            ],
            'rathaus-schmalkalden-modernisierung': [
                'Modernisierte Elektroinstallation',
                'Neue Beleuchtungsanlagen',
                'Integrierte Sicherheitstechnik'
            ],
            'produktionshalle-metallbau-schmalkalden': [
                'Maschinenanschlüsse und Steuerungstechnik',
                'Produktionsbeleuchtung',
                'Sicherheitstechnik für Metallverarbeitung'
            ],
            'seniorenheim-haus-am-park-erweiterung': [
                'Wohnbereiche mit angepasster Beleuchtung',
                'Pflegebereiche mit Sicherheitstechnik',
                'Kommunikationstechnik für Bewohner'
            ]
        }

        for slug, image_urls in stock_images.items():
            try:
                project = Project.objects.get(slug=slug)
                self.stdout.write(f'Adding images to: {project.title}')
                
                # Add main image (first image)
                if not project.main_image:
                    try:
                        response = requests.get(image_urls[0])
                        if response.status_code == 200:
                            image_content = ContentFile(response.content)
                            project.main_image.save(
                                f'{slug}_main.jpg',
                                image_content,
                                save=True
                            )
                            self.stdout.write(f'  Added main image for {project.title}')
                    except Exception as e:
                        self.stdout.write(f'  Error adding main image: {e}')
                
                # Add additional project images
                for i, image_url in enumerate(image_urls[1:], 1):
                    try:
                        response = requests.get(image_url)
                        if response.status_code == 200:
                            caption = image_captions[slug][i] if i < len(image_captions[slug]) else ''
                            
                            project_image = ProjectImage.objects.create(
                                project=project,
                                caption=caption,
                                order=i
                            )
                            
                            # Save the image file
                            image_content = ContentFile(response.content)
                            project_image.image.save(
                                f'{slug}_image_{i}.jpg',
                                image_content,
                                save=True
                            )
                            self.stdout.write(f'  Added image {i} for {project.title}')
                    except Exception as e:
                        self.stdout.write(f'  Error adding image {i}: {e}')
                        
            except Project.DoesNotExist:
                self.stdout.write(f'Project not found: {slug}')
            except Exception as e:
                self.stdout.write(f'Error processing {slug}: {e}')

        self.stdout.write(
            self.style.SUCCESS('Successfully added sample images!')
        ) 