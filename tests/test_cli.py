import unittest
import os
from click.testing import CliRunner
from flintdata.scripts.cli import *

class CliTestCase(unittest.TestCase):
	def test_cli_no_option(self):
		runner = CliRunner()
		result = runner.invoke(cli)
		self.assertEqual(result.exit_code,0)

	def test_cli_help(self):
		runner = CliRunner()
		result = runner.invoke(cli, ['--help'])
		self.assertEqual(result.exit_code,0)

	def test_cli_version(self):
		runner = CliRunner()
		result = runner.invoke(cli, ['--version'])
		self.assertEqual(result.output,'flintdata, version 1.0.0\n' )
		self.assertEqual(result.exit_code,0)

	def test_cli_missing_arg_raster(self):
		runner = CliRunner()
		result = runner.invoke(cli, ['optimize-rasters'])
		self.assertEqual(result.output,'Usage: flintdata optimize-rasters [OPTIONS] RASTER_FILES...\n\nError: Missing argument "raster-files".\n' )
		self.assertEqual(result.exit_code,2)

	def test_cli_no_raster_file(self):
		runner = CliRunner()
		result = runner.invoke(cli, ['optimize-rasters', '', '-o', 'test_output'])
		self.assertEqual(result.output,'No files given\n' )
		self.assertEqual(result.exit_code,0)

	def test_cli_optimise_raster(self):
		runner = CliRunner()
		result = runner.invoke(cli, ['optimize-rasters', 'tests/Hansen_v1.7_gain.tif', '-o', 'test_output'])
		self.assertEqual(result.exit_code,0)

if __name__ == '__main__':
    	unittest.main()
