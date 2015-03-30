var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var sass = require('gulp-sass');
minifyCSS = require('gulp-minify-css');

var paths = {
  css: ['static/home/css/**/*.scss'],
};

gulp.task('sass', function () {
  gulp.src(paths.css)
    .pipe(sass())
    .pipe(minifyCSS({keepBreaks:false}))
    .pipe(gulp.dest('static/home/css'));
});

gulp.task('watch', function() {
  gulp.watch(paths.css, ['sass']);
});

gulp.task('default', ['watch', 'sass']);
