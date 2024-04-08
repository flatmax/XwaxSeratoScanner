#!/usr/bin/env python3

import sys
from SeratoData import SeratoData
from Entry import Entry

seratorData = SeratoData()
# list = crate.loadcrate('../_ScratchLIVE_/Subcrates/bhangra.crate')
# list = crate.loadcrate('../_ScratchLIVE_/Subcrates/hip hop.crate')
list = seratorData.loadFile('/home/flatmax/xwax/_ScratchLIVE_/database V2')
# list = seratorData.loadFile(sys.argv[1])

# for item in list:
#     print(item[0])
#     print(item)
#     for dat in item:
#         print(dat)
# print(list[1][1])

files = {}
for item in list:
# for its in range(0, 3):
#     item = list[its]
    e = Entry(item)
    fn = e.getFileName()
    if fn != None:
        # files[fn] = e.getXwaxFormat()
        e.printXwaxFormat()

# print(files)
# for f in files:
#     print(f)
# #     print('')
