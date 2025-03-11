#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  al1.py
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
import dataMan

def main(args):
	s = "(sense_body 54 (view_mode high normal) (stamina 8000 1 130600) (speed 0 -101) (head_angle 0) (kick 0) (dash 0) (turn 54) (say 0) (turn_neck 0) (catch 0) (move 1) (change_view 0) (change_focus 0) (arm (movable 0) (expires 0) (target 0 0) (count 0)) (focus (target none) (count 0)) (tackle (expires 0) (count 0)) (collision none) (foul (charged 0) (card none)) (focus_point 0 0))"
	i = 0
	while i < 10000000:
		dataMan.findForward(s, 0, "focus_point")
		i += 1
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
