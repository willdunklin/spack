# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDask(PythonPackage):
    """Dask is a flexible parallel computing library for analytics."""

    homepage = "https://github.com/dask/dask/"
    pypi = "dask/dask-1.1.0.tar.gz"

    maintainers("skosukhin")

    version("2023.4.1", sha256="9dc72ebb509f58f3fe518c12dd5a488c67123fdd66ccb0b968b34fd11e512153")
    version("2022.10.2", sha256="42cb43f601709575fa46ce09e74bea83fdd464187024f56954e09d9b428ceaab")
    version("2021.6.2", sha256="8588fcd1a42224b7cfcd2ebc8ad616734abb6b1a4517efd52d89c7dd66eb91f8")
    version("2021.4.1", sha256="195e4eeb154222ea7a1c368119b5f321ee4ec9d78531471fe0145a527f744aa8")
    version("2020.12.0", sha256="43e745afd4b464e6c0113131e430a16dce6ac42460b06e24d799093d098f7ab0")
    version(
        "2.16.0",
        sha256="2af5b0dcd48ce679ce0321cf91de623f4fe376262789b951fefa3c334002f350",
        deprecated=True,
    )
    version(
        "1.2.2",
        sha256="5e7876bae2a01b355d1969b73aeafa23310febd8c353163910b73e93dc7e492c",
        deprecated=True,
    )
    version(
        "1.1.2",
        sha256="93b355b9a9c9a3ddbb39fab99d5759aad5cfd346f4520b87788970e80cf97256",
        deprecated=True,
    )
    version(
        "1.1.0",
        sha256="e76088e8931b326c05a92d2658e07b94a6852b42c13a7560505a8b2354871454",
        deprecated=True,
    )
    version(
        "0.17.4",
        sha256="c111475a3d1f8cba41c8094e1fb1831c65015390dcef0308042a11a9606a2f6d",
        deprecated=True,
    )
    version(
        "0.8.1",
        sha256="43deb1934cd033668e5e60b735f45c9c3ee2813f87bd51c243f975e55267fa43",
        deprecated=True,
    )

    variant("array", default=True, description="Install requirements for dask.array")
    variant("bag", default=True, description="Install requirements for dask.bag")
    variant("dataframe", default=True, description="Install requirements for dask.dataframe")
    variant("distributed", default=True, description="Install requirements for dask.distributed")
    variant("diagnostics", default=False, description="Install requirements for dask.diagnostics")
    variant(
        "delayed",
        default=True,
        description="Install requirements for dask.delayed (dask.imperative)",
    )
    variant("yaml", default=True, description="Ensure support for YAML configuration files")

    conflicts("~bag", when="@2021.3.1:")
    conflicts("+distributed", when="@:0.4.0,0.7.6:0.8.1")
    conflicts("+diagnostics", when="@:0.5.0")
    conflicts("~delayed", when="@2021.3.1:")
    conflicts("+yaml", when="@:0.17.5")
    conflicts("~yaml", when="@2.17.1:")

    depends_on("python@2.7:2.8,3.5:", type=("build", "run"))
    depends_on("python@3.5:", type=("build", "run"), when="@2.0.0:")
    depends_on("python@3.6:", type=("build", "run"), when="@2.7.0:")
    depends_on("python@3.7:", type=("build", "run"), when="@2021.3.1:")
    depends_on("python@3.8:", type=("build", "run"), when="@2022.10.2:")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@62.6:", type="build", when="@2023.4.1:")
    depends_on("py-versioneer@0.28+toml", type="build", when="@2023.4.1:")

    # Common requirements
    depends_on("py-packaging@20:", type="build", when="@2022.10.2:")
    depends_on("py-pyyaml", type=("build", "run"), when="@2.17.1:")
    depends_on("py-pyyaml@5.3.1:", type=("build", "run"), when="@2022.10.2:")
    depends_on("py-cloudpickle@1.1.1:", type=("build", "run"), when="@2021.3.1:")
    depends_on("py-cloudpickle@1.5.0:", type=("build", "run"), when="@2023.4.1:")
    depends_on("py-fsspec@0.6.0:", type=("build", "run"), when="@2021.3.1:")
    depends_on("py-fsspec@2021.09.0:", type=("build", "run"), when="@2023.4.1:")
    depends_on("py-toolz@0.8.2:", type=("build", "run"), when="@2021.3.1:")
    depends_on("py-toolz@0.10.0:", type=("build", "run"), when="@2023.4.1:")
    depends_on("py-partd@0.3.10:", type=("build", "run"), when="@2021.3.1:")
    depends_on("py-partd@1.2.0:", type=("build", "run"), when="@2023.4.0:")
    depends_on("py-click@7.0:", type=("build", "run"), when="@2022.10.2:")
    depends_on("py-click@8.0:", type=("build", "run"), when="@2023.4.1:")
    depends_on("py-importlib-metadata@4.13.0:", type=("build", "run"), when="@2023.4.0:")

    # Requirements for dask.array
    depends_on("py-numpy", type=("build", "run"), when="@:0.17.1 +array")
    depends_on("py-numpy@1.10.4:", type=("build", "run"), when="@0.17.2: +array")
    depends_on("py-numpy@1.11.0:", type=("build", "run"), when="@0.17.3: +array")
    depends_on("py-numpy@1.13.0:", type=("build", "run"), when="@1.2.1: +array")
    depends_on("py-numpy@1.15.1:", type=("build", "run"), when="@2020.12.0: +array")
    depends_on("py-numpy@1.16.0:", type=("build", "run"), when="@2021.3.1: +array")
    depends_on("py-numpy@1.18.0:", type=("build", "run"), when="@2022.10.2: +array")
    depends_on("py-numpy@1.21.0:", type=("build", "run"), when="@2023.4.0: +array")

    depends_on("py-toolz", type=("build", "run"), when="@:0.6.1 +array")
    depends_on("py-toolz@0.7.2:", type=("build", "run"), when="@0.7.0: +array")
    depends_on("py-toolz@0.7.3:", type=("build", "run"), when="@0.14.1: +array")
    # The dependency on py-toolz is non-optional starting version 2021.3.1
    depends_on("py-toolz@0.8.2:", type=("build", "run"), when="@2.13.0:2021.3.0 +array")

    # Requirements for dask.bag
    depends_on("py-dill", type=("build", "run"), when="@:0.7.5 +bag")
    depends_on("py-cloudpickle", type=("build", "run"), when="@0.7.6: +bag")
    depends_on("py-cloudpickle@0.2.1:", type=("build", "run"), when="@0.8.2: +bag")
    # The dependency on py-cloudpickle is non-optional starting version 2021.3.1
    depends_on("py-cloudpickle@0.2.2:", type=("build", "run"), when="@2.13.0:2021.3.0 +bag")

    depends_on("py-fsspec@0.3.3:", type=("build", "run"), when="@2.2.0: +bag")
    depends_on("py-fsspec@0.5.1:", type=("build", "run"), when="@2.5.0: +bag")
    # The dependency on py-fsspec is non-optional starting version 2021.3.1
    depends_on("py-fsspec@0.6.0:", type=("build", "run"), when="@2.8.0:2021.3.0 +bag")

    depends_on("py-toolz", type=("build", "run"), when="@:0.6.1 +bag")
    depends_on("py-toolz@0.7.2:", type=("build", "run"), when="@0.7.0: +bag")
    depends_on("py-toolz@0.7.3:", type=("build", "run"), when="@0.14.1: +bag")
    # The dependency on py-toolz is non-optional starting version 2021.3.1
    depends_on("py-toolz@0.8.2:", type=("build", "run"), when="@2.13.0:2021.3.0 +bag")

    depends_on("py-partd@0.3.2:", type=("build", "run"), when="@0.6.0: +bag")
    depends_on("py-partd@0.3.3:", type=("build", "run"), when="@0.9.0: +bag")
    depends_on("py-partd@0.3.5:", type=("build", "run"), when="@0.10.2: +bag")
    depends_on("py-partd@0.3.6:", type=("build", "run"), when="@0.12.0: +bag")
    depends_on("py-partd@0.3.7:", type=("build", "run"), when="@0.13.0: +bag")
    depends_on("py-partd@0.3.8:", type=("build", "run"), when="@0.15.0: +bag")
    # The dependency on py-partd is non-optional starting version 2021.3.1
    depends_on("py-partd@0.3.10:", type=("build", "run"), when="@2.0.0:2021.3.0 +bag")

    # Requirements for dask.dataframe
    depends_on("py-numpy", type=("build", "run"), when="@:0.17.1 +dataframe")
    depends_on("py-numpy@1.10.4:", type=("build", "run"), when="@0.17.2: +dataframe")
    depends_on("py-numpy@1.11.0:", type=("build", "run"), when="@0.17.3: +dataframe")
    depends_on("py-numpy@1.13.0:", type=("build", "run"), when="@1.2.1: +dataframe")
    depends_on("py-numpy@1.15.1:", type=("build", "run"), when="@2020.12.0: +dataframe")
    depends_on("py-numpy@1.16.0:", type=("build", "run"), when="@2021.3.1: +dataframe")
    depends_on("py-numpy@1.18.0:", type=("build", "run"), when="@2022.10.2: +dataframe")
    depends_on("py-numpy@1.21.0:", type=("build", "run"), when="@2023.4.0: +dataframe")

    depends_on("py-pandas@0.16.0:", type=("build", "run"), when="+dataframe")
    depends_on("py-pandas@0.18.0:", type=("build", "run"), when="@0.9.0: +dataframe")
    depends_on("py-pandas@0.19.0:", type=("build", "run"), when="@0.14.0: +dataframe")
    depends_on("py-pandas@0.21.0:", type=("build", "run"), when="@1.2.1: +dataframe")
    depends_on("py-pandas@0.23.0:", type=("build", "run"), when="@2.11.0: +dataframe")
    depends_on("py-pandas@0.25.0:", type=("build", "run"), when="@2020.12.0: +dataframe")
    depends_on("py-pandas@1.0:", type=("build", "run"), when="@2022.10.2: +dataframe")
    depends_on("py-pandas@1.3:", type=("build", "run"), when="@2023.4.0: +dataframe")

    depends_on("py-toolz", type=("build", "run"), when="@:0.6.1 +dataframe")
    depends_on("py-toolz@0.7.2:", type=("build", "run"), when="@0.7.0: +dataframe")
    depends_on("py-toolz@0.7.3:", type=("build", "run"), when="@0.14.1: +dataframe")
    # The dependency on py-toolz is non-optional starting version 2021.3.1
    depends_on("py-toolz@0.8.2:", type=("build", "run"), when="@2.13.0:2021.3.0 +dataframe")

    depends_on("py-partd@0.3.2:", type=("build", "run"), when="@0.6.0: +dataframe")
    depends_on("py-partd@0.3.3:", type=("build", "run"), when="@0.9.0: +dataframe")
    depends_on("py-partd@0.3.5:", type=("build", "run"), when="@0.10.2: +dataframe")
    depends_on("py-partd@0.3.7:", type=("build", "run"), when="@0.13.0: +dataframe")
    depends_on("py-partd@0.3.8:", type=("build", "run"), when="@0.15.0: +dataframe")
    depends_on("py-partd@0.3.10:", type=("build", "run"), when="@2.0.0: +dataframe")
    # The dependency on py-partd is non-optional starting version 2021.3.1
    depends_on("py-partd@0.3.10:", type=("build", "run"), when="@2.0.0:2021.3.0 +dataframe")

    depends_on("py-cloudpickle@0.2.1:", type=("build", "run"), when="@0.8.2:2.6.0 +dataframe")

    depends_on("py-fsspec@0.3.3:", type=("build", "run"), when="@2.2.0: +dataframe")
    depends_on("py-fsspec@0.5.1:", type=("build", "run"), when="@2.5.0: +dataframe")
    # The dependency on py-fsspec is non-optional starting version 2021.3.1
    depends_on("py-fsspec@0.6.0:", type=("build", "run"), when="@2.8.0:2021.3.0 +dataframe")

    # Requirements for dask.distributed
    depends_on("py-dill", type=("build", "run"), when="@:0.7.5 +distributed")
    depends_on("py-pyzmq", type=("build", "run"), when="@:0.7.5 +distributed")
    depends_on("py-distributed@:2021.8.0", type=("build", "run"), when="@0.8.2:0.8 +distributed")
    depends_on("py-distributed@1.9:2021.8.0", type=("build", "run"), when="@0.9 +distributed")
    depends_on("py-distributed@1.10:2021.8.0", type=("build", "run"), when="@0.10 +distributed")
    depends_on("py-distributed@1.14:2021.8.0", type=("build", "run"), when="@0.12 +distributed")
    depends_on("py-distributed@1.15:2021.8.0", type=("build", "run"), when="@0.13 +distributed")
    depends_on(
        "py-distributed@1.16:2021.8.0", type=("build", "run"), when="@0.14.1:0.14 +distributed"
    )
    depends_on("py-distributed@1.20:2021.8.0", type=("build", "run"), when="@0.16 +distributed")
    depends_on("py-distributed@1.21:2021.8.0", type=("build", "run"), when="@0.17 +distributed")
    depends_on(
        "py-distributed@1.22:2021.8.0", type=("build", "run"), when="@0.18.0:1 +distributed"
    )
    depends_on(
        "py-distributed@2.0:2021.8.0", type=("build", "run"), when="@2.0.0:2020.11 +distributed"
    )
    depends_on(
        "py-distributed@2020.12.0:2021.8.0",
        type=("build", "run"),
        when="@2020.12.0:2021.6.1 +distributed",
    )
    depends_on("py-distributed@2021.6.2", type=("build", "run"), when="@2021.6.2 +distributed")
    depends_on("py-distributed@2022.10.2", type=("build", "run"), when="@2022.10.2 +distributed")
    depends_on("py-distributed@2023.4.1", type=("build", "run"), when="@2023.4.1 +distributed")

    # Requirements for dask.diagnostics
    depends_on("py-bokeh@1.0.0:", type=("build", "run"), when="@2.0.0: +diagnostics")
    depends_on("py-bokeh@1.0.0:1,2.0.1:", type=("build", "run"), when="@2.26.0: +diagnostics")
    depends_on("py-bokeh@2.4.2:2", type=("build", "run"), when="@2022.10.2:2023.3 +diagnostics")
    depends_on("py-bokeh@2.4.2:", type=("build", "run"), when="@2023.4.0: +diagnostics")
    depends_on("py-jinja2", type=("build", "run"), when="@2022.10.2: +diagnostics")
    depends_on("py-jinja2@2.10.3", type=("build", "run"), when="@2023.4.0: +diagnostics")

    # Requirements for dask.delayed
    depends_on("py-cloudpickle@0.2.1:", type=("build", "run"), when="@2.7.0: +delayed")
    # The dependency on py-cloudpickle is non-optional starting version 2021.3.1
    depends_on("py-cloudpickle@0.2.2:", type=("build", "run"), when="@2.13.0:2021.3.0 +delayed")

    depends_on("py-toolz@0.7.2:", type=("build", "run"), when="@0.8.1: +delayed")
    depends_on("py-toolz@0.7.3:", type=("build", "run"), when="@0.14.1: +delayed")
    # The dependency on py-toolz is non-optional starting version 2021.3.1
    depends_on("py-toolz@0.8.2:", type=("build", "run"), when="@2.13.0:2021.3.0 +delayed")

    # Support for YAML configuration files
    # The dependency on py-pyyaml is non-optional starting version 2.17.1
    depends_on("py-pyyaml", type=("build", "run"), when="@0.18.0:2.17.0 +yaml")

    @property
    def import_modules(self):
        modules = ["dask"]

        if self.spec.satisfies("@0.9.0:"):
            modules.append("dask.bytes")

        if self.spec.satisfies("@:0.20.2"):
            modules.append("dask.store")

        if "+array" in self.spec:
            modules.append("dask.array")

        if "+bag" in self.spec:
            modules.append("dask.bag")

        if self.spec.satisfies("@:0.7.5 +distributed"):
            modules.append("dask.distributed")

        if "+dataframe" in self.spec:
            modules.append("dask.dataframe")
            if self.spec.satisfies("@0.8.2:"):
                modules.append("dask.dataframe.tseries")
            if self.spec.satisfies("@0.12.0:"):
                modules.append("dask.dataframe.io")

        if "+diagnostics" in self.spec:
            modules.append("dask.diagnostics")

        return modules
