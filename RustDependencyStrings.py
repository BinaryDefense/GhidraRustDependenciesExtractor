# Extracts Rust crate dependency strings from a compiled Rust binary.
# @author Matt Ehrnschwender
# @category Search

import re
import string
import struct

from ghidra.program.database import *

unsigned_convert = lambda x: struct.unpack("B", struct.pack("b", x))[0]

regex_string = (
    r".cargo(/|\\)registry(/|\\)src(/|\\).*?-[a-f0-9]{16}(/|\\)(.*?\d+.\d+.\d+)"
)

initialized_sections = filter(
    lambda x: x.isInitialized(), currentProgram.getMemory().getBlocks()
)

rw_sections = filter(lambda x: x.getPermissions() & 1 == 0, initialized_sections)

string_data = ""
for section in rw_sections:
    raw_bytes = [unsigned_convert(x) for x in section.getData().readAllBytes()]
    printable_bytes = [chr(x) for x in raw_bytes if chr(x) in string.printable]
    string_data += "".join(printable_bytes)

matches = sorted(set(re.findall(regex_string, string_data)))

if len(matches) > 0:
    for match in matches:
        print(match[-1])
else:
    print("No Rust crate dependency strings found.")
