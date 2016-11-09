from conans import ConanFile, CMake
import os

class PlexMediaPlayer(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  requires = (
    "web-client-desktop/2.10.8-4bfce4e@plex/stable",
    "web-client-tv/2.10.8-864e6a4b@plex/stable"
  )
  
  def imports(self):
    self.copy("*", dst="web-client/tv", src="tv")
    self.copy("*", dst="web-client/desktop", src="desktop")