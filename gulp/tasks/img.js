export async function img(){
    return app.gulp.src(app.path.src.images)
    
    .pipe(app.gulp.dest(app.path.build.images))
    .pipe(app.plugins.browserSync.stream())
}