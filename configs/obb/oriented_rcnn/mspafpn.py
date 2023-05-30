_base_ = './dcn.py'
model = dict(
    neck=
        dict(type='MSPAFPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        num_outs=5))