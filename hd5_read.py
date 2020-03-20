import h5py
import tables
import numpy as np


dfile_path='./data/development_sample_dataset_speaker.hdf5'
efile_path='./data/enrollment-evaluation_sample_dataset.hdf5'

with h5py.File(dfile_path, 'r') as f:
    print('development_sample_dataset_speaker')
    for item in f.keys():
        print ('main key is: {}'.format(item))
        print(f[item].shape)
        print(f[item].dtype)
        # content = f[item][:]
        # print ('key value of {0} is: {1}'.format(item,content))

with h5py.File(efile_path, 'r') as f:
    print('enrollment-evaluation_sample_dataset')
    for item in f.keys():
        print ('main key is: {}'.format(item))
        print(f[item].shape)
        print(f[item].dtype)


# Load the sample artificial dataset
fileh = tables.open_file(dfile_path, mode='r')
filec = tables.open_file(efile_path, mode='r')
##################################
######### Check dataset ##########
##################################

# Train
print("Train data shape:", fileh.root.utterance_train.shape)
print("Train label shape:", fileh.root.label_train.shape)
cc=fileh.root.utterance_train[:]
cc=np.transpose(cc[:,:,:,:],axes=(0,3,1,2))
ll=[ cc[0][:][:][i] for  i in range(0,20)]
label_train=fileh.root.label_train[:]
tran_data=fileh.root.utterance_train[0]
# Test
print("Test data shape:", fileh.root.utterance_test.shape)
print("Test label shape:",fileh.root.label_test.shape)
label_test=fileh.root.label_test[:]
test_data=fileh.root.utterance_test[:]
test_data=np.transpose(test_data[:,:,:,:],axes=(0,3,1,2))
jj=[ test_data[0][:][:][i] for  i in range(0,20)]
print('aa')



label_enrollment=filec.root.label_enrollment[:]
label_evaluation=filec.root.label_evaluation[:]


print('cc')






pass





pass
















