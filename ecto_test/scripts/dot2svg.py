#!/usr/bin/env python

import sys
import os

def dot2svg(data):
    print "Data : %s"%data
    tmp_dot_file = data
    tmp_svg_file = 'svg_graph.svg'

    # write the DOT data to file
    command = "dot -Tsvg " + tmp_dot_file + " -o "+ tmp_svg_file #Tsvg can be changed to Tjpg, Tpng, Tgif etc (see dot man pages)
    print("command : %s"%command)
    os.system(command)

    # read the SVG data from file
    tmp_file = open(tmp_svg_file,'r+')
    data = tmp_file.read()
    tmp_file.close()

    # delete the temporary files
    #os.system('rm ' + tmp_dot_file + ' ' + tmp_svg_file)

    return data

if __name__=="__main__":
    print(str(sys.argv))
    if len(sys.argv) != 2:
        print "Usage: python dot2svg.py mygraph.dot"
        exit ()
    filename=sys.argv[1]
    dot2svg(filename)
