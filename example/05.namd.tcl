# 5. Minimize the system with restraints just on the backbone of 
#    the molecule
#
# Minimization of the system with restraints only on the backbone of the
# protein. In earlier runs, all atoms of the protein were restrainted. 
# Now it's just the backbone atoms.

# Note: The atoms to be restrained in this step will vary depending on 
# your system. If you have molecules other than a protein,such as DNA 
# or RNA, the "backbone" atom names will differ.


# input
#-----------------------------------------------------------------------
amber                           yes    
parmfile                        sys.prmtop                                              
ambercoor                       sys.crd                                                 
#coordinates                     C13-7Leu_sys_revisado.pdb

binCoordinates output_04.coor
binVelocities  output_04.vel
extendedSystem output_04.xsc
#-----------------------------------------------------------------------

set run_steps 10000


# Output                                                 
#-----------------------------------------------------------------------
outputName                      output_05                          
restartfreq                     1000          ;# 1000steps = every 2 ps  
dcdfreq                         1000                                     
outputEnergies                  1000                                     
outputPressure                  1000                                     
#-----------------------------------------------------------------------




#-------------------------------------------------------------------------------------------
# Load the reference positions for harmonic restraints
constraints on
consref   sys_const.pdb       ;# Reference file with atom positions
conskfile sys_const.pdb       ;# File with force constants
conskcol  B                   ;# O for occupancy / B  to Use the B-factor column for force constants
constraintScaling 10.0        ;# Optional scaling factor for the constraints

# Example conskfile PDB
# In the conskfile, you’ll include the desired force constants in a specified 
# column (such as B), and each restrained atom should have a non-zero value in this column. For instance:
#  
#                                                            O     B 
#   ATOM      1  CA  ALA A   1       1.000   2.000   3.000  1.00 10.00           C
#   ATOM      2  CB  ALA A   1       1.500   2.500   3.500  1.00  5.00           C 
# In this example, 10.00 and 5.00 in the B column are the force constants (in kcal/mol/Å²). 
#-------------------------------------------------------------------------------------------



#                            TEMPERATURE
#-----------------------------------------------------------------------
# Cannot specify both an initial temperature and a velocity file
set temperature                 300         
#temperature                     $temperature 
firsttimestep                   0                                                                                                    
readexclusions                  yes    
scnb                            2.0   
#-----------------------------------------------------------------------
 


#############################################################                
##                 SIMULATION PARAMETERS                   ##                
##                AMBER-LIKE  SIMULATIONS                  ##
#############################################################              
#-----------------------------------------------------------------------
switching                       off 
exclude                         scaled1-4            
oneFourScaling                  0.833333333          
cutoff                          8                    
watermodel                      tip3                 
pairListDist                    12                   
LJcorrection                    on 
rigidBonds                      all                  
rigidTolerance                  1e-08                
rigidIterations                 100                  
useSettle                       on 
fullElectFrequency              1                    
nonBondedFreq                   1                    
stepspercycle                   10                   
timeStep                        1.0   # change here to 2, if necessary               
#-----------------------------------------------------------------------


# Constant Temperature Control                                               
#-----------------------------------------------------------------------
langevin                        yes    ;# do langevin dynamics                            
langevinDamping                 5       ;# damping coefficient (gamma) of 2/ps
langevinTemp                    $temperature                                             
langevinHydrogen                off    ;# dont couple langevin bath to hydrogens         
#-----------------------------------------------------------------------


# Constant Pressure Control (variable volume)                                
#-----------------------------------------------------------------------
useGroupPressure                yes 
useFlexibleCell                 no  
useConstantArea                 no  
langevinPiston                  yes  
langevinPistonTarget            1.01325               
langevinPistonPeriod            100.0                 
langevinPistonDecay             50.0                  
langevinPistonTemp              $temperature 
#-----------------------------------------------------------------------


# já está escrito no xsc gerado pelo primeiro passo
## Periodic Boundary Conditions                                               
##-----------------------------------------------------------------------
#cellBasisVector1    62.29966     0.00000     0.00000   
#cellBasisVector2     0.00000    59.12049     0.00000   
#cellBasisVector3     0.00000     0.00000    55.57959   
#cellOrigin          31.91115    30.44440    28.60415   
#wrapAll                         on     
##-----------------------------------------------------------------------

# PME (for full-system periodic electrostatics)                              
#-----------------------------------------------------------------------
PME                             yes                                                      
PMEGridSpacing                  1.0           
PMEGridSizeX                    63            
PMEGridSizeY                    60            
PMEGridSizeZ                    56            
PMETolerance                    1e-06         
PMEInterpOrder                  4             
#-----------------------------------------------------------------------

#minimize                        2000     
minimize $run_steps

#run 1000 


#############################################################                
## EXECUTION SCRIPT                                        ##                
#############################################################               

# Minimization                                                           
# minimize                        2000     

# # Incremento de temperatura em etapas
# set temperature_initial   100    ;# Temperatura inicial (em K)
# set temperature_final     300    ;# Temperatura final desejada (em K)
# set heating_steps         100    ;# Número de passos para o aquecimento
# set increment [expr {($temperature_final - $temperature_initial) / $heating_steps}]
# 
# # Rampa de aquecimento
# # obs: são 100 heating_steps, como 10000 passa, isso resulta em 1.000.000 passos = 1ns
# for {set i 0} {$i < $heating_steps} {incr i} {
#     set current_temp [expr {$temperature_initial + $i * $increment}]
#     langevinTemp $current_temp
#     #run 10000               ;# Número de passos para cada incremento de temperatura
#     run 100                 ;# Número de passos para cada incremento de temperatura
# }

## Quando alcançar a temperatura final, estabilizar nela
#langevinTemp $temperature_final
#run 1000 



