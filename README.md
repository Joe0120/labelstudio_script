# labelstudio_script

start backend
```
label-studio-ml start sam --port 8003 --with sam_config=vit_b sam_checkpoint_file=.\sam_vit_b_01ec64.pth out_mask=True out_bbox=True device=cuda:0

label-studio-ml start sam --port 8003 --with sam_config=vit_l sam_checkpoint_file=.\sam_vit_l_0b3195.pth out_mask=True out_bbox=True device=cuda:0
```