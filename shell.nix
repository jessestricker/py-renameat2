{
  pkgs ? import <nixpkgs> { },
}:
let
  self = import ./. { inherit pkgs; };
in
pkgs.mkShell {
  inputsFrom = [ self ];
  packages = with pkgs; [
    ruff
  ];
}
