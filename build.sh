# Remove the existing bouncing ball opk.
rm -f bouncing_ball.opk && \

# Compile the ball.py to ball.pyc
python -m compileall ./ && \

# Create the OPK. It is a squashfs archive so we just list all the files and
# the last name will be the archive name,
mksquashfs  default.gcw0.desktop ball.pyc icon.png ball.png bouncing_ball.opk -all-root -no-xattrs -noappend -no-exports
