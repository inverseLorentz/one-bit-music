# Copyright (C) 2021 inverseLorentz
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from random import random

def miditofreq(n):
    return 440.0 * 2**((n-69)/12.0)

def append_note(note, length, output_file):
    with open(output_file, 'ab') as output:
        samples = int(44100/(miditofreq(note)*2))
        for i in range(length//(samples*2)):
            output.write(b'\x00'*samples)
            output.write(b'\xff'*samples)

def append_silence(length, output_file):
    with open(output_file, 'ab') as output:
        output.write(b'\x00'*length)

def append_noise(slowness, length, output_file):
    with open(output_file, 'ab') as output:
        for i in range(length//slowness):
            if random() < 0.5:
                output.write(b'\x00'*slowness)
            else:
                output.write(b'\xff'*slowness)

def compile_text(filename_in, filename_out):
    # type parameter on/off length
    # type is 0 for noise and 1+ for pulse
    # parameter is slowness if noise and midi number if pulse
    # on/off is 0 for silence and 1 for not silence
    # length is length
    with open(filename_out, 'wb') as output:
        output.write(b'')
    
    with open(filename_in, 'r') as file:
        events = file.read().splitlines()
    for element in events:
        if element == '' or element.startswith('#') or element.startswith('//'):
            pass
        else:
            options = element.split(' ')
            if int(options[2]) == 0:
                append_silence(int(options[3]), filename_out)
            elif int(options[2]) == 1:
                if int(options[0]) == 0:
                    append_noise(int(options[1]), int(options[3]), filename_out)
                elif int(options[0]) > 0:
                    append_note(int(options[1]), int(options[3]), filename_out)
