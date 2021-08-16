class Palette:

    def __init__(self, name, bgColor, foreColor, shadeColor):
        self.name = name
        self.bgColor = bgColor
        self.foreColor = foreColor
        self.shadeColor = shadeColor

TargetPalettes = [
    Palette("pink-on-yellow", (241,249,2), (201,0,181), (71,2,64)),
    Palette("red-on-green", (107,252,40), (249,14,2), (79,3,0))
    ]