with import <nixpkgs> {};

  stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  venvDir = "./.VENV";
  buildInputs = [
    python38Full
    python38Packages.venvShellHook
    python38Packages.virtualenv

    python38Packages.click
    python38Packages.pandas
    python38Packages.pycairo
    python38Packages.spacy
    python38Packages.toolz

    python38Packages.jupyter
    python38Packages.matplotlib
  ];
  postShellHook = ''
    export PS1="\$(__git_ps1) $PS1"
    pip install -e ".[dev,doc]"
  '';
}
