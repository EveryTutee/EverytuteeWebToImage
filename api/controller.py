from flask import url_for,request,render_template,redirect,flash,send_file
from api import app
import traceback


@app.errorhandler(404)
def not_found(error):
    return {
        "status" : "Invalid URL"
    }, 404

@app.route("/wti", methods=['POST'])
def webToImage():
    try: 
        data = request.get_json()
        if not data: raise ValueError('Data field empty')
        html = data.get("html", None)
        if not html: raise ValueError('HTML field cannot be empty')
    except ValueError as e:
        return {
            "status" : "Failed",
            "error" : str(e)
        }, 400
    except Exception as e:
        traceback.print_exc()
        return {
            "status" : "Failed",
            "error" : str(e)
        }, 400
        
    try:    
        try:
            css = data.get("css", None)
            if not css: raise ValueError        
        except ValueError:
            css= ""
        try:
            options = data.get("options")
            if not options: raise ValueError
        except ValueError:
            options = ""
    except Exception as e:
        return {
            "status" : "Failed",
            "error" : str(e)
        }, 406
    return "This is just testing"