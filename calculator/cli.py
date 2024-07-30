import click

from calculator.model import Calculator


@click.group()
@click.pass_context
def calc(ctx: click.Context):
    """ A simple calculator"""

    ctx.obj = {"calculator_object", Calculator()}


@click.command()
@click.argument('num1', type=float)
@click.argument('num2', type=float)
@click.pass_context
def add(ctx: click.Context, num1: float, num2: float) -> None:
    """Add two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.add(num1, num2)
    click.echo(result)


@click.command()
@click.argument('num1', type=float)
@click.argument('num2', type=float)
@click.pass_context
def subtract(ctx: click.Context, num1: float, num2: float) -> None:
    """Add two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.subtract(num1, num2)
    click.echo(result)


@click.command()
@click.argument('num1', type=float)
@click.argument('num2', type=float)
@click.pass_context
def multiply(ctx: click.Context, num1: float, num2: float) -> None:
    """Multiply two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.multiply(num1, num2)
    click.echo(result)
    

@click.command()
@click.argument('num1', type=float)
@click.argument('num2', type=float)
@click.pass_context
def divide(ctx: click.Context, num1: float, num2: float) -> None:
    """Divide two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.divide(num1, num2)
    click.echo(result)
    

calc.add_command(add)
calc.add_command(subtract)
calc.add_command(multiply)
calc.add_command(divide)