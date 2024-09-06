from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    # Definování URL, které nejsou v databázi
    def items(self):
        return ['', 'Contacts', 'AutoLocksmith',
                'Removals&Storage', 'Cleaning', 'Plumbing',
                'WasteRemovals', 'Gardening', 'ElectricalServices',
                'Landscaping', 'Refurbishment', 'LCE']  # název URL v urlpatterns

    # Vytvoření absolutní URL pro každou stránku
    def location(self, item):
        return reverse(item)