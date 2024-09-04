from typing import Union

# Constants
# Measurement units
UNIT_C = -1
UNIT_CENTIMETRES = -1
UNIT_CICERO = UNIT_C
UNIT_CM = UNIT_CENTIMETRES
UNIT_IN = -1
UNIT_INCHES = UNIT_IN
UNIT_MILLIMETERS = -1
UNIT_MM = UNIT_MILLIMETERS
UNIT_P = -1
UNIT_PICAS = UNIT_P
UNIT_POINTS = -1
UNIT_PT = UNIT_POINTS

# Unit Conversion
pt = -1
inch = -1
p = -1
cm = -1
mm = -1

# Page orientation
PORTRAIT = 0
LANDSCAPE = 1

# Page sizes
PAPER_A0 = [2380, 3368]
PAPER_A0_MM = [841, 1189]
PAPER_A1 = [1684, 2380]
PAPER_A1_MM = [594, 841]
PAPER_A2 = [1190, 1684]
PAPER_A2_MM = [420, 594]
PAPER_A3 = [842, 1190]
PAPER_A3_MM = [297, 420]
PAPER_A4 = [595, 842]
PAPER_A4_MM = [210, 297]
PAPER_A5 = [421, 595]
PAPER_A5_MM = [148, 210]
PAPER_A6 = [297, 421]
PAPER_A6_MM = [105, 148]
PAPER_A7 = [210, 297]
PAPER_A7_MM = [74, 105]
PAPER_A8 = [148, 210]
PAPER_A8_MM = [52, 74]
PAPER_A9 = [105, 148]
PAPER_A9_MM = [37, 52]
PAPER_B0 = [2836, 4008]
PAPER_B0_MM = [1000, 1414]
PAPER_B1 = [2004, 2836]
PAPER_B1_MM = [707, 1000]
PAPER_B2 = [1418, 2004]
PAPER_B2_MM = [500, 707]
PAPER_B3 = [1002, 1418]
PAPER_B3_MM = [353, 500]
PAPER_B4 = [709, 1002]
PAPER_B4_MM = [250, 353]
PAPER_B5 = [501, 709]
PAPER_B5_MM = [176, 250]
PAPER_B6 = [355, 501]
PAPER_B6_MM = [125, 176]
PAPER_B7 = [250, 355]
PAPER_B7_MM = [88, 125]
PAPER_B8 = [178, 250]
PAPER_B8_MM = [62, 88]
PAPER_B9 = [125, 178]
PAPER_B9_MM = [44, 62]
PAPER_B10 = [89, 125]
PAPER_B10_MM = [31, 44]
PAPER_C5E = [462, 649]
PAPER_COMM10E = [298, 683]
PAPER_DLE = [312, 624]
PAPER_EXECUTIVE = [542, 720]
PAPER_FOLIO = [595, 935]
PAPER_LEDGER = [1224, 792]
PAPER_LEGAL = [612, 1008]
PAPER_LETTER = [612, 792]
PAPER_TABLOID = [792, 1224]

# Document layout
FACINGPAGES = -1
NOFACINGPAGES = -1
FIRSTPAGELEFT = -1
FIRSTPAGERIGHT = -1

# Layer modes
NORMAL = -1
DARKEN = -1
LIGHTEN = -1
MULTIPLY = -1
SCREEN = -1
OVERLAY = -1
HARD_LIGHT = -1
SOFT_LIGHT = -1
DIFFERENCE = -1
EXCLUSION = -1
COLOR_DODGE = -1
COLOR_BURN = -1
HUE = -1
SATURATION = -1
COLOR = -1
LUMINOSITY = -1

# Lines and stroke properties (Line style)
LINE_DASH = -1
LINE_DASHDOT = -1
LINE_DASHDOTDOT = -1
LINE_DOT = -1
LINE_SOLID = -1

# Lines and stroke properties (Line join)
JOIN_BEVEL = -1
JOIN_MITTER = -1
JOIN_ROUND = -1

# Lines and stroke properties (Line ending)
CAP_FLAT = -1
CAP_ROUND = -1
CAP_SQUARE = -1

# Fill modes
FILL_NOG = -1
FILL_HORIZONTALG = -1
FILL_VERTICALG = -1
FILL_DIAGONALG = -1
FILL_CROSSDIAGONALG = -1
FILL_RADIALG = -1

# Text frame first line offset mode
FLOP_REALGLYPHHEIGHT = -1
FLOP_FONTASCENT = -1
FLOP_LINESPACING = -1
FLOP_BASELINEGRID = -1

# Text paragraph alignment
ALIGN_LEFT = -1
ALIGN_CENTERED = -1
ALIGN_RIGHT = -1
ALIGN_FORCED = -1
ALIGN_BLOCK = -1

# Tabs modes
TAB_LEFT = -1
TAB_RIGHT = -1
TAB_PERIOD = -1
TAB_COMMA = -1
TAB_CENTER = -1

# LTR and RTL directions
DIRECTION_LTR = -1
DIRECTION_RTL = -1

# Text frame vertical alignment
ALIGNV_TOP = -1
ALIGNV_CENTERED = -1
ALIGNV_BOTTOM = -1

# Image's color space
CSPACE_UNDEFINED = -1
CSPACE_RGB = -1
CSPACE_CMYK = -1
CSPACE_GRAY = -1
CSPACE_DUOTONE = -1
CSPACE_MONOCHROME = -1

# Item types
ITEMTYPE_ARC = -1
ITEMTYPE_GROUP = -1
ITEMTYPE_IMAGEFRAME = -1
ITEMTYPE_ITEMTYPE1 = -1
ITEMTYPE_ITEMTYPE3 = -1
ITEMTYPE_LATEXFRAME = -1
ITEMTYPE_LINE = -1
ITEMTYPE_MULTIPLE = -1
ITEMTYPE_NOTEFRAME = -1
ITEMTYPE_OSGFRAME = -1
ITEMTYPE_PATHTEXT = -1
ITEMTYPE_POLYGON = -1
ITEMTYPE_POLYLINE = -1
ITEMTYPE_REGULARPOLYGON = -1
ITEMTYPE_SPIRAL = -1
ITEMTYPE_SYMBOL = -1
ITEMTYPE_TABLE = -1
ITEMTYPE_TEXTFRAME = -1

# Printer language
PRNLANG_POSTSCRIPT1 = -1
PRNLANG_POSTSCRIPT2 = -1
PRNLANG_POSTSCRIPT3 = -1
PRNLANG_WINDOWSGDI = -1
PRNLANG_PDF = -1

# Dialog buttons
BUTTON_ABORT = 262144
BUTTON_CANCEL = 4194304
BUTTON_IGNORE = 1048576
BUTTON_NO = 65536
BUTTON_NONE = None
BUTTON_OK = 1024
BUTTON_RETRY = 524288
BUTTON_YES = 16384
BUTTON_DEFAULT = -1
BUTTON_ESCAPE = -1

# Dialog icons
ICON_CRITICAL = -1
ICON_INFORMATION = -1
ICON_NONE = -1
ICON_WARNING = -1


# Errors
class Error(Exception):
    pass


class NoDocOpenError(Error):
    pass


class ScribusError(Error):
    pass


class NameExistsError(Error):
    pass


class NotFoundError(Error):
    pass


class WrongFrameTypeError(Error):
    pass


# Document Commands
def closeDoc() -> None:
    """Closes the current document without prompting to save.
    May throw NoDocOpenError if there is no document to close"""


def docChanged(bool: bool) -> None:
    """Enable/disable save icon in the Scribus icon bar and the Save menu item. It's useful to call this procedure when you're changing the document, because Scribus won't automatically notice when you change the document using a script."""


def getDocName() -> str:
    """Returns the name the document was saved under. If the document was not saved before the name is empty."""


def getUnit() -> int:
    """Returns the measurement units of the document. The returned value will be one of the UNIT_* constants: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS"""


def haveDoc() -> int:
    """Returns the quantity of open documents: 0 if none are opened."""


def newDocument(size: tuple, margins: tuple, orientation: int, firstPageNumber: int, unit: int, pagesType: int,
                firstPageOrder: int, numPages: int) -> bool:
    """Creates a new document and returns true if successful. The parameters have the following meaning:

    size = A tuple (width, height) describing the size of the document. You can use predefined constants named PAPER_ e.g. PAPER_A4 etc.

    margins = A tuple (left, right, top, bottom) describing the document margins

    orientation = the page orientation - constants PORTRAIT, LANDSCAPE

    firstPageNumer = is the number of the first page in the document used for pagenumbering. While you'll usually want 1, it's useful to have higher numbers if you're creating a document in several parts.

    unit: this value sets the measurement units used by the document. Use a predefined constant for this, one of: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS.

    pagesType = One of the predefined constants PAGE_n. PAGE_1 is single page, PAGE_2 is for facing pages documents, PAGE_3 is for 3 pages fold and PAGE_4 is 4-fold.

    firstPageOrder = What is position of first page in the document. Indexed from 0 (0 = first).

    numPage = Number of pages to be created.

    The values for width, height and the margins are expressed in the given unit for the document. PAPER_* constants are expressed in points. If your document is not in points, make sure to account for this.

    example: newDocument(PAPER_A4, (10, 10, 20, 20), LANDSCAPE, 7, UNIT_POINTS, PAGE_4, 3, 1)

    May raise ScribusError if is firstPageOrder bigger than allowed by pagesType."""


def openDoc(name: str) -> None:
    """Opens the document "name".

    May raise ScribusError if the document could not be opened."""


def redrawAll() -> None:
    """Redraws all pages."""


def revertDoc() -> None:
    """Revert the current document to its last saved state."""


def saveDoc() -> None:
    """Saves the current document with its current name, returns true if successful. If the document has not already been saved, this may bring up an interactive save file dialog.

If the save fails, there is currently no way to tell."""


def saveDocAs(name: str) -> None:
    """Saves the current document under the new name "name" (which may be a full or relative path).

May raise ScribusError if the save fails."""


def setBaseLine(grid: float, offset: float) -> None:
    """Sets the base line settings of the document, grid spacing(grid), grid offset(offset). Values are given in the measurement units of the document - see UNIT_ constants."""


def setBleeds(lr: float, rr: float, tr: float, br: float) -> None:
    """Sets the bleeds of the document. Left(lr), Right(rr), Top(tr) and Bottom(br) bleeds are given in the measurement units of the document - see UNIT_ constants."""


def setDocType(facingPages: int, firstPageLeft: int) -> None:
    """Sets the document type. To get facing pages set the first parameter to FACINGPAGES, to switch facingPages off use NOFACINGPAGES instead. If you want to be the first page a left side set the second parameter to FIRSTPAGELEFT, for a right page use FIRSTPAGERIGHT."""


def setInfo(author: str, info: str, description: str) -> bool:
    """Sets the document information. "Author", "Info", "Description" are strings."""
    return success


def setMargins(lr: float, rr: float, tr: float, br: float) -> None:
    """Sets the margins of the document, Left(lr), Right(rr), Top(tr) and Bottom(br) margins are given in the measurement units of the document - see UNIT_ constants."""


def setRedraw(redraw: bool) -> None:
    """Disables page redraw when bool = False, otherwise redrawing is enabled. This change will persist even after the script exits, so make sure to call setRedraw(True) in a finally: clause at the top level of your script."""


def setUnit(type: int) -> None:
    """Changes the measurement unit of the document. Possible values for "unit" are defined as constants UNIT_.

May raise ValueError if an invalid unit is passed."""


# Master Page Commands
def applyMasterPage(masterPageName: str, pageNr: int) -> None:
    """Apply master page masterPageName on page pageNumber."""


def closeMasterPage() -> None:
    """Closes the currently active master page, if any, and returns editing to normal. Begin editing with editMasterPage()."""


def createMasterPage(pageName: str) -> None:
    """Creates a new master page named pageName and opens it for editing."""


def deleteMasterPage(pageName: str) -> None:
    """Delete the named master page."""


def editMasterPage(pageName: str) -> None:
    """Enables master page editing and opens the named master page for editing. Finish editing with closeMasterPage()."""


def getMasterPage(pageNr: int) -> None:
    """Returns the name of master page applied to page "nr".

May raise IndexError if the page number is out of range."""


def masterPageNames() -> None:
    """Returns a list of the names of all master pages in the document."""


# Layers
def createLayer(name: str) -> None:
    """Creates a new layer with the name "name".

May raise ValueError if the layer name isn't acceptable."""


def deleteLayer(layer: str) -> None:
    """Deletes the layer with the name "layer". Nothing happens if the layer doesn't exists or if it's the only layer in the document.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def getActiveLayer() -> str:
    """Returns the name of the current active layer."""


def getLayerBlendmode(layer: str) -> int:
    """Returns the "layer" layer blendmode,

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def getLayerTransparency(layer: str) -> float:
    """Returns the "layer" layer transparency,

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def getLayers() -> list:
    """Returns a list with the names of all defined layers."""


def isLayerFlow(layer: str) -> bool:
    """Returns whether text flows around objects on layer "layer", a value of True means that text flows around, a value of False means that the text does not flow around.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerLocked(layer: str) -> bool:
    """Returns whether the layer "layer" is locked or not, a value of True means that the layer "layer" is editable, a value of False means that the layer "layer" is locked.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerOutlined(layer: str) -> bool:
    """Returns whether the layer "layer" is outlined or not, a value of True means that the layer "layer" is outlined, a value of False means that the layer "layer" is normal.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerPrintable(layer: str) -> bool:
    """Returns whether the layer "layer" is printable or not, a value of True means that the layer "layer" can be printed, a value of False means that printing the layer "layer" is disabled.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def isLayerVisible(layer: str) -> bool:
    """Returns whether the layer "layer" is visible or not, a value of True means that the layer "layer" is visible, a value of False means that the layer "layer" is invisible.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def lowerActiveLayer() -> None:
    """Lowers the current active layer."""


def raiseActiveLayer() -> None:
    """Raises the current active layer."""


def sendToLayer(layer: str, name: str = None) -> None:
    """Sends the object "name" to the layer "layer". The layer must exist. If "name" is not given the currently selected item is used.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setActiveLayer(name: str) -> None:
    """Sets the active layer to the layer named "name".

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerBlendmode(layer: str, blend: int) -> None:
    """Sets the layers "layer" blendmode to blend.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerFlow(layer: str, flow: bool) -> None:
    """Sets the layers "layer" flowcontrol to flow. If flow is set to true text in layers above this one will flow around objects on this layer.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable"""


def setLayerLocked(layer: str, locked: bool) -> None:
    """Sets the layer "layer" to be locked or not. If locked is set to true the layer will be locked.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerOutlined(layer: str, outline: bool) -> None:
    """Sets the layer "layer" to be locked or not. If outline is set to true the layer will be displayed outlined.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerPrintable(layer: str, printable: bool) -> None:
    """Sets the layer "layer" to be printable or not. If is the printable set to false the layer won't be printed.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerTransparency(layer: str, trans: float) -> None:
    """Sets the layers "layer" transparency to trans.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


def setLayerVisible(layer: str, visible: bool) -> None:
    """Sets the layer "layer" to be visible or not. If is the visible set to false the layer is invisible.

May raise NotFoundError if the layer can't be found. May raise ValueError if the layer name isn't acceptable."""


# Page Commands
def currentPage() -> int:
    """Returns the number of the current working page. Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is."""


def deletePage(nr: int) -> None:
    """Deletes the given page. Does nothing if the document contains only one page. Page numbers are counted from 1 upwards, no matter what the displayed first page number is.

May raise IndexError if the page number is out of range"""


def getAllObjects(type: int = -1, index: int = 0, layer: str = None) -> list:
    """Returns a list containing the names of all objects of specified type and located on specified page and/or layer. This function accepts several optional keyword arguments: - type (optional) -> None: integer corresponding to item type, by default all items will be returned. - page (optional) -> None: index of page on which returned objects are located, by default the current page. The page index starts at 0 and goes to the total number of pages - 1. - layer (optional) -> None: name of layer on which returned objects are located, by default the function returns items located on all layers. May throw ValueError if page index or layer name is invalid."""


def getHGuides() -> list:
    """Returns a list containing positions of the horizontal guides. Values are in the document's current units - see UNIT_ constants."""


def getPageItems() -> list:
    """Returns a list of tuples with items on the current page. The tuple is: (name, objectType, order) E.g. [('Text1', 4, 0), ('Image1', 2, 1)] means that object named 'Text1' is a text frame (type 4) and is the first at the page..."""


def getPageMargins() -> tuple:
    """Returns the document page margins as a (top, left, right, bottom) tuple in the document's current units. See UNIT_ constants and getPageSize()."""


def getPageNMargins(nr: int) -> tuple:
    """Returns a tuple with a particular page's margins measured in the document's current units. See UNIT_ constants and getPageMargins()"""


def getPageSize(nr: int) -> tuple:
    """Returns a tuple with a particular page's size measured in the document's current units. See UNIT_ constants and getPageMargins()"""


def getPageSize() -> tuple:
    """Returns a tuple with document page dimensions measured in the document's current units. See UNIT_ constants and getPageMargins()"""


def getPageType() -> int:
    """Returns the type of the Page, 0 means left Page, 1 is a middle Page and 2 is a right Page"""


def getVGuides() -> list:
    """See getHGuides."""


def gotoPage(nr: int) -> None:
    """Moves to the page "nr" (that is, makes the current page "nr"). Note that gotoPage doesn't (currently) change the page the user's view is displaying, it just sets the page that script commands will operates on.

May raise IndexError if the page number is out of range."""


def importPage(fromDoc: str, pageList: tuple, create: bool = True, importWhere: int = -1,
               importPageWhere: int = 2) -> None:
    """Imports a set of pages (given as a tuple) from an existing document (the file name must be given). This functions maps the "Page->Import" dropdown menu function. fromDoc: string; the filename of the document to import pages from pageList: tuple with page numbers of pages to import create: number; 0 to replace existing pages, 1 (default) to insert new pages importWhere: number; the page number (of the current document) at which import the pages importWherePage: number; used if create==1; 0 to create pages before selected page; 1 to create pages after selected page; 2 (default) to create pages at the end of the document"""


def moveItemToPage(page: int, name: str = None) -> None:
    """Move the item to the given page (the first page being 0). If "name" is not given the currently selected item is moved."""


def newPage(where: int, masterpage: str = None) -> None:
    """Creates a new page. If "where" is -1 the new Page is appended to the document, otherwise the new page is inserted before "where". Page numbers are counted from 1 upwards, no matter what the displayed first page number of your document is. The optional parameter "masterpage" specifies the name of the master page for the new page.

May raise IndexError if the page number is out of range"""


def pageCount() -> int:
    """Returns the number of pages in the document."""


def setHGuides(guides: tuple) -> None:
    """Sets horizontal guides. Input parameter must be a list of guide positions measured in the current document units - see UNIT_ constants.

Example: setHGuides(getHGuides() + [200.0, 210.0] # add new guides without any lost setHGuides([90,250]) # replace current guides entirely"""


def setVGuides(guides: tuple) -> None:
    """See setHGuides."""


# Text styles
def createCharStyle(name: str, font: str = "Arial Regular", fontsize: float = 12.0, features: str = None,
                    fillcolor: str = "None", fillshade: float = 1.0,
                    strokecolor: str = "Black", strokehade: float = 1.0, baselineoffset: float = -1.0,
                    shadowxoffset: float = -1.0, shadowyoffset: float = -1.0,
                    outlinewidth: float = -1.0, underlineoffset: float = -1.0, underlinewidth: float = -1.0,
                    strikethroughoffset: float = -1.0,
                    strikethroughwidth: float = -1.0, scaleh: float = 1.0, scalev: float = 1.0, tracking: int = -1,
                    language: str = "en", fontfeatures: str = None) -> None:
    """Creates a character style. This function takes the following keyword parameters:

"name" [required] -> name of the char style to create

"font" [optional] -> name of the font to use

fontsize [optional] -> font size to set (double)

"features" [optional] -> nearer typographic details can be defined by a string that might contain the following phrases comma-seperated (without spaces!):

-> inherit

-> bold

-> italic

-> underline

-> underlinewords

-> strike

-> superscript

-> subscript

-> outline

-> shadowed

-> allcaps

-> smallcaps

"fillcolor" [optional], "fillshade" [optional] -> specify fill options

"strokecolor" [optional], "strokeshade" [optional] -> specify stroke options

baselineoffset [optional] -> offset of the baseline

shadowxoffset [optional], shadowyoffset [optional] -> offset of the shadow if used

outlinewidth [optional] -> width of the outline if used

underlineoffset [optional], underlinewidth [optional] -> underline options if used

strikethruoffset [optional], strikethruwidth [optional] -> strikethru options if used

scaleh [optional], scalev [optional] -> scale of the chars

tracking [optional] -> tracking of the text

"language" [optional] -> language code"""


def createParagraphStyle(name: str, linespacingmode: int = 0, linespacing: float = 12.0, alignment: int = 0,
                         leftmargin: float = 0.0, rightmargin: float = 0.0,
                         gapbefore: float = -1.0, gapafter: float = -1.0, firstindent: float = 0.0,
                         hasdropcap: bool = False, dropcaplines: int = -1,
                         dropcapoffset: float = -1.0, charstyle: str = "style", bullet: str = None,
                         tabs: tuple = None) -> None:
    """Creates a paragraph style. This function takes the following keyword parameters:

"name" [required] -> specifies the name of the paragraphstyle to create

linespacingmode [optional] -> specifies the linespacing mode; possible modes are:

fixed linespacing: 0

automatic linespacing: 1

baseline grid linespacing: 2

linespacing [optional] -> specifies the linespacing if using fixed linespacing

alignment [optional] -> specifies the alignment of the paragraph

-> left: 0

-> center: 1

-> right: 2

-> justify: 3

-> extend: 4

leftmargin [optional], rightmargin [optional] -> specify the margin

gapbefore [optional], gapafter [optional] -> specify the gaps to the heading and following paragraphs

firstindent [optional] -> the indent of the first line

hasdropcap [optional] -> specifies if there are caps (1 = yes, 0 = no)

dropcaplines [optional] -> height (in lines) of the caps if used

dropcapoffset [optional] -> offset of the caps if used

"charstyle" [optional] -> char style to use

"bullet" [optional] -> string to use as bullet

"tabs" [optional] -> a list containg tab definitions

-> a tab is defined as a tuple with the following format (position,type,fillchar)"

-> position [required] -> float value for the position

-> type [optional] -> left: 0 [default], right: 1, period: 2, comma: 3, center: 4

-> fillchar [optional] -> the char to fill the space; default is none"""


def getCharStyles() -> list:
    """Return a list of the names of all character styles in the current document."""


def getCharacterStyle(name: str = None) -> str:
    """Return name of character style applied to object named "name". If "name" is not given, the currently selected object is used. If current object has a text selection, the name of style applied to start of selection is returned. Otherwise the name of the item default character style is returned."""


def getParagraphStyle(name: str = None) -> str:
    """Return name of paragraph style applied to object named "name". If "name" is not given, the currently selected object is used. If current object has a text selection, the name of style applied to start of selection is returned. Otherwise the name of the item default style is returned."""


def getParagraphStyles() -> list:
    """Return a list of the names of all paragraph styles in the current document."""


def loadStylesFromFile(filename: str) -> None:
    """Loads paragraph styles from the Scribus document at "filename" into the current document."""


def setCharacterStyle(style: str, name: str = None) -> None:
    """Apply the named character "style" to the object named "name". If object name is not provided, style is applied on current object selection. If multiple objects are selected or if selected object has no text selection, style is applied on selected objects. Otherwise style is applied to the current text selection."""


def setParagraphStyle(style: str, name: str = None):
    """Apply the named paragraph "style" to the object named "name". If object name is not provided, style is applied on current object selection. If multiple objects are selected or if selected object has no text selection, style is applied on selected objects. Otherwise style is applied to the current text selection."""


# Other Styles
def createCustomLineStyle(styleName: str, style: dict) -> None:
    """Creates the custom line style 'styleName'.

styleName -> name of the custom line style to create

This function takes list of dictionary as parameter for "style". Each dictionary represent one subline within style. Dictionary can have those keys:

Color [optional] -> name of the color to use (string)

Dash [optional] -> type of line to use (integer)

LineEnd [optional] -> type of LineEnd to use (integer)

LineJoin [optional] -> type of LineJoin to use (integer)

Shade [optional] -> opacity of line (integer)

Width [optional] -> width of line (double)"""


def getCellStyle(row: int, column: int, name: str = None) -> str:
    """Returns the named style of the cell at "row", "column" in the table "name". If "name" is not given the currently selected item is used.

May throw ValueError if the cell does not exist."""


def getCellStyles() -> list:
    """Return a list of the names of all cell styles in the current document."""


def getCustomLineStyle(name: str = None) -> str:
    """Returns the styleName of custom line style for the object. If object's "name" is not given the currently selected item is used."""


def getLineStyle(name: str = None) -> int:
    """Returns the line style of the object "name". If "name" is not given the currently selected item is used. Line style constants are: LINE_DASH, LINE_DASHDOT, LINE_DASHDOTDOT, LINE_DOT, LINE_SOLID"""


def getLineStyles() -> list:
    """Return a list of the names of all line styles in the current document."""


def getTableStyle(name: str = None) -> str:
    """Returns the named style of the table "name". If "name" is not given the currently selected item is used."""


def getTableStyles() -> list:
    """Return a list of the names of all table styles in the current document."""


def setCellStyle(row: int, column: int, style: str, name: str = None) -> None:
    """Sets the named style of the cell at "row", "column" in the table "name" to "style". If "name" is not given the currently selected item is used.

May throw ValueError if the cell does not exist."""


def setCustomLineStyle(styleName: str, name: str = None) -> None:
    """Sets the custom line style of the object "name" to "styleName" Argument "styleName" is the name of line style as seen in Style Manager If "name" is not given the currently selected item is used."""


def setLineStyle(style: int, name: str = None) -> None:
    """Sets the line style of the object "name" to the style "style". If "name" is not given the currently selected item is used. Argument for this function is number - value from 1 to 37 There are few predefined constants for "style" - LINE_"""


# Selection
def deselectAll() -> None:
    """Deselects all objects in the whole document."""


def getSelectedObject(nr: int = 0) -> None:
    """Returns the name of the selected object. "nr" if given indicates the number of the selected object, e.g. 0 means the first selected object, 1 means the second selected Object and so on."""


def moveSelectionToBack() -> None:
    """Moves current selection to back."""


def moveSelectionToFront() -> None:
    """Moves current selection to front."""


def selectObject(name: str) -> None:
    """Selects the object with the given "name"."""


def selectionCount() -> int:
    """Returns the number of selected objects."""


# Frame Properties
def flipObject(H: bool, V: bool, name: str = None) -> None:
    """Toggle the object "name" horizontal and/or vertical flip. If "name" is not given the currently selected item is used. """


def getCornerRadius(name: str = None) -> int:
    """Returns the corner radius of the object "name". The radius is expressed in points. If "name" is not given the currently selected item is used."""


def getFillBlendmode(name: str = None) -> int:
    """Returns the fill blendmode of the object "name". If "name" is not given the currently selected Item is used."""


def getFillColor(name: str = None) -> str:
    """Returns the name of the fill color of the object "name". If "name" is not given the currently selected item is used."""


def getFillShade(name: str = None) -> int:
    """Returns the shading value of the fill color of the object "name". If "name" is not given the currently selected item is used."""


def getFillTransparency(name: str = None) -> float:
    """Returns the fill transparency of the object "name". If "name" is not given the currently selected Item is used."""


def getLineBlendmod(name: str = None) -> int:
    """Returns the line blendmode of the object "name". If "name" is not given the currently selected Item is used."""


def getLineCap(name: str = None) -> int:
    """Returns the line cap style of the object "name". If "name" is not given the currently selected item is used. The cap types are: CAP_FLAT, CAP_ROUND, CAP_SQUARE"""


def getLineColor(name: str = None) -> str:
    """Returns the name of the line color of the object "name". If "name" is not given the currently selected item is used."""


def getLineJoin(name: str = None) -> int:
    """Returns the line join style of the object "name". If "name" is not given the currently selected item is used. The join types are: JOIN_BEVEL, JOIN_MITTER, JOIN_ROUND"""


def getLineShade(name: str = None) -> int:
    """Returns the shading value of the line color of the object "name". If "name" is not given the currently selected item is used."""


def getLineTransparency(name: str = None) -> float:
    """Returns the line transparency of the object "name". If "name" is not given the currently selected Item is used."""


def getLineWidth(name: str = None) -> int:  # returns integer but wants to take float in setLineWidth?!
    """Returns the line width of the object "name". If "name" is not given the currently selected Item is used."""


def getObjectAttributes(name: str = None) -> list:
    """Returns a list containing all attributes of object \"name\""""


def getObjectType(name: str = None) -> str:
    """Get type of object "name" as a string."""


def getPosition(name: str = None) -> (float, float):
    """Returns a (x, y) tuple with the position of the object "name". If "name" is not given the currently selected item is used. The position is expressed in the actual measurement unit of the document - see UNIT_ for reference."""


def getRotation(name: str = None) -> int:
    """Returns the rotation of the object "name". The value is expressed in degrees, and clockwise is positive. If "name" is not given the currently selected item is used."""


def getSize(name: str = None) -> (float, float):
    """Returns a (width, height) tuple with the size of the object "name". If "name" is not given the currently selected item is used. The size is expressed in the current measurement unit of the document - see UNIT_ for reference."""


def getTextFlowMode(name: str = None) -> int:
    """Return the current text flow mode used by item "name" as an integer. If "name" is not given, the currently selected object is used.

The function will return one of the following value: - 0 : text flow around frame is disabled - 1 : text flow around frame shape - 2 : text flow around frame bounding box - 3 : text flow around frame contour line - 4 : text flow around image clip path"""


def isLocked(name: str = None) -> bool:
    """Returns true if is the object "name" locked. If "name" is not given the currently selected item is used."""


def lockObject(name: str = None) -> bool:
    """Locks the object "name" if it's unlocked or unlock it if it's locked. If "name" is not given the currently selected item is used. Returns true if locked."""


def moveObject(dx: float, dy: float, name: str = None) -> None:
    """Moves the object "name" by dx and dy relative to its current position. The distances are expressed in the current measurement unit of the document (see UNIT constants). If "name" is not given the currently selected item is used. If the object "name" belongs to a group, the whole group is moved."""


def moveObjectAbs(x: float, y: float, name: str = None) -> None:
    """Moves the object "name" to a new location. The coordinates are expressed in the current measurement unit of the document (see UNIT constants). If "name" is not given the currently selected item is used. If the object "name" belongs to a group, the whole group is moved."""


def rotateObject(rot: float, name: str = None) -> None:
    """Rotates the object "name" by "rot" degrees relatively. The object is rotated by the vertex that is currently selected as the rotation point - by default, the top left vertex at zero rotation. Positive values mean counter clockwise rotation when the default rotation point is used. If "name" is not given the currently selected item is used."""


def rotateObjectAbs(rot: float, name: str = None) -> None:
    """Sets the rotation of the object "name" to "rot". Positive values mean counter clockwise rotation. If "name" is not given the currently selected item is used."""


def setCornerRadius(radius: int, name: str = None) -> None:
    """Sets the corner radius of the object "name". The radius is expressed in points. If "name" is not given the currently selected item is used.

May raise ValueError if the corner radius is negative."""


def setFillBlendmode(blendmode: int, name: str = None) -> None:
    """Sets the fill blendmode of the object "name" to blendmode If "name" is not given the currently selected item is used."""


def setFillColor(color: str, name: str = None) -> None:
    """Sets the fill color of the object "name" to the color "color". "color" is the name of one of the defined colors. If "name" is not given the currently selected item is used."""


def setFillShade(shade: int, name: str = None) -> None:
    """Sets the shading of the fill color of the object "name" to "shade". "shade" must be an integer value in the range from 0 (lightest) to 100 (full Color intensity). If "name" is not given the currently selected Item is used.

May raise ValueError if the fill shade is out of bounds."""


def setFillTransparency(transparency: float, name: str = None) -> None:
    """Sets the fill transparency of the object "name" to transparency If "name" is not given the currently selected item is used."""


def setGradientFill(type: int, color1: str, shade1: int, color2: str, shade2: int, name: str = None) -> None:
    """Sets the gradient fill of the object "name" to type. Color descriptions are the same as for setFillColor() and setFillShade(). See the constants for available types (FILL_)."""


def setGradientStop(color: str, shade: int, opacity: float, ramppoint: float, name: str = None) -> None:
    """Set or add a gradient stop to the gradient fill of the object "name" at position ramppoint. Color descriptions are the same as for setFillColor() and setFillShade(). setGradientFill() must have been called previously for the gradient fill to be visible."""


def setitemname(newName: str,
                name: str = None) -> None:  # Not sure if this capitalization is correct, that's how it is in the docs
    """Sets the name of object "name" to newName and returns the name applied. If "name" is not given the currently selected item is used.

May raise NotFoundError if the object doesn't exist."""


def setLineBlendmod(blendmode: int, name: str = None) -> None:
    """Sets the line blendmode of the object "name" to blendmode If "name" is not given the currently selected item is used."""


def setLineCap(endType: int, name: str = None) -> None:
    """Sets the line cap style of the object "name" to the style "cap". If "name" is not given the currently selected item is used. There are predefined constants for "cap" - CAP_."""


def setLineColor(color: str, name: str = None) -> str:
    """Sets the line color of the object "name" to the color "color". If "name" is not given the currently selected item is used."""


def setLineJoin(join: int, name: str = None) -> None:
    """Sets the line join style of the object "name" to the style "join". If "name" is not given the currently selected item is used. There are predefined constants for join - JOIN_."""


def setLineShade(shade: int, name: str = None) -> None:
    """Sets the shading of the line color of the object "name" to "shade". "shade" must be an integer value in the range from 0 (lightest) to 100 (full color intensity). If "name" is not given the currently selected item is used.

May raise ValueError if the line shade is out of bounds."""


def setLineTransparency(transparency: float, name: str = None) -> None:
    """Sets the line transparency of the object "name" to transparency If "name" is not given the currently selected item is used."""


def setLineWidth(width: float, name: str = None) -> None:  # takes float but returns integer in getLineWidth?!
    """Sets line width of the object "name" to "width". "width" must be in the range from 0.0 to 12.0 inclusive, and is measured in points. If "name" is not given the currently selected item is used.

May raise ValueError if the line width is out of bounds."""


def setMultiLine(namedStyle: str, name: str = None) -> None:
    """Sets the line style of the object "name" to the named style "namedStyle". If "name" is not given the currently selected item is used.

May raise NotFoundError if the line style doesn't exist."""


def setOpjectAttributes(attributes: dict, name: str = None) -> None:
    """Sets attributes of the object "name". If "name" is not given the currently selected item is used.

attributes is a list of dictionary. Each dictionary must have those keys: Name, Type, Value, Parameter, Relationship, RelationshipTo, AutoAddTo All values must be strings.

May raise NotFoundError if the object doesn't exist."""


def setTextFlowMode(name: str, state: int) -> None:
    """Enables/disables "Text Flows Around Frame" feature for object "name". Called with parameters string name and optional int "state" (0 <= state <= 3). Setting "state" to 0 will disable text flow. Setting "state" to 1 will make text flow around object frame. Setting "state" to 2 will make text flow around bounding box. Setting "state" to 3 will make text flow around contour line. If "state" is not passed, text flow is toggled."""


def sizeObject(width: float, height: float, name: str = None) -> None:
    """Resizes the object "name" to the given width and height. If "name" is not given the currently selected item is used."""


def getObjectType(name: str = None) -> str:
    """Get type of object "name" as a string."""


def getPosition(name: str = None) -> (float, float):
    """Returns a (x, y) tuple with the position of the object "name". If "name" is not given the currently selected item is used. The position is expressed in the actual measurement unit of the document - see UNIT_ for reference."""


def getRotation(name: str = None) -> int:
    """Returns the rotation of the object "name". The value is expressed in degrees, and clockwise is positive. If "name" is not given the currently selected item is used."""


def getSize(name: str = None) -> (float, float):
    """Returns a (width, height) tuple with the size of the object "name". If "name" is not given the currently selected item is used. The size is expressed in the current measurement unit of the document - see UNIT_ for reference."""


def getTextFlowMode(name: str = None) -> int:
    """Return the current text flow mode used by item "name" as an integer. If "name" is not given, the currently selected object is used.

The function will return one of the following value: - 0 : text flow around frame is disabled - 1 : text flow around frame shape - 2 : text flow around frame bounding box - 3 : text flow around frame contour line - 4 : text flow around image clip path"""


# Text frames
def createPathText(x: float, y: float, textbox: str, beziercurve: str, name: str = None) -> str:
    """Creates a new pathText by merging the two objects "textbox" and "beziercurve" and returns its name. The coordinates are given in the current measurement unit of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used. May raise NotFoundError if one or both of the named base object don't exist."""


def createText(x: float, y: float, width: float, height: float, name: str = None) -> str:
    """Creates a new text frame on the actual page and returns its name. The coordinates are given in the actual measurement unit of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used."""


def dehyphenateText(name: str = None) -> bool:
    """Does dehyphenation on text frame "name". If "name" is not given the currently selected item is used.

May raise WrongFrameTypeError if the target frame is not a text frame"""


def deleteText(name: str = None) -> None:
    """Deletes any text in the text frame "name". If there is some text selected, only the selected text will be deleted. If "name" is not given the currently selected item is used."""


def getAllText(name: str = None) -> str:
    """Returns the text of the text frame "name" and of all text frames which are linked with this frame. If this textframe has some text selected, the selected text is returned. If "name" is not given the currently selected item is used."""


def getCellText(row: int, column: int, name: str = None) -> str:
    """Returns the text content of the cell at "row", "column" in the table "name". If cell has some text selected, the selected text is returned. If "name" is not given the currently selected item is used.

May throw ValueError if the cell does not exist."""


def getColumnGap(name: str = None) -> float:
    """Returns the column gap size of the text frame "name" expressed in points. If "name" is not given the currently selected item is used."""


def getColumns(name: str = None) -> int:
    """Gets the number of columns of the text frame "name". If "name" is not given the currently selected item is used."""


def getFirstLineOffset(name: str = None) -> int:
    """Gets the offset of the first line of text inside text frame "name". If "name" is not given the currently selected item is used."""


def getFirstLinkedFrame(name: str = None) -> int:
    """Return the first text frame in the chain.

If "name" is not given the currently selected item is used."""


def getFont(name: str = None) -> str:
    """Returns the font name for the text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used."""


def getFontFeatures(name: str = None) -> str:
    """Returns the font features for the text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used."""


def getFontSize(name: str = None) -> float:
    """Returns the font size in points for the text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used."""


def getFrameText(name: str = None) -> str:
    """Returns the text visible in text frame "name". If this text frame has some text selected, the selected text is returned. If "name" is not given the currently selected item is used.

This function returns only the text visible in specified frame. If you need to retrieve the text contained in a text chain, use getAllText() instead.

As this function depends on text layout being up-to-date, you may need to call layoutText() or layoutTextChain() before calling this function in order to get expected result."""


def getLastLinkedFrame(name: str = None) -> str:
    """Return the last text frame in the chain.

If "name" is not given the currently selected item is used."""


def getLineSpacing(name: str = None) -> float:
    """Returns the line spacing ("leading") of the text frame "name" expressed in points. If "name" is not given the currently selected item is used."""


def getNextLinkedFrame(name: str = None) -> str:
    """Return the next text frame in the chain or None if specified frame is the last frame in the chain.

If "name" is not given the currently selected item is used."""


def getPrevLinkedFrame(name: str = None) -> str:
    """Return the previous text frame in the chain or None if specified frame is the first frame in the chain.

If "name" is not given the currently selected item is used."""


def getTextColor(name: str = None) -> str:
    """Returns the name of the text color used for text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used."""


def getTextDistances(name: str = None) -> (float, float, float, float):
    """Returns the text distances of the text frame "name" expressed in points. The distances are returned as a tuple like (left, right, top, bottom). If "name" is not given the currently selected item is used."""


def getTextLength(name: str = None) -> int:
    """Returns the length of the text in the text frame "name". If "name" is not given the currently selected item is used."""


def getTextLines(name: str = None) -> int:
    """Returns the number of lines of the text in the text frame "name". If "name" is not given the currently selected item is used.

As this function depends on text layout being up-to-date, you may need to call layoutText() or layoutTextChain() before calling this function in order to get expected result."""


def getTextShade(name: str = None) -> int:
    """Returns the shade of text color used for text frame "name". If this text frame has some text selected the value assigned to the first character of the selection is returned. If "name" is not given the currently selected item is used."""


def getTextVerticalAlignment(name: str = None) -> int:
    """Gets the vertical alignment of text inside text frame "name". If "name" is not given the currently selected item is used."""


def hyphenateText(name: str = None) -> bool:
    """Does hyphenation on text frame "name". If "name" is not given the currently selected item is used.

May raise WrongFrameTypeError if the target frame is not a text frame"""


def insertHTMLText(file: str, name: str = None) -> None:
    """Inserts the text from "file" into the text frame "name". Text must be UTF encoded (see setText() as reference). If "name" is not given the currently selected Item is used."""


def insertText(text: str, pos: int, name: str = None) -> None:
    """Inserts the text "text" at the position "pos" into the text frame "name". Text must be UTF encoded (see setText() as reference) The first character has an index of 0. Inserting text at position -1 appends it to the frame. If "name" is not given the currently selected item is used.

For performance reason, this function does not update text layout in any way. As a consequence, you may need to call layoutText() or layoutTextChain() at appropriate times after calling this function and before calling functions such as getFrameText() or getTextLines().

May throw IndexError for an insertion out of bounds."""


def isPDFBookmark(name: str = None) -> bool:
    """Returns true if the text frame "name" is a PDF bookmark. If "name" is not given the currently selected item is used.

May raise WrongFrameTypeError if the target frame is not a text frame"""


def layoutText(name: str = None) -> None:
    """Relayout text in the text frame "name". If "name" is not given the currently selected item is used."""


def layoutChainText(name: str = None) -> None:
    """Relayout the whole text chain whom the text frame "name" belongs. If "name" is not given the currently selected item is used."""


def linkTextFrames(fromname: str, toname: str) -> None:
    """Link two text frames. The frame named "fromname" is linked to the frame named "toname". The target frame must be an empty text frame and must not link to or be linked from any other frames already.

May throw ScribusException if linking rules are violated."""


def outlineText(
        name: str = None) -> None:  # this was documented as traceText() but I'm very certain that is a mistake as traceText() is defined twice, one being deprecated and referencing outlineText()
    """Convert the text frame "name" to outlines. If "name" is not given the currently selected item is used."""


def selectFrameText(start: int, count: int, name: str = None) -> None:
    """Selects "count" characters of text in the text frame "name" starting from the character "start". Character counting starts at 0. If "count" is zero, any text selection will be cleared. If "count" is -1, the selection will extend to the end of the frame. If "name" is not given the currently selected item is used.

This function only acts on the text visible in the specified frame. If you need to work on the text contained in a text chain, use selectText() instead. As this function depends on text layout being up-to-date, you may need to call layoutText() or layoutTextChain() before calling this function in order to get expected result.

May throw IndexError if the selection is outside the bounds of the text."""


def selectText(start: int, count: int, name: str = None) -> None:
    """Selects "count" characters of text in the story of the text frame "name" starting from the character "start". Character counting starts at 0. If "count" is zero, any text selection will be cleared. If "name" is not given the currently selected item is used.

May throw IndexError if the selection is outside the bounds of the text."""


def setCellText(row: int, column: int, text: str, name: str = None) -> None:
    """Sets the text of the cell at "row", "column" in the table "name" to "text". If "name" is not given the currently selected item is used.

May throw ValueError if the cell does not exist."""


def setColumnGap(size: float, name: str = None) -> None:
    """Sets the column gap of the text frame "name" to the value "size". If "name" is not given the currently selected item is used.

May throw ValueError if the column gap is out of bounds (must be positive)."""


def setColumns(nr: int, name: str = None) -> None:
    """Sets the number of columns of the text frame "name" to the integer "nr". If "name" is not given the currently selected item is used.

May throw ValueError if number of columns is not at least one."""


def setFirstLineOffset(offset: int, name: str = None) -> None:
    """Sets the offset of the first line of text inside text frame "name" to the specified offset policy. If "name" is not given the currently selected item is used. "offset" should be one of the FLOP_* constants defined in this module - see dir(scribus).

May throw ValueError for an invalid offset constant."""


def setFont(font: str, name: str = None) -> None:
    """Sets the font of the text frame "name" to "font". If there is some text selected only the selected text is changed. If "name" is not given the currently selected item is used.

May throw ValueError if the font cannot be found."""


def setFontFeatures(fontfeature: str, name: str = None) -> None:
    """Sets the font features of the text frame "name" to "fontfeature". If there is some text selected only the selected text is changed. If "name" is not given the currently selected item is used.

May throw ValueError if the font cannot be found."""


def setFontSize(size: float, name: str = None) -> None:
    """Sets the font size of the text frame "name" to "size". "size" is treated as a value in points. If there is some text selected only the selected text is changed. "size" must be in the range 1 to 512. If "name" is not given the currently selected item is used.

May throw ValueError for a font size that's out of bounds."""


def setLineSpacing(size: float, name: str = None) -> None:
    """Sets the line spacing ("leading") of the text frame "name" to "size". "size" is a value in points. If "name" is not given the currently selected item is used.

May throw ValueError if the line spacing is out of bounds."""


def setLineSpacingMode(mode: int, name: str = None) -> None:
    """Sets the line spacing mode of the text frame "name" to "mode". If "name" is not given the currently selected item is used. Mode values are the same as in createParagraphStyle.

May throw ValueError if the mode is out of bounds."""


def setPDFBookmark(toggle: bool, name: str = None) -> None:
    """Sets whether (toggle = 1) the text frame "name" is a bookmark nor not. If "name" is not given the currently selected item is used.

May raise WrongFrameTypeError if the target frame is not a text frame"""


def setText(text: str, name: str = None) -> None:
    """Sets the text of the text frame "name" to the text of the string "text". Text must be UTF8 encoded - use e.g. unicode(text, 'iso-8859-2'). See the FAQ for more details. If "name" is not given the currently selected item is used."""


def setTextAlignment(align: int, name: str = None) -> None:
    """Sets the text alignment of the text frame "name" to the specified alignment. If "name" is not given the currently selected item is used. "align" should be one of the ALIGN_ constants defined in this module - see dir(scribus).

May throw ValueError for an invalid alignment constant."""


def setTextAnnotation(icon: int, isopen: bool, name: str = None) -> None:
    """Turns a text fame into a text annotation.

Arguments: "icon" must be 0-8. The values correspond to:( 0 "Note", 1 "Comment", 2 "Key", 3 "Help", 4 "NewParagraph", 5 "Paragraph", 6 "Insert",7 "Cross", 8 "Circle")n"isopen" is True or False. "name" uses the currently selected item if not given.

Returns: None

May raise WrongFrameTypeError if the target frame is not a text frame"""


def setTextColor(color: str, name: str = None) -> None:
    """Sets the text color of the text frame "name" to the color "color". If there is some text selected only the selected text is changed. If "name" is not given the currently selected item is used."""


def setTextDirection(direction: int, name: str = None) -> None:
    """Sets the text direction of the text frame "name" to the specified direction. If "name" is not given the currently selected item is used. "direction" should be one of the DIRECTION_ constants defined in this module - see dir(scribus).

May throw ValueError for an invalid direction constant."""


def setTextDistances(left: float, right: float, top: float, bottom: float, name: str = None) -> None:
    """Sets the text distances of the text frame "name" to the values "left" "right", "top" and "bottom". If "name" is not given the currently selected item is used.

May throw ValueError if any of the distances are out of bounds (must be positive)."""


def setTextScalingH(scale: float, name: str = None) -> None:
    """Sets the horizontal character scaling of the object "name" to "scale" in percent. If "name" is not given the currently selected item is used."""


def setTextScalingV(scale: float, name: str = None) -> None:
    """Sets the vertical character scaling of the object "name" to "scale" in percent. If "name" is not given the currently selected item is used."""


def setTextShade(shade: int, name: str = None) -> None:
    """Sets the shading of the text color of the object "name" to "shade". If there is some text selected only the selected text is changed. "shade" must be an integer value in the range from 0 (lightest) to 100 (full color intensity). If "name" is not given the currently selected item is used."""


def setTextStroke(color: str, name: str = None) -> None:
    """Set "color" of the text stroke. If "name" is not given the currently selected item is used."""


def setTextVerticalAlignment(align: int, name: str = None) -> None:
    """Sets the vertical alignment of text inside text frame "name" to the specified alignment. If "name" is not given the currently selected item is used. "align" should be one of the ALIGNV constants defined in this module - see dir(scribus).

May throw ValueError for an invalid alignment constant."""


def textOverflows(name: str = None, nolinks: bool = False) -> bool:
    """Returns 1 if there are overflowing characters in text frame "name", 0 if not. If is nolinks set to non zero value it takes only one frame - it doesn't use text frame linking. Without this parameter it search all linking chain.

May raise WrongFrameTypeError if the target frame is not an text frame"""


def unlinkTextFrames(name: str) -> None:
    """Remove the specified (named) object from the text frame flow/linkage. If the frame was in the middle of a chain, the previous and next frames will be connected, eg 'a->b->c' becomes 'a->c' when you unlinkTextFrames(b)'

May throw ScribusException if linking rules are violated."""


# Image frames
def createImage(x: float, y: float, width: float, height: float, name: str = None) -> str:
    """Creates a new picture frame on the current page and returns its name. The coordinates are given in the current measurement units of the document. "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used."""


def getImageColorSpace(name: str = None) -> int:
    """Returns the color space for the image loaded in image frame "name" as  one of following integer constants: CSPACE_RGB (0), CSPACE_CMYK (1),  CSPACE_GRAY (2), CSPACE_DUOTONE (3) or CSPACE_MONOCHROME (4). Returns CSPACE_UNDEFINED (-1) if no image is loaded in the frame. If "name" is not given the currently selected item is used."""


def getImageFile(name: str = None) -> str:
    """Returns the filename for the image in the image frame. If "name" is not given the currently selected item is used."""


def getImageOffset(name: str = None) -> (float, float):
    """Returns a (x, y) tuple containing the offset values in point unit of the image frame "name". If "name" is not given the currently selected item is used."""


def getImageScale(name: str = None) -> (float, float):
    """Returns a (x, y) tuple containing the scaling values of the image frame "name". If "name" is not given the currently selected item is used."""


def loadImage(filename: str, name: str = None) -> None:
    """Loads the picture "picture" into the image frame "name". If "name" is not given the currently selected item is used.

May raise WrongFrameTypeError if the target frame is not an image frame"""


def scaleImage(x: float, y: float, name: str = None) -> None:
    """Sets the internal scaling factors of the picture in the image frame "name". If "name" is not given the currently selected item is used. A number of 1 means 100 %. Internal scaling factors are different from the values shown on properties palette. Note : deprecated, use setImageScale() instead.

May raise WrongFrameTypeError if the target frame is not an image frame"""


def setImageBrightness(n: float, name: str = None) -> None:
    """Set image brightness effect of the picture in the image frame "name". If "name" is not given the currently selected item is used. A number of 1 means 100 %. Brightness factor is equal to the value shown on properties palette.

May raise WrongFrameTypeError if the target frame is not an image frame"""


def setImageGrayscale(name: str = None) -> None:
    """Set image grayscale effect of the picture in the image frame "name". If "name" is not given the currently selected item is used.

May raise WrongFrameTypeError if the target frame is not an image frame"""


def setImageOffset(x: float, y: float, name: str = None) -> None:
    """Sets the position of the picture in the image frame "name". If "name" is not given the currently selected item is used. The specified offset values are equal to the values shown on properties palette when point unit is used.

May raise WrongFrameTypeError if the target frame is not an image frame"""


def setImageScale(x: float, y: float, name: str = None) -> None:
    """Sets the scaling factors of the picture in the image frame "name". If "name" is not given the currently selected item is used. A number of 1 means 100 %. Scaling factors are equal to the values shown on properties palette.

May raise WrongFrameTypeError if the target frame is not an image frame"""


def setScaleFrameToImage(name: str = None) -> None:
    """Set frame size on the selected or specified image frame to image size.

May raise WrongFrameTypeError."""


def setScaleImageToFrame(name: str = None) -> None:
    """Sets the scale to frame on the selected or specified image frame to 'scaletoframe'. If 'proportional' is specified, set fixed aspect ratio scaling to 'proportional'. Both 'scaletoframe' and 'proportional' are boolean.

May raise WrongFrameTypeError."""


# Item
def copyObjects(names: Union[str, tuple] = None) -> None:
    """Copies the specified objects or the current object selection if no item names are given. The names of objects to copy can be provided as a string for copying a single object or as a list of strings to copy several objects at once."""


def deleteObject(name: str = None) -> None:
    """Deletes the item with the name "name". If "name" is not given the currently selected item is deleted."""


def duplicateObjects(names: Union[str, tuple] = None) -> list:
    """Creates a duplicate of the specified objects or of the current selection if no names are given. The names of objects to duplicate can be provided as a string to duplicate a single object or as a list of strings to duplicate several objects at once. Returns a list of the names of the newly created objects."""


def getProperty(object: str,
                property: str) -> str:  # apparently you can also use PyCObject as 'object' and get a PyCObject back but no clue how that works
    """Return the value of the property 'property' of the passed 'object'.

The 'object' argument may be a string, in which case the named PageItem is searched for. It may also be a PyCObject, which may point to any C++ QObject instance.

The 'property' argument must be a string, and is the name of the property to look up on 'object'.

The return value varies depending on the type of the property."""


def getPropertyCType(object: str, property: str,
                     includesuper: bool = True) -> str:  # no clue if it actually returns str
    """Returns the name of the C type of 'property' of 'object'. See getProperty() for details of arguments.

If 'includesuper' is true, search inherited properties too."""


def getPropertyNames(object: str, includesuper: bool = True) -> list:
    """Return a list of property names supported by 'object'. If 'includesuper' is true, return properties supported by parent classes as well."""


def groupObjects(list: list) -> str:
    """Groups the objects named in "list" together. "list" must contain the names of the objects to be grouped. If "list" is not given the currently selected items are used. Returns the group name for further referencing."""


def objectExists(name: str = None) -> bool:
    """Test if an object with specified name really exists in the document. The optional parameter is the object name. When no object name is given, returns True if there is something selected."""


def pasteObjects() -> list:
    """Pastes the content of clipboard to canvas. This will be used only or most sensibly following copyObjects(...), since otherwise there will likely be nothing in the clipboard to paste. Returns the names of the newly created object in a list."""


def scaleGroup(factor, name: str = None) -> None:
    """Scales the group the object "name" belongs to. Values greater than 1 enlarge the group, values smaller than 1 make the group smaller e.g a value of 0.5 scales the group to 50 % of its original size, a value of 1.5 scales the group to 150 % of its original size. The value for "factor" must be greater than 0. If "name" is not given the currently selected item is used.

May raise ValueError if an invalid scale factor is passed."""


def setProperty(object: str, property: str, value) -> None:
    """Set 'property' of 'object' to 'value'. If 'value' cannot be converted to a type compatible with the type of 'property', an exception is raised. An exception may also be raised if the underlying setter fails.

See getProperty() for more information."""


def unGroupObjects(name: str = None) -> None:
    """Destructs the group the object "name" belongs to.If "name" is not given the currently selected item is used."""


# Lines
def createBezierLine(list: list, name: str = None) -> str:
    """Creates a new bezier curve and returns its name. The points for the bezier curve are stored in the list "list" in the following order: [x1, y1, kx1, ky1, x2, y2, kx2, ky2...xn. yn, kxn. kyn] In the points list, x and y mean the x and y coordinates of the point and kx and ky meaning the control point for the curve. The coordinates are given in the current measurement units of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of points is passed or if the number of values passed don't group into points without leftovers."""


def createLine(x1: float, y1: float, x2: float, y2: float, name: str = None) -> str:
    """Creates a new line from the point(x1, y1) to the point(x2, y2) and returns its name. The coordinates are given in the current measurement unit of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used."""


def createPolyLine(list: list, name: str = None) -> str:
    """Creates a new polyline and returns its name. The points for the polyline are stored in the list "list" in the following order: [x1, y1, x2, y2...xn. yn]. The coordinates are given in the current measurement units of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of points is passed or if the number of values passed don't group into points without leftovers."""


# Shapes
def combinePolygons() -> None:
    """Combine two or more selected Polygons"""


def createEllipse(x: float, y: float, width: float, height: float, name: str = None) -> str:
    """Creates a new ellipse on the current page and returns its name. The coordinates are given in the current measurement units of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used."""


def createPolygon(list: list, name: str = None) -> str:
    """Creates a new polygon and returns its name. The points for the polygon are stored in the list "list" in the following order: [x1, y1, x2, y2...xn. yn]. At least three points are required. There is no need to repeat the first point to close the polygon. The polygon is automatically closed by connecting the first and the last point. The coordinates are given in the current measurement units of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further access to that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of points is passed or if the number of values passed don't group into points without leftovers."""


def createRect(x: float, y: float, width: float, height: float, name: str = None) -> str:
    """Creates a new rectangle on the current page and returns its name. The coordinates are given in the current measurement units of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name to reference that object in future. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used."""


# Tables
def createTable(x: float, y: float, width: float, height: float, numRows: int, numColumns: int,
                name: str = None) -> str:
    """Creates a new table with the given number of rows and columns on the actual page and returns its name. The coordinates are given in the actual measurement unit of the document (see UNIT constants). "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

May raise NameExistsError if you explicitly pass a name that's already used. May raise ValueError if an insufficient number of rows or columns is passed."""


def getCellColumnSpan(row: int, column: int, name: str = None) -> int:
    """Returns the column span of the cell at "row", "column" in the table "name" or -1 if the cell does not exist. If the cell is covered by another spanning cell, the column span of the spanning cell is returned. If "name" is not given the currently selected item is used."""


def getCellFillColor(row: int, column: int, name: str = None) -> str:
    """Returns the fill color of the cell at "row", "column" in the table "name" If "name" is not given the currently selected item is used."""


def getCellRowSpan(row: int, column: int, name: str = None) -> int:
    """Returns the row span of the cell at "row", "column" in the table "name" or -1 if the cell does not exist. If the cell is covered by another spanning cell, the row span of the spanning cell is returned. If "name" is not given the currently selected item is used."""


def getTableColumnWidth(column: int, name: str = None) -> float:
    """Returns the column width of "column" in the table "name" expressed in points, or 0.0 if the column does not exist. If "name" is not given the currently selected item is used."""


def getTableColumns(name: str = None) -> int:
    """Gets the number of columns in the table "name". If "name" is not given the currently selected item is used."""


def getTableFillColor(name: str = None) -> str:
    """Returns the fill color of the table "name". If "name" is not given the currently selected item is used."""


def getTableRowHeight(row: int, name: str = None) -> float:
    """Returns the row height of "row" in the table "name" expressed in points, or 0.0 if the row does not exist. If "name" is not given the currently selected item is used."""


def getTableRows(name: str = None) -> int:
    """Gets the number of rows in the table "name". If "name" is not given the currently selected item is used."""


def insertTableColumns(index: int, numColumns: int, name: str = None) -> None:
    """Inserts "numColumns" columns before the column at "index" in the table "name". If "name" is not given the currently selected item is used.

May throw ValueError if number of columns is not at least one or index is out of bounds."""


def insertTableRows(index: int, numRows: int, name: str = None) -> None:
    """Inserts "numRows" rows before the row at "index" in the table "name". If "name" is not given the currently selected item is used.

May throw ValueError if number of rows is not at least one or index is out of bounds."""


def mergeTableCells(row: int, column: int, numRows: int, numColumns: int, name: str = None) -> None:
    """Merges the cell at the specified "row" and "column" with the adjacent cells into one cell.

May throw ValueError if number if numRows or numColumns is less than 1 or the specified area is out of bounds."""


def removeTableColumns(index: int, numColumns: int, name: str = None) -> None:
    """Removes "numColumns" columns from the table "name" starting with the column at "index". If "name" is not given the currently selected item is used.

May throw ValueError if number of columns is not at least one or the range to be deleted is out of bounds."""


def removeTableRows(index: int, numRows: int, name: str = None) -> None:
    """Removes "numRows" rows from the table "name" starting with the row at "index". If "name" is not given the currently selected item is used.

May throw ValueError if number of rows is not at least one or the range to be deleted is out of bounds."""


def resizeTableColumn(column: int, width: float, name: str = None) -> None:
    """Resizes "column" to "width" in the table "name". If "name" is not given the currently selected item is used.

May throw ValueError if the width is less than 0 or the column does not exist."""


def resizeTableRow(row: int, width: float, name: str = None) -> None:
    """Resizes "row" to "height" in the table "name". If "name" is not given the currently selected item is used.

May throw ValueError if the height is less than 0 or the row does not exist."""


def setCellBottomBorder(row: int, column: int, borderLines: (float, int, str), name: str = None) -> None:
    """Sets the bottom border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "borderLines" is of the wrong format."""


def setCellBottomPadding(row: int, column: int, padding: float, name: str = None) -> None:
    """Sets the bottom padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "padding" is less than 0."""


def setCellFillColor(row: int, column: int, color: str, name: str = None) -> None:
    """Sets the fill color of the cell at "row", "column" in the table "name" to "color". If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist."""


def setCellLeftBorder(row: int, column: int, borderLines: (float, int, str), name: str = None) -> None:
    """Sets the left border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "borderLines" is of the wrong format."""


def setCellLeftPadding(row: int, column: int, padding: float, name: str = None) -> None:
    """Sets the left padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "padding" less than 0."""


def setCellRightBorder(row: int, column: int, borderLines: (float, int, str), name: str = None) -> None:
    """Sets the right border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "borderLines" is of the wrong format."""


def setCellRightPadding(row: int, column: int, padding: float, name: str = None) -> None:
    """Sets the right padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "padding" less than 0."""


def setCellTopBorder(row: int, column: int, borderLines: (float, int, str), name: str = None) -> None:
    """Sets the top border of the cell at "row", "column" in the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "borderLines" is of the wrong format."""


def setCellTopPadding(row: int, column: int, padding: float, name: str = None) -> None:
    """Sets the top padding of the cell at "row", "column" in the table "name" to "padding". If "name" is not given the currently selected item is used.

May throw ValueError the cell does not exist or if "padding" is less than 0."""


def setTableBottomBorder(borderLines: (float, int, str), name: str = None) -> None:
    """Sets the bottom border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError if "borderLines" is of the wrong format."""


def setTableFillColor(color: str, name: str = None) -> None:
    """Sets the fill color of the table "name" to "color". If "name" is not given the currently selected item is used.

May throw ValueError the table does not exist."""


def setTableLeftBorder(borderLines: (float, int, str), name: str = None) -> None:
    """Sets the left border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError if "borderLines" is of the wrong format."""


def setTableRightBorder(borderLines: (float, int, str), name: str = None) -> None:
    """Sets the right border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError if "borderLines" is of the wrong format."""


def setTableTopBorder(borderLines: (float, int, str), name: str = None) -> None:
    """Sets the top border of the table "name". The border is specified as a list of "(width, style, color)" tuples. "style" is one of the LINE_* constants. If "name" is not given the currently selected item is used.

May throw ValueError if "borderLines" is of the wrong format."""


# Vector images
def placeEPS(filename: str, x: float, y: float) -> None:
    """Places the EPS "filename" onto the current page, x and y specify the coordinate of the topleft corner of the EPS placed on the page

If loading was successful, the selection contains the imported EPS"""


def placeODG(filename: str, x: float, y: float) -> None:
    """Places the ODG "filename" onto the current page, x and y specify the coordinate of the topleft corner of the ODG placed on the page

If loading was successful, the selection contains the imported ODG"""


def placeSVG(filename: str, x: float, y: float) -> None:
    """Places the SVG "filename" onto the current page, x and y specify the coordinate of the topleft corner of the SVG placed on the page

If loading was successful, the selection contains the imported SVG"""


def placeSXD(filename: str, x: float, y: float) -> None:
    """Places the SXD "filename" onto the current page, x and y specify the coordinate of the topleft corner of the SXD placed on the page

If loading was successful, the selection contains the imported SXD"""


def placeVectorFile(filename: str, x: float, y: float) -> None:
    """Places the vector graphic "filename" onto the current page, x and y specify the coordinate of the topleft corner of the graphic placed on the page

If loading was successful, the selection contains the imported graphic"""


# Colors
def changeColorCMYK(name: str, c: int, m: int, y: int, k: int) -> None:
    """Changes the color "name" to the specified CMYK value. The color value is defined via four components c = Cyan, m = Magenta, y = Yellow and k = Black. Color components should be in the range from 0 to 255.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def changeColorCMYKFloat(name: str, c: float, m: float, y: float, k: float) -> None:
    """Changes the color "name" to the specified CMYK value. The color value is defined via four components c = Cyan, m = Magenta, y = Yellow and k = Black. Color components are floating point values between 0 and 100.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def changeColorLab(name: str, L: float, a: float,
                   b: float) -> None:  # this is documented the same as changeColorRGB but this is pretty certainly a mistake
    """Changes the color "name" to the specified CIELab values. The color value is defined via three components: L = luminosity, a = green/red, b = blue/yellow. Color components are floating point values with L between 0 and 100, a and b between -128 and 128.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def changeColorRGB(name: str, r: int, g: int, b: int) -> None:
    """Changes the color "name" to the specified RGB value. The color value is defined via three components r = red, g = green, b = blue. Color components should be in the range from 0 to 255.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def changeColorRGBFloat(name: str, r: float, g: float, b: float) -> None:
    """Changes the color "name" to the specified RGB value. The color value is defined via three components r = red, g = green, b = blue. Color components are floating point values between 0 and 255.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def defineColorCMYK(name: str, c: int, m: int, y: int, k: int) -> None:
    """Defines a new color "name". The color Value is defined via four components: c = Cyan, m = Magenta, y = Yellow and k = Black. Color components should be in the range from 0 to 255.

May raise ValueError if an invalid color name is specified."""


def defineColorCMYKFloat(name: str, c: float, m: float, y: float, k: float) -> None:
    """Defines a new color "name". The color Value is defined via four components: c = Cyan, m = Magenta, y = Yellow and k = Black. Color components are floating point values between 0 and 100.

May raise ValueError if an invalid color name is specified."""


def defineColorLab(name: str, L: float, a: float,
                   b: float) -> None:  # this is documented the same as changeColorRGB but this is pretty certainly a mistake
    """Defines a new color "name" using CIELab values. The color value is defined via three components: L = luminosity, a = green/red, b = blue/yellow. Color components are floating point values with L between 0 and 100, a and b between -128 and 128.

May raise ValueError if an invalid color name is specified."""


def defineColorRGB(name: str, r: int, g: int, b: int) -> None:
    """Defines a new color "name". The color Value is defined via three components: r = red, g = green, b = blue. Color components should be in the range from 0 to 255.

May raise ValueError if an invalid color name is specified."""


def defineColorRGBFloat(name: str, r: float, g: float, b: float) -> None:
    """Defines a new color "name". The color Value is defined via three components: r = red, g = green, b = blue. Color components are floating point values between 0 and 255.

May raise ValueError if an invalid color name is specified."""


def deleteColor(name: str, replace: str = "None") -> None:
    """Deletes the color "name". Every occurrence of that color is replaced by the color "replace". If not specified, "replace" defaults to the color "None" - transparent.

deleteColor works on the default document colors if there is no document open. In that case, "replace", if specified, has no effect.

May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified."""


def getColor(name: str) -> (int, int, int, int):
    """Returns a tuple (C, M, Y, K) containing the four color components of the color "name" from the current document. If no document is open, returns the value of the named color from the default document colors.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def getColorAsRGB(name: str) -> (int, int, int):
    """Returns a tuple (R,G,B) containing the three color components of the color "name" from the current document, converted to the RGB color space. If no document is open, returns the value of the named color from the default document colors.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def getColorAsRGBFloat(name: str) -> (float, float, float):
    """Returns a tuple (R,G,B) containing the three color components of the color "name" from the current document, converted to the RGB color space. Color components are floating point values between 0 and 255. If no document is open, returns the value of the named color from the default document colors.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def getColorFloat(name: str) -> (float, float, float, float):
    """Returns a tuple (C, M, Y, K) containing the four color components of the color "name" from the current document. Color components are floating point values between 0 and 100. If no document is open, returns the value of the named color from the default document colors.

May raise NotFoundError if the named color wasn't found. May raise ValueError if an invalid color name is specified."""


def getColorNames() -> list:
    """Returns a list containing the names of all defined colors in the document. If no document is open, returns a list of the default document colors."""


def isSpotColor(name: str) -> bool:
    """Returns True if the color "name" is a spot color. See also setSpotColor()

May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified."""


def replaceColor(name: str, replace: str) -> None:
    """Every occurrence of the color "name" is replaced by the color "replace".

May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified."""


def setSpotColor(name: str, spot: bool) -> None:
    """Set the color "name" as a spot color if spot parameter is True. See also isSpotColor()

May raise NotFoundError if a named color wasn't found. May raise ValueError if an invalid color name is specified."""


# Fonts
def getFontNames() -> list:
    """Returns a list with the names of all available fonts."""


def getXFontNames() -> list:
    """Returns a larger font info. It's a list of the tuples with: [ (Scribus name, Family, Real name, subset (1|0), embed PS (1|0), font file), (...), ... ]"""


def renderFont(name: str, filename: str, sample: str, size: (int, int),
               format: str = "PPM") -> bool:  # not entirely sure about size, i assume its (xPixels, yPixels) when in doubt, ignore format
    """Creates an image preview of font "name" with given text "sample" and size. If "filename" is not "", image is saved into "filename". Otherwise image data is returned as a string. The optional "format" argument specifies the image format to generate, and supports any format allowed by QPixmap.save(). Common formats are PPM, JPEG, PNG and XPM.

May raise NotFoundError if the specified font can't be found. May raise ValueError if an empty sample or filename is passed."""


# PDF forms
def createPdfAnnotation(which: int, x: float, y: float, w: float, h: float, name: str = None) -> str:
    """Arguments: "which" is one of the following: (0 PDFBUTTON, 1 PDFRADIOBUTTON, 2 PDFTEXTFIELD, 3 PDFCHECKBOX, 4 PDFCOMBOBOX, 5 PDFLISTBOX, 6 PDFTEXTANNOTATION, 7 PDFLINKANNOTATION, 8 PDF3DANNOTATION) "x" and "y" are the coordinates where it will be placed. "w" is its width. "h" is its height. On systems without OSG installed a runtime error will be raised. "name" should be a unique identifier for the object because you need this name for further referencing of that object. If "name" is not given Scribus will create one for you.

Returns: The name of the newly created annotation.

May raise NameExistsError if you explicitly pass a name that's already used."""


def getJSActionScript(which: int, name: str = None) -> str:
    """Gets the JavaScript action for a particular event "which" is one of the following: (0 Mouse Up, 1 Mouse Down, 2 Mouse Enter, 3 Mouse Exit, 4 Focus In, 5 Focus Out, 6 Selection Change, 7 Field Format, 8 Field Validate, 9 Field Calculate) "name" uses the currently selected item if not given. Page item must be an annotation or an error will be raised. Returns: Returns a string if object's action type is Javascript, NONE otherwise."""


def isAnnotated(name: str = None, deannotate: bool = False) -> (str, dict):
    """Queries the item to see if it has a Pdf annotation.

Arguments: "name" uses the currently selected item if not given.

Keyword Arguments: "deannotate" if set to True will turn off the annotation flag

Returns: A tuple with a string at 0 that indicates what type of pdf annotation it is. A dictionary is in index 1 that contains data the function was able to gather. If the item is not a pdf annotation returns None. Passing the keyword parameter deannotate=True returns None.

May raise WrongFrameTypeError if the target frame is not a text frame"""


def setFileAnnotation(path: str, page: int, x: float, y: float, name: str = None, absolute: bool = True) -> None:
    """Turns a text frame into a absolute or relative link annotation. Arguments: "path" is the absolute or relative path to the file. "page" is the page that it links to. "x" and "y" are the x and y coordinates of the page. "name" uses the currently selected item if not given.

Keyword arguments: "absolute" if set to False will make this a relative path. True is its default.

Returns: None

May raise WrongFrameTypeError if the target frame is not a text frame"""


def setJSActionScript(which: int, script: str, name: str = None) -> None:
    """Sets the JavaScript action for a particular event. Also sets the annotation's action to JavaScript. "which" is one of the following: (0 Mouse Up, 1 Mouse Down, 2 Mouse Enter, 3 Mouse Exit, 4 Focus In, 5 Focus Out, 6 Selection Change, 7 Field Format, 8 Field Validate, 9 Field Calculate) "script" is the JavaScript set to the action. "name" uses the currently selected item if not given. Page item must be an annotation or an error will be raised. Returns: None"""


def setURIAnnotation(uri: str, name: str = None) -> None:
    """Turns a text fame into a uri link that gotos the uri specified.

Arguments: "uri" is the uri that the link will be set to. "name" uses the currently selected item if not given.

Returns: None

May raise WrongFrameTypeError if the target frame is not a text frame"""


# PDF export
def readPDFOptions(fileName: str) -> None:
    """Read PDF options from fileName."""


def savePDFOptions(fileName: str) -> None:
    """Save PDF options to fileName."""


class PDFfile:
    """Exporting PDF

Class PDFfile() provides the PDF exporting
for Python scripting as you know it from Save as PDF
menu.
Example:
pdf = PDFfile()
pdf.thumbnails = 1 # generate thumbnails too
pdf.file = 'mypdf.pdf'
pdf.save()"""

    def save(self) -> None:
        """Save selected pages to pdf file."""

    allowAnnots: bool
    """Allow Adding Annotations and Fields. Bool value"""

    allowChange: bool
    """Allow Adding Annotations and Fields. Bool value"""

    allowCopy: bool
    """Allow Copying Text and Graphics. Bool value"""

    allowPrinting: bool
    """Allow Printing the Document. Bool value"""

    article: bool
    """Save Linked Text Frames as PDF Articles
Bool value"""

    binding: int
    """Choose binding.
0 - Left binding
1 - Right binding"""

    bleedMarks: bool
    """Create marks delimiting the bleed area."""

    bleedb: float
    """Bleed Bottom
Distance for bleed from the bottom of the physical page"""

    bleedl: float
    """Bleed Left
Distance for bleed from the left of the physical page"""

    bleedr: float
    """Bleed Right
Distance for bleed from the right of the physical page"""

    bleedt: float
    """Bleed Top
Distance for bleed from the top of the physical page"""

    bookmarks: bool
    """Embed the bookmarks you created in your document.
These are useful for navigating long PDF documents.
Bool value"""

    colorMarks: bool
    """Add color calibration bars."""

    compress: bool
    """Compression switch. Bool value."""

    compressmtd: int
    """Compression method.
0 - Automatic
1 - JPEG
2 - zip
3 - None."""

    cropMarks: bool
    """Create crop marks in the PDF indicating where the paper should be cut or trimmed after printing."""

    displayBookmarks: bool
    """Display the bookmarks upon opening"""

    displayFullscreen: bool
    """Display the document in full screen mode upon opening."""

    displayLayers: bool
    """Display the layer list upon opening. Useful only for PDF 1.5+."""

    displayThumbs: bool
    """Display the page thumbnails upon opening"""

    doClip: bool
    """Do not show objects outside the margins in the exported file"""

    docInfoMarks: bool
    """Add document information which includes the document title and page numbers."""

    domulti: bool
    """Produce a PDF File for every Page. Bool value"""

    downsample: int
    """Downsample image resolusion to this value. Values from 35 to 4000
Set 0 for not to downsample"""

    effval: [int, int, int, int, int, int]
    """List of effection values for each saved page.
It is list of list of six integers. Those int has followin meaning:
- Length of time the page is shown before the presentation
starts on the selected page. (1-3600)
- Length of time the effect runs. (1 - 3600)
A shorter time will speed up the effect,
a longer one will slow it down
- Type of the display effect
0 - No Effect
1 - Blinds
2 - Box
3 - Dissolve
4 - Glitter
5 - Split
6 - Wipe
- Direction of the effect of moving lines
for the split and blind effects.
0 - Horizontal
1 - Vertical
- Starting position for the box and split effects.
0 - Inside
1 - Outside
- Direction of the glitter or wipe effects.
0 - Left to Right
1 - Top to Bottom
2 - Bottom to Top
3 - Right to Left
4 - Top-left to Bottom-Right"""

    embedPDF: bool
    """Export EPS and PDFs in image frames as embedded PDFs. This does not yet take care of colorspaces, so you should know what you are doing before setting this to 'true'."""

    encrypt: bool
    """Use Encription. Bool value"""

    file: str
    """Name of file to save into"""

    fitWindow: bool
    """Fit the document page or pages to the available space in the viewer window."""

    fontEmbedding: int
    """Font embedding mode.
Value must be one of integers: 0 (Embed), 1 (Outline), 2 (No embedding)."""

    fonts: list
    """List of fonts to embed."""

    hideMenuBar: bool
    """Hide the viewer menu bar, the PDF will display in a plain window."""

    hideToolBar: bool
    """Hide the viewer toolbar. The toolbar has usually selection and other editing capabilities."""

    imagepr: any
    """Color profile for images"""

    info: str
    """Mandatory string for PDF/X or the PDF will fail
PDF/X conformance. We recommend you use the title of the document."""

    intenti: int
    """Rendering intent for images
0 - Perceptual
1 - Relative Colorimetric
2 - Saturation
3 - Absolute Colorimetric"""

    intents: int
    """Rendering intent for solid colors
0 - Perceptual
1 - Relative Colorimetric
2 - Saturation
3 - Absolute Colorimetric"""

    isGrayscale: bool
    """Export PDF in grayscale"""

    lpival: list
    """Rendering Settings for individual colors.

This is list of values for each color
Color values have structure [siii] which stand for:
s - Color name ('Black', 'Cyan', 'Magenta', 'Yellow')
i - Frequency (10 to 1000)
i - Angle (-180 to 180)
i - Spot Function
0 - Simple Dot
1 - Line
2 - Round
3 - Ellipse
Be careful when supplying these values as they
are not checked for validity."""

    markLength: float
    """Indicate the length of crop and bleed marks."""

    markOffset: float
    """Indicate the distance offset between mark and page area."""

    mirrorH: bool
    """Mirror Page(s) horizontally"""

    mirrorV: bool
    """Mirror Page(s) vetically"""

    noembicc: bool
    """Don't use embedded ICC profiles. Bool value"""

    openAction: str
    """Javascript to be executed when PDF document is opened."""

    outdst: int
    """Output destination.
0 - screen
1 - printer"""

    owner: str
    """Owner's password"""

    pageLayout: int
    """Document layout in PDF viewer:
0 - Show the document in single page mode
1 - Show the document in single page mode with the pages displayed continuously end to end like a scroll
2 - Show the document with facing pages, starting with the first page displayed on the left
3 - Show the document with facing pages, starting with the first page displayed on the right"""

    pages: list
    """List of pages to print"""

    presentation: bool
    """Enable Presentation Effects.Bool value"""

    printprofc: any
    """Output profile for printing. If possible, get some guidance from your printer on profile selection."""

    profilei: bool
    """Embed a color profile for images. Bool value."""

    profiles: bool
    """Embed a color profile for solid colors. Bool value."""

    quality: int
    """Image quality
0 - Maximum
1 - High
2 - Medium
3 - Low
4 - Minimum"""

    registrationMarks: bool
    """Add registration marks to each separation."""

    resolution: int
    """Resolution of output file. Values from 35 to 4000."""

    rotatedDeg: int
    """Automatically rotate the exported pages
Value must be one of integers: 0, 90, 180 or 270"""

    solidpr: any
    """Color profile for solid colors"""

    subsetList: list
    """List of fonts to subsetted."""

    thumbnails: bool
    """Generate thumbnails. Bool value."""

    useDocBleeds: bool
    """Use the existing bleed settings from the document preferences. Bool value"""

    useLayers: bool
    """Layers in your document are exported to the PDF. Only available if PDF 1.5 is chosen."""

    uselpi: bool
    """Use Custom Rendering Settings. Bool value"""

    usespot: bool
    """Use Spot Colors. Bool value"""

    version: int
    """Choose PDF version to use:
10 = PDF/X4
11 = PDF/X1a
12 = PDF/X-3
13 = PDF 1.3 (Acrobat 4)
14 = PDF 1.4 (Acrobat 5)
15 = PDF 1.5 (Acrobat 6)"""


# Printing
class Printer:
    """Printing

Class Printer() provides printing for Python scripting.

Example:
p = Printer()
p.print()"""

    def printNow(self) -> bool:
        """Prints selected pages."""

    allPrinters: list
    """List of installed printers -- read only"""

    cmd: str
    """Alternative Printer Command"""

    color: bool
    """Print in color.
True - color -- Default
False - greyscale"""

    copies: int
    """Number of copies"""

    file: str
    """Name of file to print into"""

    mph: bool
    """Mirror Pages Horizontal
True
False -- Default"""

    mpv: bool
    """Mirror Pages Vertical
True
False -- Default"""

    pages: list
    """List of pages to be printed"""

    printer: str = "File"
    """Name of printer to use.
Default is 'File' for printing into file"""

    prnLanguage: int = PRNLANG_POSTSCRIPT3
    """Print Language
One of PRNLANG_* constants -- Default is PRNLANG_POSTSCRIPT3."""

    separation: str
    """Print separationl
'No' -- Default
'All'
'Cyan'
'Magenta'
'Yellow'
'Black'
Beware of misspelling because check is not performed"""

    ucr: bool
    """Apply Under Color Removal
True -- Default
False"""

    useICC: bool
    """Use ICC Profile
True
False -- Default"""


# Export to bitmap
def savePageAsEPS(name: str) -> None:
    """Saves the current page as an EPS to the file "name".

May raise ScribusError if the save failed."""


class ImageExport:
    """Image export

Class ImageExport() provides the bitmap graphics exporting
for Python scripting as you know it from Export/Save as Image
menu. See related class PDFfile() and procedure savePageAsEPS().
Example:
i = ImageExport()
i.type = 'PNG' # select one from i.allTypes list
i.scale = 200 # I want to have 200%
i.name = '/home/subik/test.png'
i.save()

two last lines should be replaced with:
i.saveAs('/home/subik/test.png')"""

    def save(self) -> bool:
        """Saves image under previously set 'name'."""

    def saveAs(self) -> bool:
        """Saves image as 'filename'."""

    allTypes: list
    """Available image types. Read only list of strings."""

    dpi: int
    """This value will be used for export as DPI. Read/write integer."""

    name: str
    """Filename of the image. With or without path. Read/write string."""

    quality: int
    """Quality/compression: minimum 1 (poor), maximum 100 (qaulity). Read/write integer."""

    scale: int
    """This is the scaling of the image. 100 = 100% etc. Read/write iteger."""

    transparentBkgnd: bool
    """Enable or disable transparent background."""

    type: str
    """Bitmap type. See allTypes list for more info. Read/write string."""


# View
def scrollDocument(x: float, y: float) -> None:
    """Scroll the document in main GUI window by x and y."""


def zoomDocument(double: float) -> None:
    """Zoom the document in main GUI window. Actions have whole number values like 20.0, 100.0, etc. Zoom to Fit uses -100 as a marker."""


# Dialogs
def fileDialog(caption: str, filter: str = "comment(*.type1 *.type2)", defaultname: str = "defaultname",
               haspreview: bool = False, issave: bool = False,
               isdir: bool = False) -> str:
    """Shows a File Open dialog box with the caption "caption". Files are filtered with the filter string "filter". A default filename or file path can also supplied, leave this string empty when you don't want to use it. A value of True for haspreview enables a small preview widget in the FileSelect box. When the issave parameter is set to True the dialog acts like a "Save As" dialog otherwise it acts like a "File Open Dialog". When the isdir parameter is True the dialog shows and returns only directories. The default for all of the optional parameters is False.

The filter, if specified, takes the form 'comment (.type .type2 ...)'. For example 'Images (.png .xpm *.jpg)'.

Refer to the Qt-Documentation for QFileDialog for details on filters.

Example: fileDialog('Open input', 'CSV files (*.csv)') Example: fileDialog('Save report', defaultname='report.txt', issave=True)"""


def fileQuit() -> None:
    """Quit Scribus."""


def messageBox(caption: str, message: str, icon: int = ICON_NONE, button1: int = BUTTON_OK | BUTTON_DEFAULT,
               button2: int = BUTTON_NONE, button3: int = BUTTON_NONE) -> None:
    """Displays a message box with the title "caption", the message "message", and an icon "icon" and up to 3 buttons. By default no icon is used and a single button, OK, is displayed. Only the caption and message arguments are required, though setting an icon and appropriate button(s) is strongly recommended. The message text may contain simple HTML-like markup.

Returns the BUTTON_* constant value corresponding to the clicked button. For example, if OK button is clicked, BUTTON_OK will be returned regardless of whether it is assigned to button1, button2, or button3.

For the icon and the button parameters there are predefined constants available with the same names as in the Qt Documentation. These are the BUTTON_ and ICON_ constants defined in the module. There are also two extra constants that can be binary-ORed with button constants: BUTTON_DEFAULT Pressing enter presses this button. BUTTON_ESCAPE Pressing escape presses this button.

Usage examples: result = messageBox('Script failed', 'This script only works when you have a text frame selected.', ICON_ERROR) result = messageBox('Monkeys!', 'Something went ook! Was it a monkey?', ICON_WARNING, BUTTON_YES|BUTTON_DEFAULT, BUTTON_NO, BUTTON_IGNORE|BUTTON_ESCAPE)

Defined button and icon constants: BUTTON_NONE, BUTTON_ABORT, BUTTON_CANCEL, BUTTON_IGNORE, BUTTON_NO, BUTTON_NOALL, BUTTON_OK, BUTTON_RETRY, BUTTON_YES, BUTTON_YESALL, ICON_NONE, ICON_INFORMATION, ICON_WARNING, ICON_CRITICAL."""


def messagebarText(string: str) -> None:
    """Writes the "string" into the Scribus message bar (status line). The text must be UTF8 encoded or 'unicode' string(recommended)."""


def newDocDialog() -> bool:
    """Displays the "New Document" dialog box. Creates a new document if the user accepts the settings. Does not create a document if the user presses cancel. Returns true if a new document was created."""


def newStyleDialog() -> str:
    """Shows 'Create new paragraph style' dialog. Function returns real style name or None when user cancels the dialog."""


def progressReset() -> None:
    """Cleans up the Scribus progress bar previous settings. It is called before the new progress bar use. See progressSet."""


def progressSet(nr: int) -> None:
    """Set the progress bar position to "nr", a value relative to the previously set progressTotal. The progress bar uses the concept of steps; you give it the total number of steps and the number of steps completed so far and it will display the percentage of steps that have been completed. You can specify the total number of steps with progressTotal(). The current number of steps is set with progressSet(). The progress bar can be rewound to the beginning with progressReset(). [based on info taken from Trolltech's Qt docs]"""


def progressTotal(max: int) -> None:
    """Sets the progress bar's maximum steps value to the specified number. See progressSet"""


def valueDialog(caption: str, message: str, defaultValue: str = None) -> str:
    """Shows the common 'Ask for string' dialog and returns its value as a string Parameters: window title, text in the window and optional 'default' value.

Example: valueDialog('title', 'text in the window', 'optional')"""
