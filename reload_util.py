# The MIT License (MIT)
#
# Copyright (c) 2015 ma-ric
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""Reload package and contained subpackages and modules"""

__author__ = 'ma-ric'

import types
import importlib

def reload_module(module):
    print("reload module:", module.__name__)
    importlib.reload(module)


def issubpackage(package, item):
    if isinstance(item, types.ModuleType):
        p0 = package.__package__
        p1 = item.__package__        
        # print("issubpackage")
        # print("  ", package, p0)
        # print("  ", item, p1)
        if p1:
            return p1.startswith(p0)  # and len(p1) > len(p0)

    return False

        
def sub_packages(package):
    for item_name in dir(package):
        if not item_name.startswith('__'):
            item = getattr(package, item_name)
            if issubpackage(package, item):
                print(item.__name__)
                yield item
   
    
def reload_package(package):
    modul_list = []
    package_stack = [package]
    while len(package_stack) > 0:    
        package = package_stack.pop()
        modul_list.append(package)
        for sp in sub_packages(package):            
            package_stack.append(sp)
        
    for m in reversed(modul_list):
        reload_module(m)
