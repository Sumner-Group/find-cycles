# find-cycles
This is python3/Jupyter Notebook code that utilizes the NetworkX package (https://networkx.github.io/) to locate cyclic structures within an MD simulation. Specifically, it was written to find cyclical N-mers in an MD simulation of liquid methanol. However, it should work for any hydrogen-bonding solvent.

This script requires the following arguments (arguments in [] are optional):
    
   \<InputFile> \<OutputFile> \<# Molecules> \<Name of residue> \<Name of oxygen> \<Name of hydrogen> [distance cutoff (Ang)] [angle cutoff (deg)] [max number of molecules in a cycle]
   
   Default values for optional arguments are: [distance cutoff]=3.2 [angle cutoff]=130 [max number of molecules in a cycle]=10
  
  Currently, the InputFile must be a PDB.
