const { src, dest, watch, parallel, series }  = require('gulp');

const scss = require('gulp-sass')(require('sass'));
const concat = require('gulp-concat');
const browserSync = require('browser-sync').create();
const uglify = require('gulp-uglify-es').default;
const autoprefixer = require('gulp-autoprefixer');
const imagemin = require('gulp-imagemin');
const del = require('del');

const currentDir = os.getcwd()

function browsersync() {
  browserSync.init({
    server : {
      baseDir: ['./myapp','./static']
    }
  });
}

function cleanDist() {
  return del('dist')
}

function images() {
  return src('static/images/**/*')
    .pipe(imagemin(
      [
        imagemin.gifsicle({ interlaced: true }),
        imagemin.mozjpeg({ quality: 75, progressive: true }),
        imagemin.optipng({ optimizationLevel: 5 }),
        imagemin.svgo({
          plugins: [
            { removeViewBox: true },
            { cleanupIDs: false }
          ]
        })
      ]
    ))
    .pipe(dest('currentDirdist/images'))
}

function scripts() {
  return src([
    'node_modules/jquery/dist/jquery.js',
    'node_modules/slick-carousel/slick/slick.js',
    'static/js/main.js'
  ])
    .pipe(concat('main.min.js'))
    .pipe(uglify())
    .pipe(dest('static/js'))
    .pipe(browserSync.stream())
}


function styles() {
  return src('static/scss/style.scss')
      .pipe(scss({outputStyle: 'compressed'}))
      .pipe(concat('style.min.css'))
      .pipe(autoprefixer({
        overrideBrowserslist: ['last 10 version'],
        grid: true
      }))
      .pipe(dest('static/css'))
      .pipe(browserSync.stream())
}

function build() {
  return src([
    'static/css/style.min.css',
    'static/fonts/**/*',
    'static/js/main.min.js',
    'myapp/templates/myapp/gulp/app/*.html'
  ], {base: currentDir})
    .pipe(dest('dist'))
}

function watching() {
  watch(['static/scss/**/*.scss'], styles);
  watch(['static/js/**/*.js', '!static/js/main.min.js'], scripts);
  watch(['myapp/templates/myapp/gulp/app/*.html']).on('change', browserSync.reload);
}

exports.styles = styles;
exports.watching = watching;
exports.browsersync = browsersync;
exports.scripts = scripts;
exports.images = images;
exports.cleanDist = cleanDist;


exports.build = series(cleanDist, images, build);
exports.default = parallel(styles ,scripts ,browsersync, watching);


