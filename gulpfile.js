var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('tests', function() {
  gulp.watch(['*.py','**/*.py'], shell.task([
    'REUSE_DB=1 python manage.py test'
  ], { ignoreErrors: true }));
});

gulp.task('default', ['tests']);

