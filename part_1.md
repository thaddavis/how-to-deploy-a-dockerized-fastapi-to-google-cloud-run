# Part 1

## Prereqs

- https://www.docker.com/get-started/
- https://www.docker.com/products/docker-desktop/
- https://code.visualstudio.com/download
    - `code --install-extension ms-azuretools.vscode-docker`
    - `code --install-extension ms-vscode-remote.remote-containers`

## Follow along

1. `mkdir .devcontainer`
2. `touch .devcontainer/devcontainer.json`
3. Open the `.devcontainer/devcontainer.json` file
4. `touch Dockerfile.dev`
5. Open the `Dockerfile.dev` file
6. Go to VSCode Command Palette (ie: SHIFT + CMD + P)
    - Dev Containers: Reopen in Container
7. SMOKE TEST the "Dev Container"
    - `git version` -> 2.39.2
    - `curl --version` -> 7.88.1
    - `python --version` -> 3.12.3
    - `cat /etc/os-release` -> Debian GNU/Linux

## Reference links

- https://containers.dev/implementors/json_reference/
- https://code.visualstudio.com/docs/devcontainers/containers
- https://hub.docker.com/_/python
