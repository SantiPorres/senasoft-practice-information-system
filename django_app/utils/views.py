from django.http import Http404, HttpResponseBadRequest

from formation_area.models import FormationArea, SubFormationArea, FormationEnvironment


class GetObject:
    def get_formation_area_by_id(
            self, 
            formation_area_id
        ):
        try:
            return FormationArea.active.get(id=formation_area_id)
        except FormationArea.DoesNotExist:
            raise Http404

    def get_formation_area_by_slug(
            self, 
            formation_area_slug
        ):
        try:
            return FormationArea.active.get(slug=formation_area_slug)
        except FormationArea.DoesNotExist:
            raise Http404
        
    def get_sub_formation_area_by_slug(
            self, 
            formation_area_slug, 
            sub_formation_area_slug
        ):
        if check_if_formation_area_exists_and_active(formation_area_slug):
            try:
                return SubFormationArea.active.get(
                    formation_area__slug=formation_area_slug, 
                    slug=sub_formation_area_slug
                )
            except SubFormationArea.DoesNotExist:
                raise Http404
        else:
            raise Http404
        
    def get_formation_environment_by_slug(
            self, 
            formation_area_slug_parameter, 
            sub_formation_area_slug,
            formation_environment_slug
        ):
        
        sub_formation_area = self.get_sub_formation_area_by_slug(
            formation_area_slug_parameter, 
            sub_formation_area_slug
        )

        formation_area_slug = sub_formation_area.get_formation_area_slug()

        if formation_area_slug_parameter != formation_area_slug:
            raise HttpResponseBadRequest

        formation_area = GetObject().get_formation_area_by_slug(formation_area_slug)

        try:
            return FormationEnvironment.active.get(
                formation_area=formation_area.id, 
                sub_formation_area=sub_formation_area.id, 
                slug=formation_environment_slug
            )
        except FormationEnvironment.DoesNotExist:
            raise Http404
            


# Formation Area Methods
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
    

# Sub Formation Area Methods
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
    

# Formation Environment Methods
def check_if_formation_environment_exists_and_active(request_slug):
    try: 
        FormationEnvironment.active.get(slug=request_slug)
        return True
    except:
        return False


def check_if_formation_environment_name_exists(request_name):
    try:  
        FormationEnvironment.objects.get(name=request_name)
        return True
    except:
        return False