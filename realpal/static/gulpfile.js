var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var sass = require('gulp-sass');
var imagemin = require('gulp-imagemin');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var cssmin = require('gulp-cssmin');

// Static Server + watching scss/html files
gulp.task('serve', ['copy-assets', 'scripts', 'vendor', 'imagemin'], function () {

  browserSync.init({
    notify: false,
    port: 8000,
    proxy: 'localhost:8000',
    open: false
  });

  // gulp.watch('src/sass/*.scss', ['sass']);
  gulp.watch('../templates/**/*.html', browserSync.reload);
  // gulp.watch('src/js/*.js', ['babel']).on('change', browserSync.reload);
  gulp.watch('src/js/*.js').on('change', browserSync.reload);
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
    .pipe(concat('main.js'))
    .pipe(uglify())
    .pipe(gulp.dest('app/js'))
    .pipe(browserSync.reload({stream: true, once: true}));
});

gulp.task('css', function () {
  gulp.src('src/**/*.css')
  // .pipe(concat('style.css'))
    .pipe(cssmin())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('dist'));
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

// Compile sass into CSS & auto-inject into browsers
// gulp.task('sass', function () {
//   return gulp.src('src/css/*.css')
//     .pipe(sass({outputStyle: 'compressed'}, {errLogToConsole: true}))
//     .pipe(prefix('last 2 versions', '> 1%', 'ie 8', 'Android 2', 'Firefox ESR'))
//
//     .pipe(gulp.dest('app/css'))
//     .pipe(browserSync.stream());
// });

gulp.task('default', ['serve']);