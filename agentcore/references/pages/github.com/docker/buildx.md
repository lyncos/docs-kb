---
title: Buildx
description: docker / **buildx** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/docker/buildx
fetched: '2026-09-26'
tags:
- agentcore
- github-com
- reference
- related
referenced_by:
- runtime-troubleshooting.md
conversion: pandoc
---

[docker](/docker) / **[buildx](/docker/buildx)** Public

- [Notifications](/login?return_to=%2Fdocker%2Fbuildx) You must be signed in to change notification settings

- [Fork 684](/login?return_to=%2Fdocker%2Fbuildx)

- [ Star 4.5k](/login?return_to=%2Fdocker%2Fbuildx)

[](/docker/buildx)

master

[Branches](/docker/buildx/branches)[Tags](/docker/buildx/tags)

[](/docker/buildx/branches)[](/docker/buildx/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[4,557 Commits](/docker/buildx/commits/master/)

[](/docker/buildx/commits/master/)4,557 Commits

## Folders and files

[TABLE]

## Repository files navigation

# Buildx

[](#buildx)

[![GitHub release](https://camo.githubusercontent.com/9ff3ea5b9e809e1d8c6818fd6005ef0d518f3369b9104a6d0617ff5b1f9492b7/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f646f636b65722f6275696c64782e7376673f7374796c653d666c61742d737175617265)](https://github.com/docker/buildx/releases/latest) [![PkgGoDev](https://camo.githubusercontent.com/b92bd49f755879826fbf8a9032e9966a79f3048d9305efd266584ea5ef6db264/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f676f2e6465762d646f63732d3030376439633f7374796c653d666c61742d737175617265266c6f676f3d676f266c6f676f436f6c6f723d7768697465)](https://pkg.go.dev/github.com/docker/buildx) [![Build Status](https://camo.githubusercontent.com/b6d11cee839d1cba058641c971855108c39adbdb7c892f9ad86b355814d95ccd/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f646f636b65722f6275696c64782f6275696c642e796d6c3f6272616e63683d6d6173746572266c6162656c3d6275696c64266c6f676f3d676974687562267374796c653d666c61742d737175617265)](https://github.com/docker/buildx/actions?query=workflow%3Abuild) [![codecov](https://camo.githubusercontent.com/e51e16a7dd274f15ceb7c14285d2b43b51561f9209b019a3a8b9706ce9dc6283/68747470733a2f2f696d672e736869656c64732e696f2f636f6465636f762f632f6769746875622f646f636b65722f6275696c64783f6c6f676f3d636f6465636f76267374796c653d666c61742d737175617265)](https://codecov.io/gh/docker/buildx)

Buildx is a Docker CLI plugin for extended build capabilities with [BuildKit](https://github.com/moby/buildkit).

Tip

**Key features**

- Familiar UI from `docker build`
- Full BuildKit capabilities with container driver
- Multiple builder instance support
- Multi-node builds for cross-platform images
- Compose build support
- High-level builds with [Bake](https://docs.docker.com/build/bake/)
- In-container driver support (both Docker and Kubernetes)

------------------------------------------------------------------------

- [Installing](#installing)
  - [Windows and macOS](#windows-and-macos)
  - [Linux packages](#linux-packages)
  - [Manual download](#manual-download)
  - [Dockerfile](#dockerfile)
- [Building](#building)
- [Getting started](#getting-started)
  - [Building with Buildx](#building-with-buildx)
  - [Working with builder instances](#working-with-builder-instances)
  - [Building multi-platform images](#building-multi-platform-images)
- [Reference](/docker/buildx/blob/master/docs/reference/buildx.md)
- [Contributing](#contributing)

## Installing

[](#installing)

Using Buildx with Docker requires Docker engine 19.03 or newer.

Warning

Using an incompatible version of Docker may result in unexpected behavior, and will likely cause issues, especially when using Buildx builders with more recent versions of BuildKit.

### Windows and macOS

[](#windows-and-macos)

Docker Buildx is included in [Docker Desktop](https://docs.docker.com/desktop/) for Windows and macOS.

### Linux packages

[](#linux-packages)

Docker Engine package repositories contain Docker Buildx packages when installed according to the [Docker Engine install documentation](https://docs.docker.com/engine/install/). Install the `docker-buildx-plugin` package to install the Buildx plugin.

### Manual download

[](#manual-download)

Important

This section is for unattended installation of the Buildx component. These instructions are mostly suitable for testing purposes. We do not recommend installing Buildx using manual download in production environments as they will not be updated automatically with security updates.

On Windows and macOS, we recommend that you install [Docker Desktop](https://docs.docker.com/desktop/) instead. For Linux, we recommend that you follow the [instructions specific for your distribution](#linux-packages).

You can also download the latest binary from the [GitHub releases page](https://github.com/docker/buildx/releases/latest).

Rename the relevant binary and copy it to the destination matching your OS:

| OS      | Binary name         | Destination folder                  |
|---------|---------------------|-------------------------------------|
| Linux   | `docker-buildx`     | `$HOME/.docker/cli-plugins`         |
| macOS   | `docker-buildx`     | `$HOME/.docker/cli-plugins`         |
| Windows | `docker-buildx.exe` | `%USERPROFILE%\.docker\cli-plugins` |

Or copy it into one of these folders for installing it system-wide.

On Unix environments:

- `/usr/local/lib/docker/cli-plugins` OR `/usr/local/libexec/docker/cli-plugins`
- `/usr/lib/docker/cli-plugins` OR `/usr/libexec/docker/cli-plugins`

On Windows:

- `C:\Program Files\Docker\cli-plugins`
- `C:\ProgramData\Docker\cli-plugins` (for docker 28.x and earlier only)

Note

On Unix environments, it may also be necessary to make it executable with `chmod +x`:

    $ chmod +x ~/.docker/cli-plugins/docker-buildx

### Dockerfile

[](#dockerfile)

Here is how to install and use Buildx inside a Dockerfile through the [`docker/buildx-bin`](https://hub.docker.com/r/docker/buildx-bin) image:

    # syntax=docker/dockerfile:1
    FROM docker
    COPY --from=docker/buildx-bin /buildx /usr/libexec/docker/cli-plugins/docker-buildx
    RUN docker buildx version

## Building

[](#building)

    # Buildx 0.6+
    $ docker buildx bake "https://github.com/docker/buildx.git"
    $ mkdir -p ~/.docker/cli-plugins
    $ mv ./bin/build/buildx ~/.docker/cli-plugins/docker-buildx

    # Docker 19.03+
    $ DOCKER_BUILDKIT=1 docker build --platform=local -o . "https://github.com/docker/buildx.git"
    $ mkdir -p ~/.docker/cli-plugins
    $ mv buildx ~/.docker/cli-plugins/docker-buildx

    # Local
    $ git clone https://github.com/docker/buildx.git && cd buildx
    $ make install

## Getting started

[](#getting-started)

### Building with Buildx

[](#building-with-buildx)

Buildx is a Docker CLI plugin that extends the `docker build` command with the full support of the features provided by [Moby BuildKit](https://docs.docker.com/build/buildkit/) builder toolkit. It provides the same user experience as `docker build` with many new features like creating scoped builder instances and building against multiple nodes concurrently.

After installation, Buildx can be accessed through the `docker buildx` command with Docker 19.03. `docker buildx build` is the command for starting a new build. With Docker versions older than 19.03 Buildx binary can be called directly to access the `docker buildx` subcommands.

    $ docker buildx build .
    [+] Building 8.4s (23/32)
     => ...

Buildx will always build using the BuildKit engine and does not require `DOCKER_BUILDKIT=1` environment variable for starting builds.

The `docker buildx build` command supports features available for `docker build`, including features such as outputs configuration, inline build caching, and specifying target platform. In addition, Buildx also supports new features that are not yet available for regular `docker build` like building manifest lists, distributed caching, and exporting build results to OCI image tarballs.

Buildx is flexible and can be run in different configurations that are exposed through various [drivers](https://docs.docker.com/build/builders/drivers/). Each driver defines how and where a build should run, and have different feature sets.

We currently support the following drivers:

- The `docker` driver ([manual](https://docs.docker.com/build/builders/drivers/docker/))
- The `cloud` driver ([manual](https://docs.docker.com/build-cloud/))
- The `docker-container` driver ([manual](https://docs.docker.com/build/builders/drivers/docker-container/))
- The `kubernetes` driver ([manual](https://docs.docker.com/build/drivers/kubernetes/))
- The `remote` driver ([manual](https://docs.docker.com/build/builders/drivers/remote/))

For more information, see the [builders](https://docs.docker.com/build/builders/) and [drivers](https://docs.docker.com/build/builders/drivers/) guide.

Note

For more information, see [Docker Build docs](https://docs.docker.com/build/concepts/overview/).

### Working with builder instances

[](#working-with-builder-instances)

By default, Buildx will initially use the `docker` driver if it is supported, providing a very similar user experience to the native `docker build`. Note that you must use a local shared daemon to build your applications.

Buildx allows you to create new instances of isolated builders. This can be used for getting a scoped environment for your CI builds that does not change the state of the shared daemon or for isolating the builds for different projects. You can create a new instance for a set of remote nodes, forming a build farm, and quickly switch between them.

You can create new instances using the [`docker buildx create`](/docker/buildx/blob/master/docs/reference/buildx_create.md) command. This creates a new builder instance with a single node based on your current configuration.

To use a remote node you can specify the `DOCKER_HOST` or the remote context name while creating the new builder. After creating a new instance, you can manage its lifecycle using the [`docker buildx inspect`](/docker/buildx/blob/master/docs/reference/buildx_inspect.md), [`docker buildx stop`](/docker/buildx/blob/master/docs/reference/buildx_stop.md), and [`docker buildx rm`](/docker/buildx/blob/master/docs/reference/buildx_rm.md) commands. To list all available builders, use [`docker buildx ls`](/docker/buildx/blob/master/docs/reference/buildx_ls.md). After creating a new builder you can also append new nodes to it.

To switch between different builders, use [`docker buildx use <name>`](/docker/buildx/blob/master/docs/reference/buildx_use.md). After running this command, the build commands will automatically use this builder.

Docker also features a [`docker context`](https://docs.docker.com/engine/reference/commandline/context/) command that can be used for giving names for remote Docker API endpoints. Buildx integrates with `docker context` so that all of your contexts automatically get a default builder instance. While creating a new builder instance or when adding a node to it, you can also set the context name as the target.

Note

For more information, see [Builders docs](https://docs.docker.com/build/builders/).

### Building multi-platform images

[](#building-multi-platform-images)

BuildKit is designed to work well for building for multiple platforms and not only for the architecture and operating system that the user invoking the build happens to run.

When you invoke a build, you can set the `--platform` flag to specify the target platform for the build output, (for example, `linux/amd64`, `linux/arm64`, or `darwin/amd64`).

When the current builder instance is backed by the `cloud`, `docker-container`, `kubernetes` or `remote` driver, you can specify multiple platforms together. In this case, it builds a manifest list which contains images for all specified architectures.

When you use this image in [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/) or [`docker service`](https://docs.docker.com/reference/cli/docker/service/), Docker picks the correct image based on the node's platform.

You can build multi-platform images using three different strategies that are supported by Buildx and Dockerfiles:

1.  Using the QEMU emulation support in the kernel
2.  Building on multiple native nodes using the same builder instance
3.  Using a stage in Dockerfile to cross-compile to different architectures

QEMU is the easiest way to get started if your node already supports it (for example. if you are using Docker Desktop). It requires no changes to your Dockerfile and BuildKit automatically detects the secondary architectures that are available. When BuildKit needs to run a binary for a different architecture, it automatically loads it through a binary registered in the `binfmt_misc` handler.

For QEMU binaries registered with `binfmt_misc` on the host OS to work transparently inside containers they must be registered with the `fix_binary` flag. This requires a kernel \>= 4.8 and binfmt-support \>= 2.1.7. You can check for proper registration by checking if `F` is among the flags in `/proc/sys/fs/binfmt_misc/qemu-*`. While Docker Desktop comes preconfigured with `binfmt_misc` support for additional platforms, for other installations it likely needs to be installed using [`tonistiigi/binfmt`](https://github.com/tonistiigi/binfmt) image.

    $ docker run --privileged --rm tonistiigi/binfmt --install all

Using multiple native nodes provide better support for more complicated cases that are not handled by QEMU and generally have better performance. You can add additional nodes to the builder instance using the `--append` flag.

Assuming contexts `node-amd64` and `node-arm64` exist in `docker context ls`;

    $ docker buildx create --use --name mybuild node-amd64
    mybuild
    $ docker buildx create --append --name mybuild node-arm64
    $ docker buildx build --platform linux/amd64,linux/arm64 .

Finally, depending on your project, the language that you use may have good support for cross-compilation. In that case, multi-stage builds in Dockerfiles can be effectively used to build binaries for the platform specified with `--platform` using the native architecture of the build node. A list of build arguments like `BUILDPLATFORM` and `TARGETPLATFORM` is available automatically inside your Dockerfile and can be leveraged by the processes running as part of your build.

    # syntax=docker/dockerfile:1
    FROM --platform=$BUILDPLATFORM golang:alpine AS build
    ARG TARGETPLATFORM
    ARG BUILDPLATFORM
    RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM" > /log
    FROM alpine
    COPY --from=build /log /log

You can also use [`tonistiigi/xx`](https://github.com/tonistiigi/xx) Dockerfile cross-compilation helpers for more advanced use-cases.

Note

For more information, see [Multi-platform builds docs](https://docs.docker.com/build/building/multi-platform/).

## Contributing

[](#contributing)

Want to contribute to Buildx? Awesome! You can find information about contributing to this project in the [CONTRIBUTING.md](/docker/buildx/blob/master/.github/CONTRIBUTING.md)

## About

Docker CLI plugin for extended build capabilities with BuildKit

[docs.docker.com/build/](https://docs.docker.com/build/)

### Topics

[buildkit](/topics/buildkit)[buildx](/topics/buildx)[docker](/topics/docker)[dockerfile](/topics/dockerfile)

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](/docker/buildx#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/docker/buildx/activity)

[Custom properties](/docker/buildx/custom-properties)

### Stars

**4.5k** stars

### Watchers

**63** watching

### Forks

[**684** forks](/docker/buildx/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fdocker%2Fbuildx&report=docker+%28user%29)

## Releases

## Used by

## Contributors

## Languages
