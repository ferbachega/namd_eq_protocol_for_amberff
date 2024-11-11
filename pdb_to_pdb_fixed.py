#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pdb_to_pdb_fixed.py
#  
#  Copyright 2020 Fernando <fernando@Frost>
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

import os, sys

_file   = os.path.abspath(__file__)
dirname = os.path.dirname(_file)

#print(_file)
crd = '/home/fernando/programs/NAMD_protocol/AMBER_protocol_test/sys.crd'
pdb = '/home/fernando/programs/NAMD_protocol/AMBER_protocol_test/sys_vmd.pdb'
top = '/home/fernando/programs/NAMD_protocol/AMBER_protocol_test/sys.top'



def export_PDB_fixed (pdbin   = None, 
                      pdbout  = None, 
                      wat     = True,
                      lig     = True,
                      protein = False, 
                      
                      ):
    """ Function doc """
    data  = open(pdbin, 'r')
    data  = data.readlines()

    data2 = []
    
    for line in data:
        # ATOM     57  CA  LEU     3      33.707  25.676  30.375  1.00  0.00           C 
        #'ATOM     65 HD11 LEU     3      34.702  23.229  27.083  1.00  0.00           H'
        if line[0:4] == 'ATOM':
            #line2     = line.split()
            
            #atom_name = line[12:16]
            
            if 'WAT' in line:
                header = line[:55]
                header += ' 0.00  0.00'
                header += line[66:]
                #line[55:66]
                line = header
                #line = line.replace('  1.00  ','  0.00  ')
            else:
                header = line[:55]
                header += ' 1.00  0.00'
                header += line[66:]
                #line[55:66]
                line = header
                #line = line.replace('  1.00  ','  0.00  ')
        data2.append(line)
        
    fileout = open(pdbout, 'w')
    fileout.writelines(data2)


def export_PDB_const (pdbin   = None, 
                      pdbout  = None, 
                      wat     = True,
                      lig     = True,
                      protein = False, 
                      
                      ):
    """ Function doc """
    data  = open(pdbin, 'r')
    data  = data.readlines()

    data2 = []
    
    for line in data:
        # ATOM     57  CA  LEU     3      33.707  25.676  30.375  1.00  0.00           C 
        #'ATOM     65 HD11 LEU     3      34.702  23.229  27.083  1.00  0.00           H'
        if 'TER' in line:
            line ='' 
        if 'END' in line:
            line ='' 
           

        if line[0:4] == 'ATOM':
            #line2     = line.split()
            
            atom_name = line[12:16]
            atom_name = atom_name.strip()
            

            #if atom_name in ['C','O','N','H','CA']:
            
            if 'WAT' in line:
                header = line[:55]
                header += ' 0.00  0.00'
                header += line[66:]
                #line[55:66]
                line = header            
            else:
                if atom_name in ['C','N','CA']:
                    
                    header = line[:55]
                    header += ' 1.00  1.00'
                    header += line[66:]
                    #line[55:66]
                    line = header
                    #line = line.replace(' 0.00  0.00',' 1.00  1.00')
                    #print(atom_name)
                else:
                    header = line[:55]
                    header += ' 1.00  0.00'
                    header += line[66:]
                    line = header
                    #line = line.replace(' 0.00  0.00',' 1.00  0.00')
            
        data2.append(line)
        
    fileout = open(pdbout, 'w')
    fileout.writelines(data2)


def get_cell (inputPDB =  None, computePME = True, verbose = True):
    """ Function doc """
    if inputPDB == None:
        filein = open(self.coordinates, 'r')
        coordType = self.coordinates.split('.')
    else:
        filein = open(inputPDB, 'r')
        coordType = inputPDB.split('.')


    #defining coordinate type
    #coordType = filein.split('.')
    #print len(filein)
    if coordType[-1] == 'crd' or coordType[-1] == 'inpcrd' or coordType[-1] == 'rst':
        coords_x = []
        coords_y = []
        coords_z = []
        lines = filein.readlines()
        #print (len(lines))
        lines.pop(-1)
        #lines.pop(0)
        for line in lines:
            
            line2 = line.split()
            print (line2)

            if len(line2) == 6:
        
                try:
                    #print line[30:38], line[38:46], line[46:54]
                    x = float(line2[0])
                    y = float(line2[1])
                    z = float(line2[2])
                    coords_x.append(x)
                    coords_y.append(y)
                    coords_z.append(z)
                    
                    x = float(line2[3])
                    y = float(line2[4])
                    z = float(line2[5])
                    coords_x.append(x)
                    coords_y.append(y)
                    coords_z.append(z)
                except:
                    pass

    if coordType[-1] == 'pdb':
        coords_x = []
        coords_y = []
        coords_z = []

        for line in filein:
            line2 = line.split()
            #print line2
            try:
                if line[0:4] == 'ATOM' or line[0:4] == 'HETA':
                    #print (line[30:38], line[38:46], line[46:54])
                    x = float(line[30:38])
                    y = float(line[38:46])
                    z = float(line[46:54])
                    
                    coords_x.append(x)
                    coords_y.append(y)
                    coords_z.append(z)
                    #print line2, x, y, z
                else:
                    pass
            except:
                pass

    coords_x.sort()
    coords_y.sort()
    coords_z.sort()

    #print coords_x[0],coords_x[-1], coords_x[-1]-coords_x[0] 
    #print coords_y[0],coords_y[-1], coords_y[-1]-coords_y[0] 
    #print coords_z[0],coords_z[-1], coords_z[-1]-coords_z[0] 


    cellBasisVector1  = [ coords_x[-1]-coords_x[0],                      0. ,   0.                       ]
    cellBasisVector2  = [ 0.                      ,coords_y[-1]-coords_y[0] ,   0.                       ]
    cellBasisVector3  = [ 0.                      ,                 0.      ,   coords_z[-1]-coords_z[0] ]
    cellOrigin        = [ (coords_x[-1])/2        , (coords_y[-1] )/2       ,  (coords_z[-1] )/2         ]

    if computePME == True:
        PMEGridSizeX      = int((coords_x[-1]-coords_x[0])+1)
        PMEGridSizeY      = int((coords_y[-1]-coords_y[0])+1)
        PMEGridSizeZ      = int((coords_z[-1]-coords_z[0])+1)

    if verbose == True:
        print ('cellBasisVector1  {:10}  {:10}  {:10} '.format(cellBasisVector1[0], cellBasisVector1[1], cellBasisVector1[2]))
        print ('cellBasisVector2  {:10}  {:10}  {:10} '.format(cellBasisVector2[0], cellBasisVector2[1], cellBasisVector2[2]))			
        print ('cellBasisVector3  {:10}  {:10}  {:10} '.format(cellBasisVector3[0], cellBasisVector3[1], cellBasisVector3[2]))			
        print ('\ncellOrigin        {:10}  {:10}  {:10} \n'.format(cellOrigin[0], cellOrigin [1],cellOrigin[2])	)		
        if computePME == True:			
            print ('PMEGridSizeX 		', PMEGridSizeX )			
            print ('PMEGridSizeY 		', PMEGridSizeY )			
            print ('PMEGridSizeZ 		', PMEGridSizeZ )			
        
    parameters = { 
               'cbv1' : 'cellBasisVector1  {:6}  {:6}  {:6} \n'.format(cellBasisVector1[0], cellBasisVector1[1], cellBasisVector1[2]),
               'cbv2' : 'cellBasisVector2  {:6}  {:6}  {:6} \n'.format(cellBasisVector2[0], cellBasisVector2[1], cellBasisVector2[2]),
               'cbv3' : 'cellBasisVector3  {:6}  {:6}  {:6} \n'.format(cellBasisVector3[0], cellBasisVector3[1], cellBasisVector3[2]),
               'cbvo' : 'cellOrigin        {:6}  {:6}  {:6} \n'.format(cellOrigin[0],       cellOrigin [1],      cellOrigin[2])      ,
               'PME_X': 'PMEGridSizeX                     {} \n'.format(PMEGridSizeX),
               'PME_Y': 'PMEGridSizeY                     {} \n'.format(PMEGridSizeY),
               'PME_Z': 'PMEGridSizeZ                     {} \n'.format(PMEGridSizeZ),
              }
    print(parameters)
    return parameters


def build_equilibration_protocol ( 
                                 crd = None,
                                 top = None, 
                                 pdb = None,
                                 
                                 s01 = 2000, # = 2000   ,
                                 s02 = 1000, # = 10000  ,   #for 1 ns of heating protocol
                                 s03 = 1000, # = 1000000, #for 1 ns of heating protocol
                                 s04 = 1000, # = 1000000, #for 1 ns of heating protocol
                                 s05 = 1000, # = 10000  ,
                                 s06 = 1000, # = 1000000,
                                 s07 = 1000, # = 1000000,
                                 s08 = 1000, # = 1000000,
                                 s09 = 1000, # = 1000000,
                                
                                 output_folder = '/home/fernando/programs/NAMD_protocol/AMBER_protocol_test'
                                ):
    """ Function doc """
    
    parameters = get_cell(inputPDB = '/home/fernando/programs/NAMD_protocol/AMBER_protocol_test/sys.pdb')
    
    templates = {
                '01.namd.tcl' : s01 ,
                '02.namd.tcl' : s02 ,
                '03.namd.tcl' : s03 ,
                '04.namd.tcl' : s04 ,
                '05.namd.tcl' : s05 ,
                '06.namd.tcl' : s06 ,
                '07.namd.tcl' : s07 ,
                '08.namd.tcl' : s08 ,
                '09.namd.tcl' : s09 ,
                }
    
    for template in templates.keys():
        fullpath = os.path.join(dirname, 'templates', template)
        print (fullpath)
        
        data = open(fullpath, 'r')
        
        
        output_file = os.path.join(output_folder, template)
        output = open(output_file, 'w')
        output_data = []
        for line in data:            
            if  'set run_steps' in line:
                line = 'set run_steps {}\n'.format(templates[template])
                #output_data.append(line)
            
            else:
                pass
            
            if 'parmfile' in line:
                line = 'parmfile {}\n'.format (top)
            if 'ambercoor' in line:
                line = 'ambercoor {}\n'.format (crd)
            
            
            if template == '01.namd.tcl':
    
                if 'cellBasisVector1' in line:
                    line = parameters['cbv1']
                if 'cellBasisVector2' in line:
                    line = parameters['cbv2']
                if 'cellBasisVector3' in line:
                    line = parameters['cbv3']
                if 'cellOrigin' in line:
                    line = parameters['cbvo']

            if 'PMEGridSizeX' in line: 
                line = parameters['PME_X']
            if 'PMEGridSizeY' in line: 
                line = parameters['PME_Y']
            if 'PMEGridSizeZ' in line: 
                line = parameters['PME_Z']
            
            output_data.append(line)
        
        output.writelines(output_data)

    pdbout_const = os.path.join(output_folder, 'sys_const.pdb')
    export_PDB_const (pdbin = pdb,
                      pdbout = pdbout_const)


build_equilibration_protocol(
                             crd = crd, 
                             top = top, 
                             pdb = pdb, )


if __name__ == '__main__':
    print (sys.argv)
    args = sys.argv

    pdbin = args[1]
    pdbout_fixed = pdbin.replace('.pdb', '_fixed.pdb')
    pdbout_const = pdbin.replace('.pdb', '_const.pdb')
    #pdbout = args[2]

    export_PDB_fixed(pdbin = pdbin, pdbout = pdbout_fixed)
    export_PDB_const(pdbin = pdbin, pdbout = pdbout_const)
