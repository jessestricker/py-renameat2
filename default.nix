{
  pkgs ? import <nixpkgs> { },
}:
let
  inherit (pkgs) lib python3Packages;
  pyprojectToml = lib.importTOML ./pyproject.toml;
in
python3Packages.buildPythonPackage {
  pname = pyprojectToml.project.name;
  version = pyprojectToml.project.version;
  pyproject = true;

  src = lib.sourceFilesBySuffices ./. [
    "toml"
    "py"
  ];

  build-system = with python3Packages; [
    cffi
    setuptools
  ];
  dependencies = with python3Packages; [
    cffi
  ];
  nativeCheckInputs = with python3Packages; [
    pytestCheckHook
  ];

  pythonImportsCheck = [ "renameat2" ];
}
