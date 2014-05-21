# Flip text in the space center upside down
# Nina Stössinger / 20.5.14
# With thanks to Frederik Berlaen

from mojo.events import addObserver
from mojo.UI import CurrentSpaceCenter
from mojo.extensions import ExtensionBundle
from vanilla import ImageButton

class spaceCenterFlipButton(object):
    def __init__(self):
        addObserver(self, "spaceCenterDidOpen", "spaceCenterDidOpen")
        self.bundle = ExtensionBundle("SpaceFlip")
        self.path1 = self.bundle.resourcesPath() + '/flipButton.pdf'
        self.path2 = self.bundle.resourcesPath() + '/flipButton2.pdf'
        self.flipped = False
        
    def spaceCenterDidOpen(self, notification):
        
        s = notification["window"].window()
        s.flipButton = ImageButton((10, 10, 26, 22), imagePath=self.path1, title=None, bordered=0, callback=self.flip)
        
        preLine = s.spacingView.top.glyphLinePreInput
        line = s.spacingView.top.glyphLineInput
        for view in [preLine, line]:
            l, t, w, h = view.getPosSize()
            view.setPosSize((l+32, t, w, h))

        self.s = s
            
    def flip(self, sender=None):
        sp = CurrentSpaceCenter()
        sp.glyphLineView.contentView().setDisplayMode_("Upside Down")

        if not self.flipped:
            self.s.flipButton.setImage(imagePath=self.path2)
            self.flipped = True
        else:
            self.s.flipButton.setImage(imagePath=self.path1)
            self.flipped = False
        
spaceCenterFlipButton()
