import os,re
os.chdir(r'F:\迅雷下载\[TxxZ&A.I.R.nesSub][Psycho_Pass_2][BDRIP][Subtitles][chs+cht+jap]')
li=os.listdir('.')
pattern = re.compile(r'\[(\d{2})END\].{35}\.(\w{3})',re.DOTALL)
for i in li:
    matched=pattern.search(i)
    if matched:
        print(matched.groups())
        if matched.group(2) == 'chs':
            new=matched.group(1)
            sub='[VCB-Studio] PSYCHO-PASS II ['+new+'][Hi10p_1080p][x264_flac].ass'
            print(sub)
            os.rename(i,sub)
