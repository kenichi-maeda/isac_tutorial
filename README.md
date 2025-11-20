# isac_tutorial

[![Pre-commit](https://github.com/kenichi-maeda/isac_tutorial/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/kenichi-maeda/isac_tutorial/actions/workflows/pre-commit.yaml) [![Test](https://github.com/kenichi-maeda/isac_tutorial/actions/workflows/test.yaml/badge.svg)](https://github.com/kenichi-maeda/isac_tutorial/actions/workflows/test.yaml)


### Install Dependencies

If using Docker, install [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) and [Docker Compose](https://docs.docker.com/compose/install/linux/#install-using-the-repository) on the host system, and enter the container prior to running any commands with the following.

```bash
# Build and enter the container
bash scripts/develop-compose.bash
# For a new terminal, run "docker exec -it isac_tutorial_dev bash"
# To stop, run "docker compose down && sudo xhost -"
```

### Environment Entry and Configuration


Then, from within either the project parent folder or the Docker image home directory, run the following
to activate the environment(s).

```bash
pixi s  # Activate environment, add -e for specific env,
# Envs: gpu|ros2-gpu|ros2-cpu|genesis-gpu|genesis-ros2-gpu|isaaclab-gpu|isaaclab-ros2-gpu

# For ROS, run "colcon build" or "pixi r build-ros" to build the ros2_ws
# colcon build is auto-configured by ros2_ws/colcon-defaults.yaml
# To build your package, clone it into ros2_ws/src, and add its name to the colcon-defaults.yaml

# For Isaac Lab, do "pixi r install-isaaclab" to install all deps

# Genesis + Isaac Lab environments are still a bit flaky despite my best efforts ;(
```


## Testing and Linting

```bash
pixi run test  # Run with test environment
pixi run lint
```


## Acknowledgement

This repository was created from the [pixidock_template created by Gary Lvov](https://github.com/garylvov/pixidock_template), under fair use of the BSD 1-Clause License
