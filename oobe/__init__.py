import os.path

"""
Init program config files.
"""
for initfile in ["settings.json", "mods.json"]:
    f = open(os.path.abspath("..\\" + initfile), mode="x")
    f.close()
