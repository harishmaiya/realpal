var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var sass = require('gulp-sass');
var prefix = require('gulp-autoprefixer');
var imagemin = require('gulp-imagemin');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var cssmin = require('gulp-cssmin');

// Static Server + watching scss/html files
gulp.task('serve', [ 'copy-assets','scripts','sass','vendor', 'imagemin'], function () {

  browserSync.init({
    notify: false,
    port: 8000,
    proxy: 'localhost:8000',
    open: false
  });
  gulp.watch('src/scss/**/*.scss', ['sass']);
  gulp.watch('../templates/**/*.html', browserSync.reload);
  gulp.watch('src/js/*.js').on('change', browserSync.reload);
});
gulp.task('copy-assets', function () {
  gulp.src(['src/assets/**/*', '!src/assets/fonts/'])
    .pipe(gulp.dest('app/assets/'));
});
gulp.task('vendor', function () {
  gulp.src('src/js/vendor/*.js')
    .pipe(concat('vendor.js'))
    .pipe(uglify())
    .pipe(gulp.dest('app/js/vendor'))
    .pipe(browserSync.reload({stream: true, once: true}));
});

gulp.task('scripts', function () {
  gulp.src('src/js/*.js')
    .pipe(concat('main.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('app/js'))
    .pipe(browserSync.reload({stream: true, once: true}));
});

// Compile sass into CSS & auto-inject into browsers
gulp.task('sass', function () {
  return gulp.src('src/sass/*.scss')
    .pipe(sass({outputStyle: 'compressed'}, {errLogToConsole: true}))
    .pipe(prefix('last 2 versions', '> 1%', 'ie 8', 'Android 2', 'Firefox ESR'))

    .pipe(gulp.dest('app/css'))
    .pipe(browserSync.stream());
});

gulp.task('vendor-css', function () {
  gulp.src('src/css/vendor/*.css')
    .pipe(concat('vendor.css'))
    .pipe(cssmin())
    .pipe(gulp.dest('app/css/vendor'));
});

gulp.task('imagemin', function () {
    gulp.src('src/images/**/*')
      .pipe(imagemin([
        imagemin.gifsicle({interlaced: true}),
        imagemin.jpegtran({progressive: true}),
        imagemin.optipng({optimizationLevel: 5})
      ]))
      .pipe(gulp.dest('app/images'))
  }
);

gulp.task('default', ['serve']);
