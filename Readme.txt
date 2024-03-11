--------------------------------------
Dataset of Perceived Intoxicated Faces
--------------------------------------


The Dataset contains 4,658 and 1,769 face videos for the intoxicated and sober categories, respectively.
Each face video duration is 10 seconds(Frame rate 24) whereas the audio information corresponding to each face video could be of different duration.

This shared folder contains four type of features extracted from the face videos(and their corresponding audio information) and the CSV file for the train/Val/test split information. 


--------------------------------------
--------------------------------------
Features Description
--------------------------------------
--------------------------------------
There are four zip files named opensmile,open_chunks,open_chunks2 and vgg_face7. Each zip contains .npy files for the extracted features from the face_video.

---------------------------------------
opensmile
---------------------------------------
In this folder, audio features extracted from opensmile library are stored for audio information corresponding to each face video. For each face video, a feature of dimension 1582 is stored in .npy file.

Features dimension-1582

---------------------------------------
open_chunks
---------------------------------------
Instead of extracting audio features for whole audio, each audio file is broken into 76 chunks with an overlap of 50ms. 

Feature Dimension -[76,1582]

---------------------------------------
open_chunks2
---------------------------------------
Each audio file is divided into chunks of 75 ms with an overlap of 30ms.  

Feature Dimension: [Variable,1582]

---------------------------------------
vgg_face7
---------------------------------------
Alternate frames of face video are passed through VGG_face network and features extracted from fc7 layer(Output_dim 4096).

Features Dimension:[120,4096]




--------------------------------------
--------------------------------------
Train/val/test split
--------------------------------------
--------------------------------------

'train_test_sets' contains 10 sets of 5 cross validation. Each set contains five csv files. Each csv file containing split information. 


--------------------------------------
If you find this work useful for your research, please consider citing our work:
--------------------------------------
@inproceedings{mehta2019dif,
  title={DIF: Dataset of Perceived Intoxicated Faces for Drunk Person Identification},
  author={Mehta, Vineet and Katta, Sai Srinadhu and Yadav, Devendra Pratap and Dhall, Abhinav},
  booktitle={2019 International Conference on Multimodal Interaction},
  pages={367--374},
  year={2019},
  organization={ACM}
}

--------------------------------------
For more details
---------------------------------------
1. Vgg_face model used: https://gist.github.com/EncodeTS/6bbe8cb8bebad7a672f0d872561782d9
2. opensmile library: https://www.audeering.com/opensmile/
3. DIF website: https://sites.google.com/view/difproject/home
