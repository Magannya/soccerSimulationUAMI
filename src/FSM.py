#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FSM.py
#  
#  Copyright 2025 Gustavo <maganya@AltaUbuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def FSM:
    def __init__(attrib, see, communication):
        self.state = 0
        self.attrib = attrib
        self.see = see
        self.communication = communication
        
        print("Finite state machine init.");
    
    def sayHello():
        print("Hello from FSM.")
        
    def start():
        stop = False
        while not stop:
            if self.state = 0:
                self.state = self.idle()
            elif self.state = 1:
                self.state = self.alert()
            elif self.state = 2:
                self.state = self.attack()
            elif self.state = 3:
                self.state = self.offensive()
        
    # ----------------STATES--------------------------------------------
    
    def idle():
        return 0
        
    def alert():
        return 0
        
    def offensive():
        return 0
    
    def attack():
        return 0
        
    # --------------GETTERS Y SETTERS-----------------------------------
    def printState():
        print(f"FSM state: {self.state}")
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
