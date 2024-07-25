import * as nodePath from 'path';
const rootFolder = nodePath.basename(nodePath.resolve());

const buildFolder = './mysite/static/dist';
const staticFolder = './mysite/static';
const templatesFolder = './mysite/myapp/templates/myapp/gulp/app';
const srcFolder = './src';

export const path = {
    build: {
        js: `${staticFolder}/js/`,
        images: `${staticFolder}/images/`,
        css: `${staticFolder}/css/`,
        html: `${templatesFolder}/`,
        files: `${buildFolder}/files/`,
    },
    src: {
        js: `${srcFolder}/js/main.js`,
        images: `${srcFolder}/img/**/*.{jpg,jpeg,png,svg}`,
        scss: `${srcFolder}/scss/style.scss`,
        html: `${srcFolder}/*.html`,
        files: `${srcFolder}/files/*.*`,
    },
    watch: {
        js: `${srcFolder}/js/*.js`,
        images: `${srcFolder}/img/**/*.{jpg,jpeg,png,svg}`,
        scss: `${srcFolder}/scss/*.scss`,
        html: `${srcFolder}/*.html`,
        files: `${srcFolder}/files/**/*.*`
    },
    clean: [buildFolder,templatesFolder,staticFolder],
    buildFolder: buildFolder,
    staticFolder: staticFolder,
    templatesFolder: templatesFolder,
    srcFolder: srcFolder,
    rootFolder: rootFolder,
    ftp: ``
}