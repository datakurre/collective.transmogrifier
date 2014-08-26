# -*- coding:utf-8 -*-
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.utils import Condition
from pdb import Pdb
from zope.interface import classProvides
from zope.interface import implements

import sys


# Breaks on a condition.
class BreakpointSection(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    pdb = Pdb()

    def __init__(self, transmogrifier, name, options, previous):
        condition = options['condition']
        self.condition = Condition(condition, transmogrifier, name, options)
        self.previous = previous
        
    def __iter__(self):
        for item in self.previous:
            if self.condition(item):
                self.pdb.set_trace(sys._getframe().f_back)  # Break!
            yield item
