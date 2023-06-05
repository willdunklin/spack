# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyArchspec(PythonPackage):
    """A library for detecting, labeling and reasoning about
    microarchitectures.
    """

    homepage = "https://archspec.readthedocs.io/en/latest/"
    pypi = "archspec/archspec-0.2.0.tar.gz"

    maintainers("alalazo")

    version("0.2.1", sha256="0974a8a95831d2d43cce906c5b79a35d5fd2bf9be478b0e3b7d83ccc51ac815e")
    version("0.2.0", sha256="6aaba5ebdb5c3633c400d8c221a6a18716da0c64b367a8509f4217b22e91a5f5")
    version(
        "0.1.3",
        sha256="a1aa7abde4d4ce38d115dfd572584906fa8e192e3272b8897e7b4fa1213ec27c",
        deprecated=True,
    )
    version(
        "0.1.2",
        sha256="8bb998370f0dc3e509d57c13724ab4109d761fd74af20da26fbe513b0fe01c46",
        deprecated=True,
    )
    version(
        "0.1.1",
        sha256="34bafad493b41208857232e21776216d716de37ab051a6a4a1cc1653f7e26423",
        deprecated=True,
    )
    version(
        "0.1.0",
        sha256="a4431d0bbe9c9dd7b293c39d8e7590034d512ce5f5a1278a6cbdf61b33f7202d",
        deprecated=True,
    )

    with when("@0.1"):
        depends_on("python@2.7:2.8,3.5:", type=("build", "run"))
        depends_on("py-click@7.1.2:7", type=("build", "run"))
        depends_on("py-six@1.13.0:1", type=("build", "run"))

    with when("@0.2.0"):
        depends_on("py-click@8", type=("build", "run"))

    depends_on("python@3.6:", when="@0.2:", type=("build", "run"))
    depends_on("py-poetry-core@1.0.0:", type="build")

    def patch(self):
        # See https://python-poetry.org/docs/pyproject/#poetry-and-pep-517
        if self.spec.satisfies("@:0.1.3"):
            with working_dir(self.stage.source_path):
                filter_file("poetry>=0.12", "poetry_core>=1.0.0", "pyproject.toml")
                filter_file("poetry.masonry.api", "poetry.core.masonry.api", "pyproject.toml")
