# Remove the existing bouncing ball opk.
rm -f gosdl2.opk && \

# Compile the main.go
CC=/opt/gcw0-toolchain/usr/bin/mipsel-gcw0-linux-uclibc-gcc \
GOARCH=mipsle \
PKG_CONFIG=/opt/gcw0-toolchain/usr/bin/pkg-config \
CGO_ENABLED=1  \
go build main.go && mv main gosdl2 &&

# Create the OPK. It is a squashfs archive so we just list all the files and
# the last name will be the archive name,
mksquashfs  default.gcw0.desktop gosdl2 icon.png gosdl2.opk -all-root -no-xattrs -noappend -no-exports

