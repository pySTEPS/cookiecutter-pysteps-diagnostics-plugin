#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

def test_diagnostics_discovery():
    """It is recommended to at least test that the diagnostic postprocessors provided by the plugin are
    correctly detected by pysteps. For this, the tests should be ran on the installed
    version of the plugin (and not against the plugin sources).
    """

    from pysteps.postprocessing import interface

    new_diagnostics = ["{{cookiecutter.diagnostic_name }}_xxx"]
    for diagnostic in new_diagnostics:
        assert diagnostic.replace("diagnostic_", "") in interface._diagnostics_methods


def test_diagnostics_with_files():
    """Additionally, you can tests that your diagnostic postprocessors correctly reads the corresponding
    some example data.
    """

    # Write the test here.
    pass
