"""
The scripts obtain the required residues and organize the input for
Packmol.
To achieve this, the input must include the dimensions of the overall
box containing both nanoparticles and the source files for each
residue. The center point between the two nanoparticles will be set at
coordinates (0 0 0).
"""

import logger
import box_dimensions


if __name__ == '__main__':
    box_dimensions.BoxEdges(25, 10, log=logger.setup_logger('box_dims.log'))
