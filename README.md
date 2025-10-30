# Neuralk SDK Documentation 2.0

This documentation is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

If you want a local installation you can clone the repo and run with npm (see below)

The build is done automatically by Netlify with every git push to the repo.


## Uploading sphinx generated markdowns

These are the only files that we need generated from sphinx:
- API reference: put all files at the `api-reference` folder 
- Classification module & categorization module examples: `docs > plot_categorization.md, docs > plot_two_moon_classification.md` 

## Installation

## Local Development

```bash
npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

```bash
npm run serve
```
