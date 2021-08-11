from api.controller import webToImage
from api.models import WebToImage

def convertion_wrapper(html,css, options):
    
    wti = WebToImage(html,css,".png")
    
    