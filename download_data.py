from proteinshake.datasets import SCOPDataset
from proteinshake.utils import protein_to_pdb
from tqdm import tqdm

dataset = SCOPDataset()
proteins = dataset.proteins(resolution='atom')
labels = {'train':{}, 'val':{}, 'test':{}}
tqdm_bar = tqdm(total=len(proteins))
for i, protein in enumerate(proteins):
    split = protein['protein']['random_split']
    id = protein['protein']['ID']
    labels[split][id] = protein['protein']['SCOP-CL']
    protein_to_pdb(protein, f'./data/SCOP/{split}/{id}.pdb')
    tqdm_bar.update(1)
tqdm_bar.close()


