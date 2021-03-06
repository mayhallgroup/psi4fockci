import psi4
import psi4fockci
from psi4fockci import sf_cas

# threshold for value equality
threshold = 1e-7
# setting up molecule
n2 = psi4.core.Molecule.from_string("""
0 7
N 0 0 0
N 0 0 2.5
symmetry c1
""")

# Test: RAS(h)-1SF/CC-PVDZ with N2 (0,7 to 0,1)
def test_1():
  options = {"basis": "cc-pvdz", 'num_roots': 4, 'diis_start': 20}
  e = sf_cas( 0, 1, n2, conf_space="h", add_opts=options, localize=True )
  expected = -108.772041695171
  assert (e - expected) < threshold

