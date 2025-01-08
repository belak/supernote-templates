{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    forAllSystems = nixpkgs.lib.genAttrs nixpkgs.lib.systems.flakeExposed;
  in {
    formatter = forAllSystems (system: nixpkgs.legacyPackages.${system}.alejandra);

    devShells = forAllSystems (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      default = pkgs.mkShell {
        packages = with pkgs; [
          python3
          poetry
          reflex
          inkscape
        ];

        env = {
          # Put the venv on the repo, so direnv can access it
          POETRY_VIRTUALENVS_IN_PROJECT = "true";
          POETRY_VIRTUALENVS_PATH = "{project-dir}/.venv";

          # Use python from path, so you can use a different version to the one bundled with poetry
          POETRY_VIRTUALENVS_PREFER_ACTIVE_PYTHON = "true";
        };
      };
    });
  };
}
