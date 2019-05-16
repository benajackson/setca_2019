#This is my geometry analysis code
"""
Functions and script for geometry analysis.
"""
import numpy
import os
import sys

def calculate_distance(atomA,atomB):
    """
    Calculate the distance between two atoms.
    Paramaters
    ----------
    atom1:list
        A list of coordinates[x, y, z]
    atom2:list
        A list of coordinates[x, y, z]

    Returns
    -------
    bond_length: float
        The distance between atoms.

    Examples
    --------
    >>> calculate_distance([0,0,0],[0,0,1])
    1.0
    """
    x_distance = atomA[0]-atomB[0]
    y_distance = atomA[1]-atomB[1]
    z_distance = atomA[2]-atomB[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(bond_distance,minimum_value=0,maximum_value=1.5): #Equals set the defaults, anything without equals user must spec
    """
    Check if distance is a bond.

    Paramaters
    ----------
    bond_distance: float
        The distance between atoms
    minimum_value: float
        The minimum distance for a bond.
    maximum_value
        The maximum distance for a bond.

    Returns
    -------
    True if bond
    True if not a bond
    """

    #Check that atom_distance is a flaot
    if not isinstance(bond_distance, float):
        raise TypeError(F'Atom distance must be type float. {bond_distance}')
    if bond_distance>minimum_value and bond_distance<maximum_value:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv)<2:
        raise IndexError('No file specified. Script Requires an xyz file')
    xyz_location = sys.argv[1]
    xyz_file = numpy.genfromtxt(fname=xyz_location, skip_header=2, dtype='unicode')
    symbols=xyz_file[:,0]
    coordinates=xyz_file[:,1:]
    coordinates = coordinates.astype(numpy.float)

    for numA, atomA in enumerate(coordinates):
        for numB, atomB in enumerate(coordinates):
            if numB<numA:
                distance_AB = calculate_distance(atomA, atomB)
                if bond_check(distance_AB,0,1.5):
                    print(F'{symbols[numA]} to {symbols[numB]}: {distance_AB:.3f}')
