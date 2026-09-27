---
title: esbuild
description: An extremely fast bundler for the web
product: Amazon Bedrock AgentCore
section: References / esbuild.github.io
source_url: https://esbuild.github.io
fetched: '2026-09-26'
tags:
- agentcore
- esbuild-github-io
- reference
- related
referenced_by:
- runtime-get-started-cli-typescript.md
- runtime-get-started-code-deploy-node.md
conversion: pandoc
---

# esbuild

> An extremely fast bundler for the web

[esbuild](https://esbuild.github.io/)

0.39s

[parcel 2](https://parceljs.org/)

14.91s

[rollup 4](https://rollupjs.org/) + [terser](https://terser.org/)

34.10s

[webpack 5](https://webpack.js.org/)

41.21s

0s

10s

20s

30s

40s

Above: the time to do a production bundle of 10 copies of the [three.js](https://github.com/mrdoob/three.js) library from scratch using default settings, including minification and source maps. More info [here](/faq/#benchmark-details).

Our current build tools for the web are 10-100x slower than they could be. The main goal of the esbuild bundler project is to bring about a new era of build tool performance, and create an easy-to-use modern bundler along the way.

Major features:

- Extreme speed without needing a cache
- [JavaScript](/content-types/#javascript), [CSS](/content-types/#css), [TypeScript](/content-types/#typescript), and [JSX](/content-types/#jsx) built-in
- A straightforward [API](/api/) for CLI, JS, and Go
- Bundles ESM and CommonJS modules
- Bundles CSS including [CSS modules](https://github.com/css-modules/css-modules)
- Tree shaking, [minification](/api/#minify), and [source maps](/api/#sourcemap)
- [Local server](/api/#serve), [watch mode](/api/#watch), and [plugins](/plugins/)

Check out the [getting started](/getting-started/) instructions if you want to give esbuild a try.
