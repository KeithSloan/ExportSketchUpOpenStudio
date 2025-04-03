# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2025 Keith Sloan <ipad2@sloan-home.co.uk>               *
# *                                                                         *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# *   Acknowledgements :                                                    *
# *                                                                         *
# *   Takes as input a Volume Name, GDML file  and outputs                  *
# *             a directory structure starting at the specified Volume Name *
# *                                                                         *
# *                                                                         *
# *                                                                         *
# *                                                                         *
############################################################################*

from freecad.openStudio.gbxml_lxml import gbxml_lxml

class GBXML_file:
    def __init__(self):
        print("Init GDML file")
        self.gbxml = gbxml_lxml()

    def FileDetails(self, filename):
        print(f"Set file details {filename}")
        import os
        split = os.path.splitext(filename)
        self.filename  = filename
        self.pathDir = split[0]
        self.docName = split[1][0]
        self.fileType = os.path.splitext(filename)[1][1:]

    def parseGBXML(self, doc, filename):
        self.FileDetails(filename)
        print(f"Process GBXML file {doc.Name} path {filename} Name{self.docName}")
        self.gbxml.parse(filename)

    def exportSite(self, siteObj):
        print(f"Export Site")
        print(dir(siteObj))

    
