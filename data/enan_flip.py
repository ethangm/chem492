import MDAnalysis as mda
import numpy as np


# Load topology files
top_with_solv = mda.Universe("top.csv", "traj_sub_0.npy")
top_no_solv = mda.Universe("top_no_solv.csv", "traj_no_solv.npy")


# Create enantiomer by mirroring the coordinates
def create_enantiomer(coordinates):
   mirrored_coordinates = coordinates.copy()
   mirrored_coordinates[:, :, 0] *= -1  # Mirror x-coordinates
   return mirrored_coordinates


# Simulate enantiomers for all sub-arrays
for i in range(7):  # Assuming 7 sub-arrays
   # Extract coordinates from trajectory with solvent
   traj_with_solv = top_with_solv.trajectory[i]
   coordinates_with_solv = top_with_solv.atoms.positions


   # Create enantiomer coordinates
   coordinates_enantiomer = create_enantiomer(coordinates_with_solv)


   # Combine enantiomer coordinates with topology without solvent
   top_no_solv.atoms.positions = coordinates_enantiomer


   # Save enantiomer trajectory
   enantiomer_filename = f"enantiomer_traj_sub_{i}.npy"
   np.save(enantiomer_filename, top_no_solv.atoms.positions)


   print(f"Enantiomer trajectory {i} saved to {enantiomer_filename}")