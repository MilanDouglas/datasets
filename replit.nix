#{ pkgs ? import <nixpkgs> {} }:
#pkgs.python38
{pkgs}: {
  deps = [
    pkgs.glibcLocales
    pkgs.sqlite
    pkgs.unzip
    pkgs.wget
  ];
}
