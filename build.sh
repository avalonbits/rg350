rm -f bouncing_ball.opk && \
python -m compileall ./ && \
mksquashfs  default.gcw0.desktop ball.pyc icon.png intro_ball.gif bouncing_ball.opk -all-root -no-xattrs -noappend -no-exports
