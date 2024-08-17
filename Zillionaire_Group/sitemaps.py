from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    # Definování URL, které nejsou v databázi
    def items(self):
        return ['Home', 'Contacts', 'AutoLocksmith',
                'Removals & Storage', 'Cleaning', 'Plumbing',
                'Waste Removals', 'Gardening', 'Electrical Services',
                'Landscaping', 'Refurbishment', 'LCE']  # název URL v urlpatterns

    # Vytvoření absolutní URL pro každou stránku
    def location(self, item):
        return reverse(item)