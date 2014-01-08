#!/usr/bin/env python
# coding=utf-8
"""
Copyright (c) by Filipp Kucheryavy aka Frizzy <filipp.s.frizzy@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:

a. Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer. 

b. Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution. 

c. Neither the name of the nor the names of its contributors may be used to endorse or promote 
products derived from this software without specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS 
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
import sys
import shutil
import six
# configobj is not working with python3 =\

class Config:
    def __init__(self, parent, name, defaultConfigPathPath=""):
        self.parent = parent
        self.name = str(name)
        self.homeDir = os.path.join(os.path.expanduser("~"), self.name)
        self.moduleDir = os.path.abspath(os.path.dirname(
                                sys.modules[self.__module__].__file__))
        
        self.homeConfigPath = os.path.join(self.homeDir, self.name + ".conf")
        if not defaultConfigPathPath:
            self.defaultConfigPath = os.path.join(self.moduleDir, self.name + ".conf")
        
        self.parent.homeDir = self.homeDir

    def createUserConfig(self, paths):
        if not os.path.isdir(self.homeDir):
            try:
                os.makedirs(self.homeDir)
            except:
                six.print_(("Error: can't create %s" % self.homeDir),
                                    file=sys.stderr, end="\n", sep=" ")
                six.print_(("Can not create user config"),
                           file=sys.stderr, end="\n", sep=" ")
                return 1

        for path in paths:
            if os.path.exists(os.path.join(self.homeDir, path)):
                continue
            if os.path.isdir(os.path.join(self.moduleDir, path)):
                try:
                    shutil.copytree(os.path.join(self.moduleDir, path),
                                        os.path.join(self.homeDir, path))
                except:
                    six.print_(("Error: can't create %s"  % os.path.join(self.homeDir, path)),
                                                            file=sys.stderr, end="\n", sep=" ")                                                                                                  
                    six.print_(("Maybe you haven't write acces to %s or %s doesn't exists" %  ((
                                                self.homeDir, os.path.join(self.moduleDir, path)))),
                                                                    file=sys.stderr, end="\n", sep=" ")

            elif os.path.exists(os.path.join(self.moduleDir, path)):
                try:
                    shutil.copy(os.path.join(self.moduleDir, path), os.path.join(self.homeDir, path))
                except:
                    six.print_(("Error: can't create %s"  % os.path.join(self.homeDir, path)),
                                                                file=sys.stderr, end="\n", sep=" ")                                                                                                  
                    six.print_(("Maybe you haven't write acces to %s or %s doesn't exists" %  ((
                                                self.homeDir, os.path.join(self.moduleDir, path)))),
                                                                    file=sys.stderr, end="\n", sep=" ")

        if os.path.isfile(self.defaultConfigPath) and not os.path.isfile(self.homeConfigPath):
            try:
                shutil.copy(self.defaultConfigPath, self.homeConfigPath)
            except:
                six.print_(("Error: can't create %s" % self.homeConfigPath),
                                            file=sys.stderr, end="\n", sep=" ")

    def loadConfig(self):
        def readConfig(self, lines):
            for l in lines:
                if l[0] in "#;":
                    continue
                if "[" == l.strip()[0] and "]" == l.strip()[-1]:
                    continue
                argument = l.split("=", 1)
                if argument:
                    for f in argument:
                        f = f.strip()
                    if len(argument) == 1:
                        argument[1] = "True"
                    self.setArgument(argument[0], argument[1])

        try:
            with open(self.defaultConfigPath, "r") as l:
                lines = l.readlines()
            readConfig(self, lines)
        except:
            six.print_(("Error: can't load %s as default config" % self.defaultConfigPath),
                                                        file=sys.stderr, end="\n", sep=" ")
        try:
            with open(self.homeConfigPath, "r") as l:
                lines = l.readlines()
            readConfig(self, lines)
        except:
            six.print_(("Error: can't load %s as user config" % self.homeConfigPath),
                                                    file=sys.stderr, end="\n", sep=" ")

    def setArgument(self, argument, value):
        if not value or not argument:
            six.print_(("can not set empty argument to self"),
                            file=sys.stderr, end="\n", sep=" ")
            return 1
        self.parent.__dict__[argument] = value

    def saveConfig(self, arguments):
        with open(self.homeConfigPath, "r") as file:
            lines = file.readlines()

        for n, l in enumerate(lines):
            if l[0] in "#;":
                continue
            if "[" == l.strip()[0] and "]" == l.strip()[-1]:
                continue
            argument = l.split("=", 1)[0].strip()
            if argument in arguments:
                lines[n] = "%s = %s\n" % (argument, self.parent.__dict__[argument])
                arguments.remove(argument)
        for argument in arguments:
            lines += "%s = %s\n" % (argument, self.parent.__dict__[argument])

        with open(self.homeConfigPath, "w") as file:
            file.writelines(lines)