from django.core.management.base import BaseCommand
from projects.models import ProjectCategory, Project


class Command(BaseCommand):
    help = 'Add sample project categories and projects based on original website'

    def handle(self, *args, **options):
        self.stdout.write('Adding sample project categories and projects...')

        # Define project categories based on original website structure
        categories_data = [
            {
                'name': 'Referenzen Mario Gransow',
                'description': 'Projekte von Mario Gransow',
                'order': 1
            },
            {
                'name': 'Referenzen Egbert Herbert',
                'description': 'Projekte von Egbert Herbert',
                'order': 2
            },
            {
                'name': 'Referenzen Herbert & Gransow',
                'description': 'Gemeinsame Projekte von Herbert & Gransow',
                'order': 3
            }
        ]

        # Create categories
        categories = {}
        for cat_data in categories_data:
            category, created = ProjectCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'order': cat_data['order']
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Define sample projects based on original website
        projects_data = [
            {
                'title': 'Schmalkalden - Historische Altstadt',
                'slug': 'schmalkalden-historische-altstadt',
                'category': 'Referenzen Egbert Herbert',
                'description': 'Umfassende Elektroplanung für die historische Altstadt von Schmalkalden. Das Projekt umfasste die Modernisierung der elektrischen Infrastruktur unter Berücksichtigung des denkmalgeschützten Charakters der Gebäude.',
                'short_description': 'Elektroplanung für historische Altstadt',
                'client': 'Stadt Schmalkalden',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': '2020-06-15',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Landesgartenschau Bad Langensalza',
                'slug': 'landesgartenschau-bad-langensalza',
                'category': 'Referenzen Egbert Herbert',
                'description': 'Technische Gebäudeausrüstung für die Landesgartenschau in Bad Langensalza. Planung und Umsetzung der elektrischen Anlagen für Ausstellungsgebäude, Beleuchtung und Infrastruktur.',
                'short_description': 'TGA für Landesgartenschau',
                'client': 'Landesgartenschau Bad Langensalza GmbH',
                'location': 'Bad Langensalza, Thüringen',
                'completion_date': '2021-04-20',
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'VIBA-Nougatworld Schmalkalden',
                'slug': 'viba-nougatworld-schmalkalden',
                'category': 'Referenzen Egbert Herbert',
                'description': 'Elektroplanung für das VIBA-Nougatworld Besucherzentrum in Schmalkalden. Modernste Technologie für ein interaktives Museumserlebnis mit umweltfreundlichen Lösungen.',
                'short_description': 'Elektroplanung für Besucherzentrum',
                'client': 'VIBA-Nougatworld GmbH',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': '2019-09-10',
                'is_featured': True,
                'order': 3
            },
            {
                'title': 'Industriepark Erfurt',
                'slug': 'industriepark-erfurt',
                'category': 'Referenzen Mario Gransow',
                'description': 'Umfassende Elektroplanung für den neuen Industriepark in Erfurt. Planung der kompletten elektrischen Infrastruktur für moderne Gewerbeflächen mit Fokus auf Nachhaltigkeit.',
                'short_description': 'Elektroplanung für Industriepark',
                'client': 'Stadt Erfurt',
                'location': 'Erfurt, Thüringen',
                'completion_date': '2022-03-15',
                'is_featured': True,
                'order': 4
            },
            {
                'title': 'Klinikum Weimar',
                'slug': 'klinikum-weimar',
                'category': 'Referenzen Mario Gransow',
                'description': 'Technische Gebäudeausrüstung für die Erweiterung des Klinikums Weimar. Planung der elektrischen Anlagen unter Berücksichtigung der besonderen Anforderungen im Gesundheitswesen.',
                'short_description': 'TGA für Klinikerweiterung',
                'client': 'Klinikum Weimar',
                'location': 'Weimar, Thüringen',
                'completion_date': '2021-11-30',
                'is_featured': False,
                'order': 5
            },
            {
                'title': 'Bildungszentrum Jena',
                'slug': 'bildungszentrum-jena',
                'category': 'Referenzen Herbert & Gransow',
                'description': 'Gemeinsames Projekt für das neue Bildungszentrum in Jena. Moderne Elektroplanung für ein zukunftsweisendes Bildungskonzept mit digitalen Lernumgebungen.',
                'short_description': 'Elektroplanung für Bildungszentrum',
                'client': 'Stadt Jena',
                'location': 'Jena, Thüringen',
                'completion_date': '2023-01-20',
                'is_featured': True,
                'order': 6
            }
        ]

        # Create projects
        for project_data in projects_data:
            category = categories[project_data['category']]
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults={
                    'title': project_data['title'],
                    'category': category,
                    'description': project_data['description'],
                    'short_description': project_data['short_description'],
                    'client': project_data['client'],
                    'location': project_data['location'],
                    'completion_date': project_data['completion_date'],
                    'is_featured': project_data['is_featured'],
                    'order': project_data['order']
                }
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully added sample project categories and projects!')
        ) 