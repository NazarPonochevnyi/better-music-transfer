import os

mp3 = True
mp3_rate = 320
model = "mdx_extra"
extensions = ["mp3", "wav", "ogg", "flac"]


def separate(in_path=None, out_path=None):
    if in_path is None or out_path is None:
        print("Specify in/out filenames!")
        return
    cmd = ["python", "-m", "demucs.separate", "-o", str(out_path), "-n", model]
    if mp3:
        cmd += ["--mp3", f"--mp3-bitrate={mp3_rate}"]
    command = ' '.join(cmd + [in_path])
    print(command)
    os.system(command)
