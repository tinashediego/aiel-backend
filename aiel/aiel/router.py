from rest_framework import routers
from team.views import TeamViewSet
from events.views import EventViewSet
from research.views import ResearchViewSet
from board.views import BoardViewSet
from community.views import CommunityViewSet
from briefs.views import BriefViewSet
from resources.views import ResourceViewSet
from mediaapi.views import MediaViewSet
from contactapi.views import ContactUsViewSet

router = routers.DefaultRouter()
router.register('team', TeamViewSet)
router.register('event', EventViewSet)
router.register('research', ResearchViewSet)
router.register('board', BoardViewSet)
router.register('community', CommunityViewSet)
router.register('brief', BriefViewSet)
router.register('resource', ResourceViewSet)
router.register('mediaapi', MediaViewSet)
router.register('contactus', ContactUsViewSet)
