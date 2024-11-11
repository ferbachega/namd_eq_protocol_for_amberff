# 7. Reduce the backbone restraint force
# Relaxation for 1 ns of simulation time at a constant pressure with 
# restraints on the backbone lowered to 1 kcal/mol•Å2.

# input
#-----------------------------------------------------------------------
amber                           yes    
parmfile                        sys.prmtop                                              
ambercoor                       sys.crd                                                 
#coordinates                     C13-7Leu_sys_revisado.pdb

binCoordinates output_06.coor
binVelocities  output_06.vel
extendedSystem output_06.xsc
#-----------------------------------------------------------------------

# run_steps = 1000000  --> 1 ns (default)
set run_steps                   10000


# Output                                                 
#-----------------------------------------------------------------------
outputName                      output_07                          
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
constraintScaling 1.0         ;# Optional scaling factor for the constraints

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


run $run_steps

