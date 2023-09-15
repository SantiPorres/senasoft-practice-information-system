from django.http import Http404

from formation_area.models import FormationArea, SubFormationArea


class GetObject:
    def get_formation_area_by_slug(self, formation_area_slug):
        try:
            return FormationArea.active.get(slug=formation_area_slug)
        except FormationArea.DoesNotExist:
            raise Http404
        
    def get_sub_formation_area_by_slug(self, formation_area_slug, sub_formation_area_slug):
        if self.get_formation_area_by_slug(formation_area_slug):
            try:
                return SubFormationArea.active.get(
                    formation_area__slug=formation_area_slug, 
                    slug=sub_formation_area_slug
                )
            except SubFormationArea.DoesNotExist:
                raise Http404
        else:
            raise Http404


def check_if_formation_area_exists_and_active(request_slug):
    try: 
        FormationArea.active.get(slug=request_slug)
        return True
    except:
        return False
    

def check_if_formation_area_name_exists(request_name):
    try: 
        FormationArea.objects.get(name=request_name)
        return True
    except:
        return False
    

def check_if_sub_formation_area_exists_and_active(request_slug):
    try: 
        SubFormationArea.active.get(slug=request_slug)
        return True
    except:
        return False


def check_if_sub_formation_area_name_exists(request_name):
    try:  
        SubFormationArea.objects.get(name=request_name)
        return True
    except:
        return False