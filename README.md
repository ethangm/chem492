# chem492

Topology files (w/solvent and w/o solvent) are stored as .csv files. They can provide the index atom for each atom in trajectory.

Trajectory files are stored as .npy arrays. The trajectory w/ solvent is split up into 7 sub arrays starting with 0 s.t. each array starts with the next frame after where the previous array ended.
Shape of arrays are (frames, atoms in frame, xyz coordinates of each atom).

All data comes from CHANGED_PAR/ALA/TRAJ/AC/005/ala_1_md in original zenodo database
