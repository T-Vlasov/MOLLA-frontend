import webpack from "webpack-stream";

export async function js(){
    return app.gulp.src(app.path.src.js, {sourcemaps: true})
    .pipe(webpack({
        mode: "development",
        output: {
            filename: "main.min.js"
        }
    }))
    .pipe(app.gulp.dest(app.path.build.js))
    .pipe(app.plugins.browserSync.stream())
}