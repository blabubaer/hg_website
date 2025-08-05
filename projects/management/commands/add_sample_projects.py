from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.files.base import ContentFile
from projects.models import ProjectCategory, Project
from datetime import date
import os


class Command(BaseCommand):
    help = 'Add sample projects based on original website references'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample projects...')

        # Create categories based on original website structure
        categories = {
            'historische-gebaeude': {
                'name': 'Historische Gebäude',
                'description': 'Elektroplanung für historische Gebäude und Denkmäler',
                'order': 1
            },
            'oeffentliche-gebaeude': {
                'name': 'Öffentliche Gebäude',
                'description': 'Planung für öffentliche Einrichtungen und Verwaltungsgebäude',
                'order': 2
            },
            'industrie-gewerbe': {
                'name': 'Industrie & Gewerbe',
                'description': 'Elektroplanung für Industrieanlagen und Gewerbebauten',
                'order': 3
            },
            'aussenanlagen': {
                'name': 'Außenanlagen',
                'description': 'Elektroplanung für Außenanlagen und Landschaftsgestaltung',
                'order': 4
            }
        }

        # Create categories
        created_categories = {}
        for slug, data in categories.items():
            category, created = ProjectCategory.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'order': data['order']
                }
            )
            created_categories[slug] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
            else:
                self.stdout.write(f'Category already exists: {category.name}')

        # Sample projects based on original website
        projects_data = [
            {
                'title': 'Historische Altstadt Schmalkalden',
                'slug': 'historische-altstadt-schmalkalden',
                'category': 'historische-gebaeude',
                'description': '''Planung der technischen Ausrüstung für die historische Altstadt Schmalkaldens.

Das Projekt umfasste die umfassende Elektroplanung für die historische Altstadt Schmalkaldens, einschließlich der Beleuchtung historischer Gebäude, der Integration moderner Sicherheitstechnik in denkmalgeschützte Strukturen und der Schaffung einer harmonischen Verbindung zwischen historischem Charme und moderner Technik.

Besondere Herausforderungen waren die Integration der Elektroinstallation in die historische Bausubstanz unter Berücksichtigung der Denkmalschutzauflagen sowie die Planung einer energieeffizienten Beleuchtung, die die historische Atmosphäre bewahrt.''',
                'short_description': 'Elektroplanung für die historische Altstadt Schmalkaldens mit Integration moderner Technik in denkmalgeschützte Strukturen.',
                'client': 'Stadt Schmalkalden',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': date(2014, 12, 1),
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Landesgartenschau 2015 - Grüngürtel Schmalkalden',
                'slug': 'landesgartenschau-2015-gruenguertel-schmalkalden',
                'category': 'aussenanlagen',
                'description': '''Außenanlagen im Bereich „Grüngürtel" der Innenstadt Schmalkalden bei den Vorbereitungen zur Landesgartenschau 2015.

Das Projekt umfasste die komplette Elektroplanung für die Außenanlagen der Landesgartenschau 2015 in Schmalkalden. Dazu gehörten die Planung der Beleuchtungsanlagen für die Gartenausstellungen, die elektrotechnische Ausstattung der Veranstaltungsflächen, die Sicherheitstechnik für die Besucherbereiche sowie die Integration von LED-Technologie für energieeffiziente Außenbeleuchtung.

Besondere Highlights waren die Planung der Beleuchtung für die verschiedenen Gartenbereiche, die Schaffung einer stimmungsvollen Atmosphäre für Abendveranstaltungen und die Integration von Sicherheitstechnik, die sich harmonisch in die Gartenlandschaft einfügt.''',
                'short_description': 'Elektroplanung für die Außenanlagen der Landesgartenschau 2015 mit moderner LED-Beleuchtung und Sicherheitstechnik.',
                'client': 'Landesgartenschau Schmalkalden 2015 GmbH',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': date(2015, 4, 1),
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'VIBA-Nougatworld - Außenanlagen',
                'slug': 'viba-nougatworld-aussenanlagen',
                'category': 'industrie-gewerbe',
                'description': '''Planung der Außenanlagen der VIBA-Nougatworld mit modernster Technik.

Das Projekt umfasste die komplette Elektroplanung für die Außenanlagen der VIBA-Nougatworld, einer modernen Produktions- und Erlebniswelt für Nougatprodukte. Dazu gehörten die Planung der Beleuchtungsanlagen für die Produktionsbereiche, die elektrotechnische Ausstattung der Besucherbereiche, die Sicherheitstechnik für die gesamte Anlage sowie die Integration von energieeffizienten LED-Systemen.

Besondere Herausforderungen waren die Planung der Beleuchtung für die Produktionshallen, die Schaffung einer ansprechenden Atmosphäre für Besucherbereiche und die Integration von Sicherheitstechnik, die sowohl den Produktionsanforderungen als auch den Besuchererwartungen gerecht wird.''',
                'short_description': 'Elektroplanung für die Außenanlagen der VIBA-Nougatworld mit modernster LED-Technologie und Sicherheitstechnik.',
                'client': 'VIBA-Nougatworld GmbH',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': date(2016, 6, 1),
                'is_featured': True,
                'order': 3
            },
            {
                'title': 'Rathaus Schmalkalden - Modernisierung',
                'slug': 'rathaus-schmalkalden-modernisierung',
                'category': 'oeffentliche-gebaeude',
                'description': '''Modernisierung der Elektroinstallation im historischen Rathaus Schmalkalden.

Das Projekt umfasste die komplette Modernisierung der Elektroinstallation im historischen Rathaus Schmalkalden unter Berücksichtigung der Denkmalschutzauflagen. Dazu gehörten die Erneuerung der Beleuchtungsanlagen, die Modernisierung der Sicherheitstechnik, die Integration von moderner Kommunikationstechnik sowie die Planung einer energieeffizienten Gebäudetechnik.

Besondere Herausforderungen waren die Integration moderner Technik in die historische Bausubstanz, die Schaffung einer funktionalen Arbeitsumgebung für die Verwaltung und die Bewahrung des historischen Charakters des Gebäudes.''',
                'short_description': 'Modernisierung der Elektroinstallation im historischen Rathaus Schmalkalden mit Integration moderner Technik.',
                'client': 'Stadt Schmalkalden',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': date(2017, 3, 1),
                'is_featured': False,
                'order': 4
            },
            {
                'title': 'Produktionshalle Metallbau Schmalkalden',
                'slug': 'produktionshalle-metallbau-schmalkalden',
                'category': 'industrie-gewerbe',
                'description': '''Elektroplanung für eine moderne Produktionshalle im Metallbau.

Das Projekt umfasste die komplette Elektroplanung für eine neue Produktionshalle im Metallbau, einschließlich der Planung der Maschinenanschlüsse, der Beleuchtungsanlagen für die Produktionsbereiche, der Sicherheitstechnik und der Integration von moderner Steuerungstechnik für die Produktionsanlagen.

Besondere Herausforderungen waren die Planung der Maschinenanschlüsse für verschiedene Produktionsanlagen, die Schaffung einer optimalen Beleuchtung für die Präzisionsarbeit im Metallbau und die Integration von Sicherheitstechnik, die den Anforderungen der Metallverarbeitung gerecht wird.''',
                'short_description': 'Elektroplanung für eine moderne Produktionshalle im Metallbau mit Maschinenanschlüssen und Sicherheitstechnik.',
                'client': 'Metallbau Schmalkalden GmbH',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': date(2018, 9, 1),
                'is_featured': False,
                'order': 5
            },
            {
                'title': 'Seniorenheim "Haus am Park" - Erweiterung',
                'slug': 'seniorenheim-haus-am-park-erweiterung',
                'category': 'oeffentliche-gebaeude',
                'description': '''Elektroplanung für die Erweiterung des Seniorenheims "Haus am Park".

Das Projekt umfasste die Elektroplanung für die Erweiterung des Seniorenheims "Haus am Park", einschließlich der Planung der Beleuchtungsanlagen für die neuen Wohnbereiche, der Sicherheitstechnik für die Pflegebereiche, der Kommunikationstechnik und der Integration von moderner Gebäudetechnik für den Komfort der Bewohner.

Besondere Herausforderungen waren die Schaffung einer wohnlichen Atmosphäre durch angepasste Beleuchtung, die Integration von Sicherheitstechnik, die den besonderen Anforderungen der Pflege gerecht wird, und die Planung von Kommunikationstechnik, die den Bewohnern und dem Pflegepersonal den Alltag erleichtert.''',
                'short_description': 'Elektroplanung für die Erweiterung des Seniorenheims mit moderner Sicherheits- und Kommunikationstechnik.',
                'client': 'Seniorenheim "Haus am Park" GmbH',
                'location': 'Schmalkalden, Thüringen',
                'completion_date': date(2019, 11, 1),
                'is_featured': False,
                'order': 6
            }
        ]

        # Create projects
        for project_data in projects_data:
            category = created_categories[project_data['category']]
            
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
            else:
                self.stdout.write(f'Project already exists: {project.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample projects!')
        ) 