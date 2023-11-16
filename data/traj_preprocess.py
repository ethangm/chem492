import mdtraj as md
import numpy as np
import sys
import math


# have to load xtc file (trajectory) and corresponding pdb (topology)
def xtc_to_numpy(xtc_file: str, pdb_file: str) -> list:
    t = md.load(xtc_file, top=pdb_file)
    # format is (n frames, k atoms, xyz coords)
    # or n frames each with k atoms each with xyz coords

    # with topology, sort out only ala residue atoms from rest and track those?
    # or leave all in, but still sort residues?

    w_solv = np.array(t.xyz) # ?
    t_no_solv = t.remove_solvent()
    #t_no_solv.save_xtc("/home/ethangm2/chem492/no_solv_traj/no_solv.xtc")
    

    n_solv = np.array(t_no_solv.xyz)
    w_top = t.top.to_dataframe()[0]
    n_top = t.remove_solvent().top.to_dataframe()[0]

    return w_solv, n_solv, w_top, n_top


def inspect(xtc_file: str, pdb_file: str):
    t = md.load(xtc_file, top=pdb_file)
    print(t.top)
    print(next(t.top.residues))
    print(t.top.to_dataframe())


def split_numpy(np_file: str, num_splits: int=0):
    array = np.load(np_file)

    if num_splits == 0:
        print(array.shape)
        size = sys.getsizeof(array) / 1048576 # size in MB
        print("size of array:  " + str(size) + " MB")
        divs = math.ceil(size / 100)
        print("# of divisions: " + str(divs))
    else:
        sub_arrays = np.array_split(array, num_splits)

        temp = np_file.split(".")[0]
        for i, sub in enumerate(sub_arrays):
            print(sub.shape)
            name = temp + "_sub_" + str(i) + ".npy"
            np.save(name, sub)



if __name__ == "__main__":
    xtc = "../ZENODO/CHANGED_PAR/ALA/TRAJ/AC/005/ala_1_md.xtc"#chosen from top of files, not clear difference between 005, 0025, etc.
    pdb = "../ZENODO/CHANGED_PAR/ALA/TRAJ/AC/005/ala_1_md.pdb"
    arr = "traj.npy"

    #inspect(xtc, pdb)
    #split_numpy(arr, 7)

    '''
    w_solv, n_solv, w_top, n_top = xtc_to_numpy(xtc, pdb)
    
    print(w_solv.shape)
    print(w_solv[:10])
    print(n_solv.shape)
    print(n_solv[:10])

    np.save("traj.npy", w_solv)
    np.save("traj_no_solv.npy", n_solv)

    w_top.to_csv("top.csv", index=False)
    n_top.to_csv("top_no_solv.csv", index=False)
    '''