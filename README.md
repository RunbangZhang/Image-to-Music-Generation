# Image-to-Music-Generation
This repo provides VIS2MUS, a multimodal generation tool that generates music via visual control. 
The visual control provided include: brightness adjustment, contrast adjustment and style transfer. It is designed for people who love music and drawing to explore and create custom music, as well as to inspire and cultivate their synesthetic abilities.
Here is the paper to introduce the interface: https://arxiv.org/abs/2211.05543


## The tool interface is as shown below:
![Image from ISMIR_2022_Vis2Mus, page 6](https://github.com/RunbangZhang/Image-to-Music-Generation/assets/49141686/7fa3fb73-5732-4656-9c0f-fce05dda070c)

1⃝: Simple drawing (left) and style picture display area (right).

2⃝: Monotonic melody music (left) and polyphonic accompaniment music pianoroll and audio demonstration area (right).

3⃝: Image area after style transfer.

4⃝: Music area after style migration.

5⃝: Menu for simple drawings (upper left, lower left) and for style images (upper right).

6⃝: Style transfer button.

7⃝: Brightness slider (top), contrast slider (middle), and the apply button (bottom).

## Installation and startup

1. Default configurarion:
    - python >= 3.7
    -muspy==0.3.0
    -numpy==1.20.3
    - opencv_python==4.5.1.48
    - pandas==1.2.3
    - Pillow==8.4.0
    - pretty_midi==0.2.9
    -pygame==2.0.1
    -pypianoroll==1.0.4
    - PyQt5==5.15.6
    - quickdraw==0.2.0
    - tensorboardX==2.4.1
    -torch==1.8.1
    -matplotlib==3.4.1

2. Run `python3 main.py`. Then follow the **Instructions** section to play with it:)

## Instructions

### Select anchor point

1. Different simple drawings can be selected in the menu bar at the upper left of 5⃝, and three variations of this kind of simple drawings can be selected from the menu bar at the lower left of 5⃝.
2. 5⃝ Different style pictures can be selected in the menu bar on the upper right. The selected picture will be displayed in area 1⃝.
3. The music in area 2⃝ changes according to the selection in 5⃝. Click the **Play** and **Stop** buttons to play and stop music.

### Style Transfer

1. After determining the anchor point, the image after style transfer (fusion) will be immediately displayed in area 3⃝.
2. Use **stylize** button in 6⃝ to generate the fused music. See area 4⃝ for a demonstration of the fused music.

### Set brightness and contrast

1. Drag the Brightness/Contrast slider in 7⃝ to adjust the brightness/contrast of the style image and blended image. Use **Reset** button to restore default settings.
2. Use **Enhance** button in 7⃝ to apply brightness/contrast changes to polyphonic accompaniment and fusion music.


## Related data info

Stored in the **resources** directory:

- [344content-img](../Vis2Mus/resources/344content-img) contains 344 simple drawings.
- [344content_music ](../Vis2Mus/resources/344content_music ) contains 344 pieces of monotonous melody music.
- [style_img](../Vis2Mus/resources/style_img) contains 13 style pictures.
- [style_music](../Vis2Mus/resources/style_music) contains 13 style music.
- [344syn_img](../Vis2Mus/resources/344syn_img) contains 4472 fused images. It is the fusion result of 344 simple drawings and 13 style paintings.
- [content_img](../Vis2Mus/resources/content_img) contains 1032 simple drawings, corresponding to 3 variations of simple drawing of 344 objects.
- [content_music](../Vis2Mus/resources/content_music) contains 1032 melodies, corresponding to 3 variations of each of the 344 melodies.
- [syn_img](../Vis2Mus/resources/syn_img) contains 13416 fused images. It contains all of the fusion results between 1032 simple drawings and 13 style paintings.

