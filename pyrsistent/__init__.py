# -*- coding: utf-8 -*-
"""
This is a ClusterHQ fork of pyrsistent.

It is used as a temporary repository of
changes while we work on getting them integrated
upstream. These changes should be decent logical
units -- this branch is used to collect them all.

THIS SHOULD NEVER BE SUBMITTED UPSTREAM.
IF THIS APPEARS IN A PR TO PYRSISTENT,
IT IS A BAD PR AND SHOULD BE REJECTED OR FIXED.

However, this is perfectly OK to be in
distributions of flocker, in case there are
needed fixes which have not been merged into
a released version of pyrsistent yet.
"""

from pyrsistent._pmap import pmap, m, PMap

from pyrsistent._pvector import pvector, v, PVector

from pyrsistent._pset import pset, s, PSet

from pyrsistent._pbag import pbag, b, PBag

from pyrsistent._plist import plist, l, PList

from pyrsistent._pdeque import pdeque, dq, PDeque

from pyrsistent._checked_types import (
    CheckedPMap, CheckedPVector, CheckedPSet, InvariantException, CheckedKeyTypeError,
    CheckedValueTypeError, CheckedType, optional)

from pyrsistent._field_common import (
    field, PTypeError, pset_field, pmap_field, pvector_field)

from pyrsistent._precord import PRecord

from pyrsistent._pclass import PClass, PClassMeta

from pyrsistent._immutable import immutable

from pyrsistent._helpers import freeze, thaw, mutant

from pyrsistent._transformations import inc, discard, rex, ny


__all__ = ('pmap', 'm', 'PMap',
           'pvector', 'v', 'PVector',
           'pset', 's', 'PSet',
           'pbag', 'b', 'PBag',
           'plist', 'l', 'PList',
           'pdeque', 'dq', 'PDeque',
           'CheckedPMap', 'CheckedPVector', 'CheckedPSet', 'InvariantException', 'CheckedKeyTypeError', 'CheckedValueTypeError', 'CheckedType', 'optional',
           'PRecord', 'field', 'pset_field', 'pmap_field', 'pvector_field',
           'PClass', 'PClassMeta',
           'immutable',
           'freeze', 'thaw', 'mutant',
           'inc', 'discard', 'rex', 'ny')
