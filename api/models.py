from api import app
import ImageKit




class WebToImage:
    
    def __init__(self, html, css, output_type:
        self.html = ""
        self.css = ""
        self.output_type = ""
        self.out_image = None
        self.status = ""
        
        
        
        
    @property
    def serialize(self):
        return {
            "status" : self.status,
            "image" : self.out_image,
            "image_type" : self.output_type
        }
        
    
    
     