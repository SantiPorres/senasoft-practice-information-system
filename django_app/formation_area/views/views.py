from django.http import Http404

from ..models import FormationArea, SubFormationArea


class GetObject:
    def get_formation_area_by_slug(self, formation_area_slug):
        try:
            return FormationArea.objects.get(slug=formation_area_slug)
        except FormationArea.DoesNotExist:
            raise Http404
        
    def get_formation_area_by_name(self, formation_area_name):
        try:
            return FormationArea.objects.get(name=formation_area_name)
        except FormationArea.DoesNotExist:
            raise Http404
        
    def get_sub_formation_area_by_slug(self, formation_area_slug, sub_formation_area_slug):
        if self.get_formation_area_by_slug(formation_area_slug):
            try:
                return SubFormationArea.objects.get(
                    formation_area__slug=formation_area_slug, 
                    slug=sub_formation_area_slug
                )
            except SubFormationArea.DoesNotExist:
                raise Http404
        else:
            raise Http404
        
    def get_sub_formation_area_by_name(self, formation_area_name, sub_formation_area_name):
        if self.get_formation_area_by_name(formation_area_name):
            try:
                return SubFormationArea.objects.get(formation_area__name=formation_area_name, name=sub_formation_area_name)
            except SubFormationArea.DoesNotExist:
                raise Http404
        else:
            raise Http404