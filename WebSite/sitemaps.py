from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    
    changefreq = 'monthly'
    priority = 0.8
    
    def items(self):
        return ['Home', 'Contacts', 'AutoLocksmith', 'Removals & Storage', 'Cleaning', 'Plumbing', 'Waste Removals', 'Gardening', 'Electrical Services', 'Landscaping', 'Refurbishment', 'LCE']
    
    def location(self, item):
        return reverse(item)