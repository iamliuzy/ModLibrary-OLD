#  ModLibrary, a Minecraft mod manager.
#  Copyright (C) 2023 iamliuzy
#
#  This file is part of ModLibrary.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#   any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see https://www.gnu.org/licenses/.

from pathlib import PurePath
import jsonparse
import zipfile
import tempfile
import toml
import log
import constants
from os.path import abspath


class ModFile(object):
    """
    Object for a Minecraft Mod File.
    Attributes:
        loader: 0: Forge old Loader
                1: Forge new Loader
                2: Fabric Loader
        path: Absolute path to the mod file.
        file: ZipFile instance of the mod jar file.
        manifest_dict: Jar manifest file(META-INF/MANIFEST.MF) stored in dict form.
        metadata: Mod info file("META-INF/mods.toml" for Forge new, "mcmod.info" for Forge old and "fabric.mod.json" for
                  Fabric loader) stored in dict form.

    Args:
        path: Path to the mod file.
    """

    def __init__(self, path: PurePath):
        self.path = abspath(path)
        self.file = zipfile.ZipFile(self.path, mode="r")
        with tempfile.TemporaryDirectory() as tempdir:
            jar_manifest = self.file.extract("META-INF/MANIFEST.MF", tempdir)
            self.manifest_dict = jsonparse.ManifestAccess.manifest_to_dict(jar_manifest)
        #   try:
            extracted = self.file.extract("META-INF/mods.toml", tempdir)
            self.metadata = toml.load(extracted)
            self.loader = 1  # Forge new loader
        # These codes will be uncommented soon.
        #   except KeyError:
        #       try:
        #           extracted = self.file.extract("mcmod.info", tempdir)
        #           self.metadata = jsonparse.QuickAccess.json_to_list(extracted)
        #           self.loader = 0  # Forge old loader
        #       except KeyError:
        #           extracted = self.file.extract("fabric.mod.json", tempdir)
        #           self.metadata = jsonparse.QuickAccess.json_to_dict(extracted)
        #           self.loader = 2  # Fabric loader
        if self.loader == 1:
            try:
                self.name = str(self.metadata["mods"][0]["displayName"])
                self.id = str(self.metadata["mods"][0]["modId"])
                self.dependencies = list(self.metadata["dependencies"][self.id])
                self.version = str(self.metadata["mods"][0]["version"])
                self.url = str(self.metadata["mods"][0]["displayURL"])
                self.issue_url = str(self.metadata["issueTrackerURL"])
                self.description = str(self.metadata["mods"][0]["description"])
            except KeyError as e:
                log.warn(str(e) + ' key does not exist in the mod info file of mod "' + str(self.path) + '".')
            if self.version == "${file.jarVersion}":
                # Some mods may use ${file.jarVersion} to
                # refer to the version number in the manifest
                ver = self.manifest_dict.get("Implementation-Version")
                if ver is not None:
                    self.version = ver
                else:
                    log.error('Cannot get version of mod "%s".' % self.name)
                    # If the program cannot find version in both place, output an error.
            for i in dir(self):  # Debug code. Will remove soon.
                if i[0] != "_":
                    log.debug(i + "::" + str(getattr(self, i)))


class Mod(object):
    files: list[ModFile]
    mod_id: str
    json: dict[str, str]

    def __init__(self, files: list[ModFile]):
        self.files = files
        self.mod_id = self.files[0].id
        self.name = self.files[0].name
        self.description = self.files[0].description
        self.json = {"id": self.mod_id, "name": self.name, }

    def __repr__(self) -> dict[str, str]:
        return self.json
