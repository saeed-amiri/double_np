"""All the constant values use in the silanization"""

import typing
import sys
import os

SOURCE_DIR: str  # SOURCE OF THE DATA FILES
SOURCE_DIR = '/scratch/saeed/MyScripts/np_silica/data'


class Constants:
    """The constants which are used in the script"""
    # The desire coverage for grafting on NP
    Coverage: float = 10
    # The thickness of the shell from surface to look for Si atoms
    Shell_radius: float = 6.0
    # calculate the level ups for Aminopropyl
    OM_n: int = 4  # Number of extra atoms (Si, OM) in aminopropyl
    Amino_OM: int = 3  # The default numbers of OM in the amino file
    # Silicon name in Aminopropyl file:
    SI_amino: str = 'SI'
    # OM name in Aminopropyl file:
    OM_amino: str = 'OM'
    # total number of atoms in aminoproyl file
    Num_amino: int = 17
    # Length of the ODAP is around 10.9372292106925 but I set to 11
    ODA_length: float = 11


class Hydration:
    """set all the info for water box
    Limitation for the box are added to the maximum radius of the NP"""
    # Forcefield type:
    FFIELD: str = 'charmm'
    TOLERANCE: float = 2.0
    # Check and delete files if they are exsit, True -> check and delete
    CHECK_WATER_PDB: bool = False
    # Contact angle, it defeins how much of the nanoparticle should be
    # in the oil phase, in case there is oil phase the APTES on the oil
    # phase are unprotonated
    CONATCT_ANGLE: float = 90  # In degree; If negetive -> no oil, MAX depends!
    # Box dimensions
    # x
    X_MIN: float = -75.0
    X_MAX: float = 75.0
    # y
    Y_MIN: float = -75.0
    Y_MAX: float = 75.0
    # z
    Z_MIN: float = -85.0
    Z_MAX: float = 85.0
    # Constants
    WATER_DENSITY = 0.9998395  # g/ml
    WATER_MOLAR_MASS: float = 18.01528  # g/mol
    OIL_DENSITY = 0.730  # g/ml for Decane (D10)
    OIL_MOLAR_MASS: float = 142.286  # g/mol for Decane (D10)
    AVOGADRO: float = 6.0221408e+23  # 1/mol
    MASSES: dict[str, float] = {'HW': 1.0080,
                                'OW': 15.9994,
                                'OH': 15.9994,
                                'OR': 15.9994,
                                'CL': 35.453,
                                'NA': 22.989769,
                                'H': 1.00080,
                                'C': 12.011,
                                'N': 14.0067,
                                'POT': 39.0983,
                                'CLA': 35.453}
    # Water charges
    # Type of each water model
    WATER_CHARGE: dict[str, dict[str, float]]
    NA_Q: int = +1  # Charge of the na ion
    CL_Q: int = -1  # Charge of the cl ion
    WATER_MODEL: str = 'charmm'  # The model to use in system
    WATER_CHARGE = {'tip3p': {'OW': -0.834,
                              'HW1': 0.417,
                              'HW2': 0.417,
                              'NA': NA_Q,
                              'CL': CL_Q},
                    'spce': {'OW': -0.8476,
                             'HW1': 0.4238,
                             'HW2': 0.4238,
                             'NA': NA_Q,
                             'CL': CL_Q},
                    'spc': {'OW': -0.82,
                            'HW1': 0.41,
                            'HW2': 0.41,
                            'NA': NA_Q,
                            'CL': CL_Q},
                    'tip4p': {'OW': 0.0,
                              'HW1': 0.52,
                              'HW2': 0.52,
                              'MW': -1.04,
                              'NA': NA_Q,
                              'CL': CL_Q},
                    'charmm': {'OH2': 0.0,
                               'H1': 0.52,
                               'H2': 0.52,
                               'POT': NA_Q,
                               'CLA': CL_Q}
                    }
    # PACKMOL files

    WATER_PDB: str = os.path.join(SOURCE_DIR, 'water_charmm.pdb')
    ODAP_PDB: str = os.path.join(SOURCE_DIR, 'ODAp_charmm.pdb')
    ODAN_PDB: str = os.path.join(SOURCE_DIR, 'ODAn_charmm.pdb')
    NA_PDB: str = os.path.join(SOURCE_DIR, 'POT.pdb')
    CL_PDB: str = os.path.join(SOURCE_DIR, 'CLA.pdb')
    OIL_PDB: str = os.path.join(SOURCE_DIR, 'D10.pdb')
    ADD_ION: bool = False  # if True it will add the ion to the itp file
    NA_ITP: str = os.path.join(SOURCE_DIR, 'Na.itp')
    CL_ITP: str = os.path.join(SOURCE_DIR, 'Cl.itp')
    ODAP_ITP: str = os.path.join(SOURCE_DIR, 'ODAp_charmm.itp')
    ODAN_ITP: str = os.path.join(SOURCE_DIR, 'ODAn_charmm.itp')
    OIL_ITP: str = os.path.join(SOURCE_DIR, 'D10_charmm.itp')
    INP_FILE: str = 'water_box.inp'
    OUT_FILE: str = 'water_box.pdb'
    WS_INP: str = 'water_silica.inp'  # Input for final water & silanized file
    GRO_PDB: str = 'silica_water.pdb'  # File for GROMACS input
    # PACKMOL lib
    PACKMOL: str = '/home/saeed/Downloads/packmol/packmol'
    # Number or concentration of ODAP and ODAN (in case later wanted)
    # It is used in the write_water and lmp_itp_pdb
    # protonation of ODA in water:
    # If you want the ODA in water to
    # be protonated, set ODAP_PROTONATION to True, and the script will
    # use the data from ODAP. However, remember to set the number of
    # ODA in water still using N_ODAP. The script will select the file
    # based on the protonation state in ODAP_PROTONATION, and N_ODAN
    # should only be used if you want the ODA in the oil phase.
    ODAP_PROTONATION: bool = True
    N_ODAP: int = 50  # Protonated ODA will add to water section
    N_ODAN: int = 0  # Unprotonated ODA will add to if oil section
    # If the protonated ODA should be at the interface at the beginning,
    # set the following to INTERFACE or if they shoud be in the edge of
    # the oil phase set it to `OILDOWN` and in water edge put it to
    # `WATERTOP`:
    ODAP_INTERFACE: str = 'WATERTOP'
    # Salt (NaCl) parameters
    # Need a tuple type of concentration or molality
    # For now it only support molality
    # Molal: Containing one mole of solute per kilogram of solvent.
    # Molal should be in `MILIMOLAL`:  millimoles per kg !!!
    N_NACL: dict[str, typing.Any]  # Type of concenteration and amount
    N_NACL = {'sty': 'mmolal', 'sum': 0}


class NanoParticles:
    """information about the nanoparticles
    For each nanoparticle the radius and its source of the file.
    SEPERATION is the info for seperation distance between nanoparticles
    and where they should set; if 'center' the midpoint between the
    particles will be set at 0 0 0.
    """
    if len(sys.argv) < 3:
        sys.exit("\n\t\tCheck the inputs, need two PDB files, Exit!\n")
    NP_DICT: dict[str, dict[str, typing.Any]] = {
        'NP1' : {'source': sys.argv[1]},
        'NP2' : {'source': sys.argv[2]},
        'SEPERATION' : {'distance': 10, 'origin': 'center'}
    }


class PosRes:
    """write the psition restrians for atoms in the core of the silica
    nanoparticels"""
    RESTRINS_GROUP: list[str] = ['COR', 'SIL']
    RESTRINS_ATOMS: list[str] = ['SD', 'SI', 'SU']
    POSRES: bool = True  # if want to write it: True
    RES_FILE: str = 'STRONG_POSRES.itp'
    FUNCTION: int = 1  # Type of the function for the restrains
    FX: int = 1000  # Force along x axis
    FY: int = 1000  # Force along y axis
    FZ: int = 5000  # Force along z axis


class GroInp:
    """info for writing inputs for the gromacs input"""
    FORCEFIELD: str = '../../force_field/charmm36_silica.itp'
    WATERITP: str = '../../force_field/TIP3.itp'
    IONITP: str = '../../force_field/CLA.itp'
    TOPFILE: str = 'topol.top'
    NPPOSRES: bool = True  # True if want to set the restraints on NP
    WATERPOSRES: bool = False  # True of want to set restraints on NP
