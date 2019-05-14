import h5py as h
#import matplotlib.pyplot as plt

# Read the master file
f = h.File('/global/cscratch1/sd/jderose/BCC/Chinchilla/Herd/Chinchilla-3/sampleselection/Y3/Y3_mastercat_w_y3rmg_b3_v1.9.2.h5', 'r')
#('/global/cscratch1/sd/troxel/cats_des_y3/Y3_mastercat_v2_6_20_18_subsampled.h5', 'r')
print '\nLoading mastercat: ',f,'\n'

# Check the available file/catalogs
print 'Available files: \n', f.keys(), '\n'

# Now, focusing on 'catalog', lets read the available catalogs:
print 'Available catalogs in catalog: \n', f['catalog'].keys(), '\n'

# --- Reading metacal
print '-'*80 + ' Metacal ' + '-'*80 +'\n'
print '- Loading catalog/metacal: ', f['catalog/metacal'], '\n'

# Sub-catalogs from metacal: 
print 'Available catalog/metacal sub-catalogs: \n', f['catalog/metacal'].keys(), '\n'

# Finally, the columns from each metacal sub-catalog 
print 'Columns in catalog/metcal/unsheared: \n', f['catalog/metacal/unsheared'].keys(), '\n'

#reading gold 
print '-'*80 + ' Gold ' + '-'*80 +'\n'
print 'Loading catalog/gold: ', f['catalog/gold'], '\n'

# Columns from gold
print 'Columns in catalog/gold: \n', f['catalog/gold'].keys(), '\n'

# --- Reading bpz
print '-'*80 + ' BPZ ' + '-'*80 +'\n'
print 'Loading catalog/bpz: ', f['catalog/bpz'], '\n'

# Sub-catalogs bpz
print 'Available catalog/bpz sub-catalogs: \n', f['catalog/bpz'].keys(), '\n'

# Finally, the columns from each bpz sub-catalog 
print 'Columns in catalog/bpz/unsheared: \n', f['catalog/bpz/unsheared'].keys(), '\n'

# --- Reading redmagic
print '-'*80 + ' redmagic ' + '-'*80 +'\n'
print 'Loading catalog/redmagic: ', f['catalog/redmagic'], '\n'

# Sub-catalogs redmagic
print 'Available catalog/redmagic sub-catalogs: \n', f['catalog/redmagic'].keys(), '\n'

# Finally, the columns from each redmagic sub-catalog 
print 'Columns in catalog/redmagic/combined_sample_fid: \n', f['catalog/redmagic/combined_sample_fid'].keys(), '\n'
print 'Columns in catalog/redmagic/highdens: \n', f['catalog/redmagic/highdens'].keys(), '\n'
print 'Columns in catalog/redmagic/higherlum: \n', f['catalog/redmagic/higherlum'].keys(), '\n'
print 'Columns in catalog/redmagic/highlum: \n', f['catalog/redmagic/highlum'].keys(), '\n'

# --- Reading redmapper
print '-'*80 + ' redmapper ' + '-'*80 +'\n'
print 'Loading catalog/redmapper: ', f['catalog/redmapper'], '\n'

# Sub-catalogs redmapper
print 'Available catalog/redmapper sub-catalogs: \n', f['catalog/redmapper'].keys(), '\n'

# Finally, the columns from each redmapper sub-catalog 
print 'Columns in catalog/redmapper/lgt5: \n', f['catalog/redmapper/lgt5'].keys(), '\n'
print 'Columns in catalog/redmapper/lgt20: \n', f['catalog/redmapper/lgt20'].keys(), '\n'
