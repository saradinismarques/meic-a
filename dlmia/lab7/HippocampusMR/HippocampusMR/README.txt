Learn2Reg Dataset v1.1
______________________

Thank you for working with our "Learn2Reg" Dataset. This dataset was created for the Learn2Reg Challenge. 
Currently, we combine 5 tasks in this dataset:

- AbdomenCTCT
- AbdomenMRCT
- HippocampusMRMR
- LungCT
- OASIS
- CurIOUS
- NLST

For more information on Learn2Reg, see https://learn2reg.grand-challenge.org/ and https://learn2reg-test.grand-challenge.org/.
If you use any of our data, please cite the source noted in each [TASKNAME]_dataset.json as well as https://arxiv.org/abs/2112.04489 (currently in submission).
______________________
Data structure
Each task uses the following data structure:

[TASKNAME]
+-- [TASKNAME]_dataset.json
+-- imagesTr
¦   +-- [TASKNAME]_0001_0000.nii.gz
¦   +-- [TASKNAME]_0001_0001.nii.gz
¦   +-- [TASKNAME]_1000_0000.nii.gz
¦   +-- [TASKNAME]_1001_0000.nii.gz
¦   +-- ...
+-- *imagesTs
¦   +-- *[TASKNAME]_0030_0000.nii.gz
¦   +-- *[TASKNAME]_0030_0001.nii.gz
¦   +-- *[TASKNAME]_0031_0000.nii.gz
¦   +-- *[TASKNAME]_0031_0001.nii.gz
¦   +-- *...
+-- labelsTr
¦   +-- [TASKNAME]_0001_0000.nii.gz
¦   +-- [TASKNAME]_0001_0001.nii.gz
¦   +-- [TASKNAME]_1000_0000.nii.gz
¦   +-- [TASKNAME]_1001_0000.nii.gz
¦   ¦   +-- ...
+-- *labelsTs
¦   +-- *[TASKNAME]_0030_0000.nii.gz
¦   +-- *[TASKNAME]_0030_0001.nii.gz
¦   +-- *[TASKNAME]_0031_0000.nii.gz
¦   +-- *[TASKNAME]_0031_0001.nii.gz
¦   +-- *...
+-- landmarksTr
¦   +-- [TASKNAME]_0001_0000.csv
¦   +-- [TASKNAME]_0001_0001.csv
¦   +-- [TASKNAME]_1000_0000.csv
¦   +-- [TASKNAME]_1001_0000.csv
¦   +-- ...
+-- *landmarksTs
¦   +-- *[TASKNAME]_0030_0000.csv
¦   +-- *[TASKNAME]_0030_0001.csv
¦   +-- *[TASKNAME]_0031_0000.csv
¦   +-- *[TASKNAME]_0031_0001.csv
¦   +-- *...
+-- keypointsTr
¦   +-- [TASKNAME]_0001_0000.csv
¦   +-- [TASKNAME]_0001_0001.csv
¦   +-- [TASKNAME]_1000_0000.csv
¦   +-- [TASKNAME]_1001_0000.csv
¦   +-- ...
+-- *keypointsTs
¦   +-- *[TASKNAME]_0030_0000.csv
¦   +-- *[TASKNAME]_0030_0001.csv
¦   +-- *[TASKNAME]_0031_0000.csv
¦   +-- *[TASKNAME]_0031_0001.csv
¦   +-- *...
+-- masksTr
¦   +-- [TASKNAME]_0001_0000.nii.gz
¦   +-- [TASKNAME]_0001_0001.nii.gz
¦   +-- [TASKNAME]_1000_0000.nii.gz
¦   +-- [TASKNAME]_1001_0000.nii.gz
¦   ¦   +-- ...
+-- *masksTs
    +-- *[TASKNAME]_0030_0000.nii.gz
    +-- *[TASKNAME]_0030_0001.nii.gz
    +-- *[TASKNAME]_0031_0000.nii.gz
    +-- *[TASKNAME]_0031_0001.nii.gz
    +-- *...

[TASKNAME]		:name of task, e.g. AbdomenMRCT

For further information about image pairings, modalities, labels, data shape, etc. please see the corresponding [TASKNAME]_dataset.json

Following files and folders may be present:
images[Tr/Ts]   :training/testing images. Paired images inside one modality (e.g. exhale/inhale images) are denoted by consecutive suffix numbering (e.g. _0000.nii.gz and _0001.nii.gz). Paired images in different modalities are denoted in [TASKNAME]_dataset.json
labels[Tr/Ts] 	:training/testing labels. A description of task-specific labels can be found in [TASKNAME]_dataset.json
landmarks[Tr/Ts]:training/testing landmarks. Landmarks may be used for validation and testing the accuracy of your algorithm
keypoints[Tr/Ts]:training/testing keypoints. Keypoints have been created using corrfield (please see our github repository for futher information: https://github.com/MDL-UzL/L2R )
masks[Tr/Ts] 	:training/testing masks. Boolean masks exlclude image areas not considered in registration evaluation.
[TASKNAME]_dataset.json : All task- and dataset specific information.

Please note that files and directories denoted with "*" are part of the testset will not be released.


