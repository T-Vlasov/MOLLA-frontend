import * as dartSass from 'sass';
import gulpSass from 'gulp-sass';
import rename from 'gulp-rename';
import sourcemaps from 'gulp-sourcemaps';

import cleanCss from 'gulp-clean-css';
import webpcss from 'gulp-webpcss';
import autoprefixer from 'gulp-autoprefixer';
import groupCssMediaQueries from 'gulp-group-css-media-queries';
import minifyCSS from 'gulp-minify-css';

const sass = gulpSass(dartSass);

export async function scss(done){
    return app.gulp.src(app.path.src.scss, {sourcemaps: true})
    
    .pipe(rename({extname:".min.css"}))
    .pipe(sass({outputStyle: 'compressed'}))
    .pipe(autoprefixer({
        grid: true,
        overrideBrowserslist: ["last 3 versions"],
        cascade: true
    }))
    .pipe(app.gulp.dest(app.path.build.css))
    .pipe(app.plugins.browserSync.stream());
}