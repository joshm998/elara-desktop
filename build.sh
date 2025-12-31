#!/bin/bash
set -e

VERSION=$(grep "^Version:" elara-desktop.spec | awk '{print $2}')
RELEASE=$(grep "^Release:" elara-desktop.spec | awk '{print $2}' | cut -d'%' -f1)
NAME="elara-desktop"

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

rm -f ~/rpmbuild/SOURCES/${NAME}-${VERSION}.tar.gz
rm -f ~/rpmbuild/RPMS/noarch/${NAME}-${VERSION}-${RELEASE}*.rpm

tar czf ~/rpmbuild/SOURCES/${NAME}-${VERSION}.tar.gz \
    --exclude='.git' \
    --exclude='*.rpm' \
    --transform="s,^,${NAME}-${VERSION}/," \
    .

cp ${NAME}.spec ~/rpmbuild/SPECS/

rpmbuild -bb ~/rpmbuild/SPECS/${NAME}.spec

RPM_FILE=$(find ~/rpmbuild/RPMS/noarch/ -name "${NAME}-${VERSION}-${RELEASE}*.rpm" | head -n1)

if [ -z "$RPM_FILE" ]; then
    echo "Error: RPM file not found"
    exit 1
fi

if rpm -q ${NAME} &>/dev/null; then
    sudo dnf remove -y ${NAME}
fi

sudo dnf install -y "$RPM_FILE"
