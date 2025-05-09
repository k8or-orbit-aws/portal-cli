import click
from commands import upload, search, scan, chart, transfer, deploy, get_scan_data

@click.group()
def cli():
    """Multi-action CLI for image management."""
    pass

cli.add_command(upload.upload)
cli.add_command(search.search)
cli.add_command(scan.scan)
cli.add_command(chart.chart)
cli.add_command(transfer.transfer)
cli.add_command(deploy.deploy)
cli.add_command(get_scan_data.get_scan_data)

if __name__ == "__main__":
    cli()
