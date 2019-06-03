# find-cycles
This is python3/Jupyter Notebook code that utilizes the NetworkX package (https://networkx.github.io/) to locate cyclic structures within an MD simulation. Specifically, it was written to find cyclical N-mers in an MD simulation of liquid methanol, i.e. methanols hydrogen bonding to each other in a cycliccal fashion. However, it should work for any hydrogen-bonding solvent.

This script requires the following arguments (arguments in [] are optional):
    
   \<InputFile> \<OutputFile> \<# Molecules> \<Name of residue> \<Name of oxygen> \<Name of hydrogen> [distance cutoff (Ang)] [angle cutoff (deg)] [max number of molecules in a cycle]
   
   Default values for optional arguments are: [distance cutoff]=3.2 [angle cutoff]=130 [max number of molecules in a cycle]=10
  
  Currently, the InputFile must be a PDB.
  
  
  Included are input files (three frames of an MD simulation of 246 methaol molecules) and the output file. To generate the output, type:
  
    python3 cycle-test.py MeOH256-2frames.pdb  MeOH256-2frames.cycles  256 MOH O1 HO1

The output shows the molecule numbers invilved in the cycle, the number of molecules forming the cycle, the geometry (frame) number, and the total percent of molecules in a frame involved in the cycle.
