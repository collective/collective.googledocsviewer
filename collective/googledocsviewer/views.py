from Products.Five import BrowserView

class GoogleDocsViewerController(BrowserView):
    """View to control mimetype supported by the google doc viewer"""
    
    def validate(self):
        return True

    def file_url(self):
        return self.context.absolute_url()
    
    def width(self):
        return '600'
    
    def height(self):
        return '600'
    