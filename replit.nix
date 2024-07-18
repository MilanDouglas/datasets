#{ pkgs ? import <nixpkgs> {} }:
#pkgs.python38
{pkgs}: {
  deps = [
    pkgs.tk
    pkgs.tcl
    pkgs.qhull
    pkgs.pkg-config
    pkgs.gtk3
    pkgs.gobject-introspection
    pkgs.ghostscript
    pkgs.freetype
    pkgs.ffmpeg-full
    pkgs.cairo
    pkgs.glibcLocales
    pkgs.sqlite
    pkgs.unzip
    pkgs.wget
  ];
}
