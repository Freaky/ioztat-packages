# Copyright 1999-2022 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=7

PYTHON_COMPAT=( python3_{7..10} )
inherit python-r1

DESCRIPTION="Storage load analysis tool for OpenZFS datasets"
HOMEPAGE="https://github.com/jimsalterjrs/ioztat/"
SRC_URI="https://github.com/jimsalterjrs/ioztat/archive/refs/tags/v2.0.1.tar.gz"

LICENSE="BSD-2"
SLOT="0"
KEYWORDS="**"
IUSE=""

DEPEND="${PYTHON_DEPS}"
BDEPEND=""

DOCS= ( README.md CHANGELOG.md )

src_install() {
	dobin ioztat
	doman ioztat.1
}

