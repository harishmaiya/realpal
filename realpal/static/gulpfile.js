const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass');
const prefix = require('gulp-autoprefixer');
const babel = require('gulp-babel');
const imagemin = require('gulp-imagemin');

// Static Server + watching scss/html files
gulp.task('serve', ['copy-assets', 'copy-vendor', 'sass', 'babel', 'imagemin'], function () {

    browserSync.init({
        notify: false,
        port: 8000,
        proxy: 'localhost:8000',
        open: false
    });

    gulp.watch('src/sass/*.scss', ['sass']);
    gulp.watch('../templates/**/*.html', browserSync.reload);
    gulp.watch('src/js/*.js', ['babel']).on('change', browserSync.reload);
});

gulp.task('copy-vendor', function () {
    gulp.src('src/vendor/**/*')
        .pipe(gulp.dest('app/vendor/'));
});

gulp.task('copy-assets', function () {
    gulp.src(['src/assets/**/*', '!src/assets/images/'])
        .pipe(gulp.dest('app/assets/'));
});

gulp.task('babel', function () {
    return gulp.src('src/js/*.js')
        .pipe(babel({
            presets: ['es2015']
        }))
        .pipe(gulp.dest('app/js'));
});

gulp.task('imagemin', () =>
    gulp.src('src/images/**/*')
        .pipe(imagemin([
            imagemin.gifsicle({interlaced: true}),
            imagemin.jpegtran({progressive: true}),
            imagemin.optipng({optimizationLevel: 5}),
        ]))
        .pipe(gulp.dest('app/images'))
);

// Compile sass into CSS & auto-inject into browsers
gulp.task('sass', function () {
    return gulp.src('src/css/*.css')
        .pipe(sass({outputStyle: 'compressed'}, {errLogToConsole: true}))
        .pipe(prefix('last 2 versions', '> 1%', 'ie 8', 'Android 2', 'Firefox ESR'))

        .pipe(gulp.dest('app/css'))
        .pipe(browserSync.stream());
});

gulp.task('default', ['serve']);