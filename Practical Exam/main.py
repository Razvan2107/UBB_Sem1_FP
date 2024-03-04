from entities import Tractor
from repo import TractorFileRepo
from service import TractorService
from console import Console

repo=TractorFileRepo('tractor.txt')
service_tractor=TractorService(repo)

ui=Console(service_tractor)
ui.ui()