{ pkgs ? import <nixpkgs> {} }:

with pkgs;
stdenv.mkDerivation {
  name = "pyhton-dev";

  nativeBuildInputs = [
    python3
    python3Packages.pip
    python3Packages.virtualenv
  ];

  # ENV variables
  PROJDIR = "${toString ./.}";

  # Post Shell Hook
  shellHook = ''
    echo "Using ${python310.name}"

    [ ! -d '$PROJDIR/venv' ] && virtualenv venv
    source venv/bin/activate
    python -m pip install -r app/requirements.txt
  '';
}
