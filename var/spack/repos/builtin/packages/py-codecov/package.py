# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCodecov(PythonPackage):
    """Hosted coverage reports for Github, Bitbucket and Gitlab."""

    homepage = "https://github.com/codecov/codecov-python"
    pypi = "codecov/codecov-2.0.15.tar.gz"

    # Since codecov has been removed from PyPI, py-codecov is deprecated.
    # The new codecov uploader can be installed with the package codecov.
    version(
        "2.0.15",
        sha256="8ed8b7c6791010d359baed66f84f061bba5bd41174bf324c31311e8737602788",
        deprecated=True,
    )

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-requests@2.7.9:", type=("build", "run"))
    depends_on("py-coverage", type=("build", "run"))
