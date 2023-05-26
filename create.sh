#!/bin/sh
echo "Start create pdf"
git add .
nix build .#memoire-umons -L

echo "End of processus"
