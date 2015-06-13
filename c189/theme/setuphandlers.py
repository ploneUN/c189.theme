from collective.grok import gs
from c189.theme import MessageFactory as _

@gs.importstep(
    name=u'c189.theme', 
    title=_('c189.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('c189.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
