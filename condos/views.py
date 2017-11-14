from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class GuideView(TemplateView):
    template_name = 'guide/guide.html'

class KiheiKaiNaniView(TemplateView):
    template_name = 'condos/kkn.html'

class PacificShoresView(TemplateView):
    template_name = 'condos/ps.html'

class BeachesView(TemplateView):
    template_name = 'guide/beaches/beaches.html'

class SouthMauiView(TemplateView):
    template_name= 'guide/beaches/south_maui_beaches/south_maui_beaches.html'

class KamaoleBeachesView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/kamaole_beaches.html'

class KalamaParkView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/kalama_park.html'

class KeawakapuView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/keawakapu.html'

class UluaView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/ulua.html'

class WaileaView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/wailea.html'

class PalaueaView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/palauea.html'

class PoolenalenaView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/poolenalena.html'

class MaluakaView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/maluaka.html'

class BigBeachView(TemplateView):
    template_name = 'guide/beaches/south_maui_beaches/big_beach.html'



class WestMauiBeachesView(TemplateView):
    template_name = 'guide/beaches/west_maui_beaches/west_maui_beaches.html'

class KaanapaliBeachView(TemplateView):
    template_name = 'guide/beaches/west_maui_beaches/kaanapali_beach.html'

class NapiliBayView(TemplateView):
    template_name = 'guide/beaches/west_maui_beaches/napili_bay.html'

class KapaluaBayView(TemplateView):
    template_name = 'guide/beaches/west_maui_beaches/kapalua_bay.html'

class HonoluaBayView(TemplateView):
    template_name = 'guide/beaches/west_maui_beaches/honolua_bay.html'

class BabyBeachView(TemplateView):
    template_name = 'guide/beaches/west_maui_beaches/baby_beach.html'

class NorthMauiBeachesView(TemplateView):
    template_name = 'guide/beaches/north_maui_beaches/north_maui_beaches.html'



class ActivitiesView(TemplateView):
    template_name = 'guide/activities/activities.html'

class ActivitiesView(TemplateView):
    template_name = 'guide/activities/activities.html'

class OldLahainaLuauView(TemplateView):
    template_name = 'guide/activities/old_lahaina_luau.html'

class WhaleWatchingView(TemplateView):
    template_name = 'guide/activities/whale_watching.html'

class AquariumView(TemplateView):
    template_name = 'guide/activities/aquarium.html'

class HaleakalaView(TemplateView):
    template_name = 'guide/activities/haleakala.html'

class SnorkelingView(TemplateView):
    template_name = 'guide/activities/snorkeling.html'

class DriveToHanaView(TemplateView):
    template_name = 'guide/activities/drive_to_hana.html'

class LaPerouseBayView(TemplateView):
    template_name = 'guide/activities/la_perouse_bay.html'

class MauiFridayTownPartiesView(TemplateView):
    template_name = 'guide/activities/maui_friday_town_parties.html'

class AliiKulaLavendarFarmView(TemplateView):
    template_name = 'guide/activities/alii_kula_lavendar_farm.html'



class PlacesToEatView(TemplateView):
    template_name = 'guide/places_to_eat/places_to_eat.html'

class KiheiRestaurantsView(TemplateView):
    template_name = 'guide/places_to_eat/kihei_restaurants.html'

class LahainaRestaurantsView(TemplateView):
    template_name = 'guide/places_to_eat/lahaina_restaurants.html'

class KaanapaliRestaurantsView(TemplateView):
    template_name = 'guide/places_to_eat/kaanapali_restaurants.html'

class PaiaRestaurantsView(TemplateView):
    template_name = 'guide/places_to_eat/paia_restaurants.html'

class MoreMauiInfoView(TemplateView):
    template_name = 'guide/more_maui_info/more_maui_info.html'

class GroceriesView(TemplateView):
    template_name = 'guide/more_maui_info/groceries.html'

class ContactView(TemplateView):
    template_name = 'contact_us.html'
