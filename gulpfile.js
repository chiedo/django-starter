// This could be combined with the parent folders gulpfile if it is present.
// Separate now for clarity purposes

var gulp = require('gulp');
var browserify = require('gulp-browserify');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCSS = require('gulp-minify-css');

var paths = {
  css: ['apps/home/static/home/css/**/*.scss', 'apps/people/static/people/css/**/*.scss'],
  reactjs: ['react/main.react.jsx'],
};

gulp.task('browserify', function() {
  gulp.src(paths.reactjs)
  .pipe(browserify({transform: 'reactify'}))
  .pipe(concat('react-bundle.js'))
  //.pipe(uglify())
  .pipe(gulp.dest('apps/home/static/home/js'));
});

gulp.task('sass', function () {
  gulp.src(paths.css)
    .pipe(sass())
    .pipe(minifyCSS({keepBreaks:false}))
    .pipe(gulp.dest('apps/home/static/home/css'));
});

gulp.task('watch', function() {
  gulp.watch(['react/**/*.*'], ['browserify']);
  gulp.watch(paths.css, ['sass']);
});

gulp.task('default',['watch','browserify', 'sass']);
