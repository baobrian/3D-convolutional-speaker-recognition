import h5py



dfile_path='./data/development_sample_dataset_speaker.hdf5'


efile_path='./data/enrollment-evaluation_sample_dataset.hdf5'






with h5py.File(efile_path, 'r') as f:
    for item in f.keys():
        print ('main key is: {}'.format(item))
        print(f[item].shape)
        print(f[item].dtype)
        content = f[item][:]
        print ('key value of {0} is: {1}'.format(item,content))



with h5py.File(efile_path, 'r') as f:
    for item in f.keys():
        print ('main key is: {}'.format(item))
        # content = f[item][:]
        # print ('key value of {0} is: {1}'.format(item,content))

pass