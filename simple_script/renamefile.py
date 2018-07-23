import os,re
import glob

os.chdir(r'F:\迅雷下载\[VCB-Studio] KonoSuba\[VCB-Studio] Kono Subarashii Sekai ni Shukufuku wo! [Ma10p_1080p]')

def rename():
    li=glob.glob('*.sc.ass')
    pattern = re.compile(r'(\[\d{2}\])',re.DOTALL)
    for i in li:
        matched=pattern.search(i)
        if matched:
            new = matched.group(1)
            sub = f'[VCB-Studio] Kono Subarashii Sekai ni Shukufuku wo! {new}[Ma10p_1080p][x265_flac_aac].ass'
            print(sub)
            os.rename(i, sub)


def del_name():
    li = glob.glob('*.tc.ass')
    for i in li:
        print(i)
        os.remove(i)

