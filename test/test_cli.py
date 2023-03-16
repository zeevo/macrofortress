from cli import cli
from click.testing import CliRunner


def test_example():
    runner = CliRunner()
    result = runner.invoke(cli, ["example"])
    assert result.exit_code == 0
    assert result.output == "Hello world.\n"
