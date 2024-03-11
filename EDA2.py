import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv('dataset.csv')
print(df['set'].value_counts())

train_df = df[df['set'] == 'train']
test_df = df[df['set'] == 'test']
val_df = df[df['set'] == 'val']

print(train_df.head())


video_frames = np.load('vgg_face7/DRUNK REACTION - Doctor Who Christmas Special - The Return Of Doctor Mysterio - YouTube.MP4_12_149.mp4_aligned_1.npy')
plt.imshow(video_frames)
plt.show()

for frame in video_frames:
    plt.imshow(frame)
    plt.show()